---
title: "Claude Max as Your Personal API"
description: "$100/month flat rate. Unlimited API requests. Here's how I built a proxy that turns Claude Max into an OpenAI-compatible endpoint."
date: "2026-03-17"
tags: ["AI · Economics · Code"]
readTime: "11 min"
category: "Tech"
featured: false
slug: "claude-proxy-api"
---

Okay so—here's the problem. Claude API is metered per token. Every request costs something. You're building an agent? That's 100 requests a day minimum. Testing a chatbot? Friction everywhere. And if you're serious about AI, you want to experiment without checking your credit card balance after every spike.

    
But Claude Max is $100 a month. Flat rate. Unlimited requests. No per-token treadmill.

    
The gap between these two worlds is wild. You've already paid for Claude Max on your local machine. But there's no official way to use it programmatically. The `claude` CLI talks to you. It doesn't talk to code.

    
Until now.

    
Here's what I built: a Python proxy that wraps the Claude CLI into an OpenAI-compatible API endpoint. Your agents and tools think they're hitting a normal API. They're actually talking to the `claude` command on your local machine. Same interface shape. Different engine underneath.

    
$100/month flat rate. Unlimited agent requests. Problem solved.

    
## Why This Matters

    
Think about the economics for a second. Claude API is like $3 per million input tokens, $15 per million output tokens. You run a few agent tests and you're bleeding money—not a lot of money individually, but it adds up. Every experiment costs something. Every iteration costs something.

    
With Max, you've already paid $100. One time. The marginal cost of the next request is zero. And I mean zero. Not "small"—actually zero.

    
Now imagine building an agent system. Or running 100 variations of a prompt. Or doing recursive reasoning where the model thinks about its own thinking. In the cloud, you're optimizing for fewer tests because tests cost money. When tests are free? You run everything. You stress-test without fear. You find the breaking points because you're not afraid to look.

    
That's a different way of working entirely.

    
## How the Proxy Works

    
The architecture is straightforward. Three layers.

    
**Layer 1: HTTP Server** — Flask app listening on localhost:8000. It exposes the OpenAI-compatible endpoints: `/v1/chat/completions`, `/v1/models`, etc. Any tool that speaks OpenAI just works.

    
**Layer 2: Request Translation** — When a request arrives, the proxy unpacks the OpenAI format and rebuilds it as a Claude prompt. System message goes to the system parameter, user messages get concatenated, parameters like `temperature` and `max_tokens` get passed through.

    
**Layer 3: CLI Bridge** — The key part. Instead of hitting the API endpoint, we call `claude -p` in a subprocess. Same tool you use in the terminal. Same authentication (Claude CLI already has your credentials). Same underlying service.

    
Here's the core logic:

    
```
import subprocess
import json
import time
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    """
    Accept OpenAI-format request, proxy to claude CLI, return response.
    Why subprocess: Claude CLI is already auth'd. We just shell out to it.
    Why jsonify: OpenAI format is standardized. Tools expect it.
    """
    data = request.json
    messages = data.get('messages', [])
    temperature = data.get('temperature', 1)
    max_tokens = data.get('max_tokens', 8096)
    stream = data.get('stream', False)

    # Extract system prompt and user messages
    system_msg = next((m['content'] for m in messages if m['role'] == 'system'), '')
    user_msgs = [m['content'] for m in messages if m['role'] == 'user']
    prompt_text = '\n'.join(user_msgs)

    # Build CLI command
    # Why CLI args: The claude tool expects these flags.
    # Why we pass them: temperature affects response randomness, max_tokens prevents runaway
    cmd = ['claude', '--temperature', str(temperature), '--max-tokens', str(max_tokens)]

    if system_msg:
        cmd.extend(['--system', system_msg])

    cmd.extend(['-p', prompt_text])

    # Run subprocess
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

    if result.returncode != 0:
        return {'error': result.stderr}, 500

    response_text = result.stdout.strip()

    # Return OpenAI-compatible response
    # Why this format: Any tool expecting OpenAI API just consumes it
    openai_response = {
        'id': 'claude-proxy-' + str(int(time.time())),
        'object': 'chat.completion',
        'created': int(time.time()),
        'model': 'claude-3-5-sonnet',
        'choices': [{
            'index': 0,
            'message': {'role': 'assistant', 'content': response_text},
            'finish_reason': 'stop'
        }],
        'usage': {
            'prompt_tokens': len(prompt_text.split()),
            'completion_tokens': len(response_text.split()),
            'total_tokens': len((prompt_text + response_text).split())
        }
    }

    return jsonify(openai_response)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=False)
```

    
That's it. You point your tool at `http://localhost:8000`, set the model to `claude-3-5-sonnet`, and it works. LangChain, CrewAI, custom agents—doesn't matter. They all speak OpenAI format. The proxy translates it to CLI calls. The tool never knows the difference.

    
## Streaming: The Real-Time Version

    
The basic version works for batch calls. But here's where it gets better—streaming.

    
Most LLM tools want responses arriving in real time, chunk by chunk. Not one giant blob at the end. The Claude CLI supports streaming natively (add the `--stream` flag), so the proxy just pipes it through:

    
```
@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.json
    stream = data.get('stream', False)

    # ... build command same as before ...
    cmd = ['claude', '--stream', '-p', prompt_text]

    if stream:
        def generate():
            """
            Stream chunks back as Server-Sent Events (SSE).
            Why SSE: It's the standard for streaming responses.
            Any HTTP client can parse it. Browsers, Python, everything.
            """
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )

            for line in process.stdout:
                # Convert to OpenAI streaming format
                chunk = {
                    'choices': [{
                        'delta': {'content': line},
                        'index': 0,
                        'finish_reason': None
                    }]
                }
                yield f"data: {json.dumps(chunk)}\n\n"

            # Final chunk signals completion
            yield 'data: [DONE]\n\n'

        return Response(generate(), mimetype='text/event-stream')

    # ... non-streaming path ...
```

    
The subprocess spawns, output flows back line by line, converted to SSE format. Your tool consumes it exactly like it would from OpenAI. Real-time tokens arriving as they're generated. There's maybe 200—500ms of subprocess overhead, but that's noise compared to generation time.

    
## Groq Fallback: Because Resilience Matters

    
Here's something I added because I'm paranoid about uptime—and because systems should have backups.

    
If Claude fails (network issue, CLI crash, whatever), the proxy falls back to Groq. Free Groq API. Open source models. Lower quality, but it runs.

    
```
def get_response(prompt, system_msg, max_tokens, temperature):
    """
    Try Claude first. If it fails, use Groq.
    Why fallback: Better to degrade than to crash.
    Why Groq: Free API, reasonable latency, available.
    """
    try:
        cmd = ['claude', '--stream', '--max-tokens', str(max_tokens)]
        if system_msg:
            cmd.extend(['--system', system_msg])
        cmd.extend(['-p', prompt])

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fall back to Groq if Claude fails
    return get_groq_response(prompt, system_msg, max_tokens, temperature)

def get_groq_response(prompt, system_msg, max_tokens, temperature):
    """Groq fallback using free API key."""
    from groq import Groq
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    message = client.messages.create(
        model="mixtral-8x7b-32768",
        max_tokens=max_tokens,
        temperature=temperature,
        system=system_msg,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text
```

    
The effect: Claude goes down, Groq picks up. Tool doesn't care. It gets a response. Quality drops, but the system keeps running. You get degraded data instead of no data.

    
That's the kind of resilience you want. Not "single point of failure," but "degraded mode."

    
## The /v1/models Endpoint

    
Some tools check `/v1/models` to see what's available. The proxy fakes this response so tools don't error out:

    
```
@app.route('/v1/models', methods=['GET'])
def list_models():
    """
    List available models in OpenAI format.
    Why we fake it: Tools check this before making requests.
    Why hardcoded: We're routing everything to the local CLI anyway.
    """
    return jsonify({
        'object': 'list',
        'data': [
            {'id': 'claude-3-5-sonnet', 'object': 'model', 'owned_by': 'anthropic'},
            {'id': 'claude-3-opus', 'object': 'model', 'owned_by': 'anthropic'},
            {'id': 'claude-3-haiku', 'object': 'model', 'owned_by': 'anthropic'}
        ]
    })
```

    
Right now everything routes to whatever the local `claude` CLI defaults to. It's a future feature to pick different models. But this endpoint prevents tools from failing when they check what's available.

    
## What You Get

    
**Free agent requests.** Claude Max pays for itself if you're testing agents or building systems.

    
**No per-token math.** Your Max subscription is one flat price. No "quota exceeded" errors. No checking the billing page after each experiment.

    
**OpenAI-compatible.** Any tool that speaks OpenAI format works immediately. LangChain, CrewAI, your own custom code—drop in the localhost endpoint and it runs.

    
**Streaming responses.** Real-time tokens arriving as they're generated. Feels snappy. Tools that consume streaming just work.

    
**Fallback resilience.** Claude fails? Groq picks up. System keeps running in degraded mode.

    
**Local execution.** No data leaves your machine. No third-party service. Just your CLI, Python, and your network.

    
## The Limitations (Being Honest)

    
This isn't a replacement for production cloud infrastructure. It's a proxy, not a platform.

    
**Single machine.** Everything runs on one box. If your machine goes down, so does the proxy. If you need high availability across multiple regions, you're back to the API. But for building and testing locally? This is fine.

    
**No horizontal scaling.** You can't load-balance across 10 machines. If you need that, you'd write a coordinator that spawns multiple proxy instances on different ports and routes to them. Worth doing if you need it, but it's not built in.

    
**CLI latency.** Every request spawns a new subprocess. That overhead (maybe 200—500ms) is small compared to token generation time, but it's there. A direct API call is faster.

    
**Sequential requests.** If two requests arrive simultaneously, they queue. The CLI processes them one at a time. For local development and small agent systems, this is fine. For high-concurrency scenarios, you'd need to rearchitect.

    
**ToS gray area.** I'm reading Anthropic's terms. Using Claude Max programmatically isn't explicitly forbidden, but it's not explicitly blessed either. The CLI is a first-party tool, so technically you own the request. But if you're building something commercial, you should probably ask Anthropic first.

    
**No multi-turn state.** Every request is independent. The proxy doesn't remember conversation history. You pass it back each time. It's doable—you manage state in your calling code—but it's not automatic.

    
## What We Actually Learned

    
The real insight here isn't about saving money on Claude API. It's about abstraction layers.

    
The Claude CLI and the Claude API are two different interfaces to the same underlying service. Both are useful. The API scales horizontally but costs per token. The CLI is local and flat-rate but doesn't integrate with code.

    
By writing a translation layer between them, we're not exploiting a loophole—we're just adapting one interface to work with tools that expect another. This is how good systems get built. Stripe's API wraps payment processing. OpenAI's API wraps their models. A proxy wraps the CLI.

    
The proxy itself is thin. Maybe 100 lines of real logic. It doesn't add intelligence—it just adapts. And that's the lesson: sometimes the biggest value is in the glue layer. The thing that makes incompatible pieces talk to each other.

    
## How to Build This

    
Here's what you need:

    
1. **Prerequisites:** Claude Max subscription + Claude CLI installed + Python 3.8+ with Flask

    
2. **Optional:** Groq API key (free account) if you want fallback resilience

    
3. **Port:** Run on 8000. You can change it, but 8000 is clean.

    
4. **Networking:** For local development, `localhost:8000` works fine. If you need to access it from another machine, bind to `0.0.0.0` and firewall appropriately (or use Tailscale).

    
The full code is about 250 lines. Flask app, streaming, fallback, model endpoint. Took me about 4 hours to stabilize and test.

    
## Why This Actually Matters

    
Here's the thing: you already bought Claude Max. You're paying $100 a month. The cost of the next request is actually zero—not "small," literally zero.

    
This changes how you work. When every test costs money, you optimize for fewer tests. You polish arguments instead of running them. You guess instead of verify.

    
When tests are free? You run 100 variations. You break things intentionally. You find the breaking points because you're not afraid to look.

    
That's a different system entirely.

    
Also: if you're serious about agents, about building systems that think, about running experiments—this pays for itself immediately. Your Max subscription probably costs you nothing per agent request, when the economics actually matter.

    
## One Last Thing

    
If Anthropic releases an official way to use Claude Max programmatically, this post becomes a museum piece. And that's fine. That's the healthy outcome. But until they do, this is a working exploit of the economics. $100/month beats per-token billing every time, if your use case fits.

    
You already own the tool. Might as well make it work for what you're actually building.

    <!-- CTA BLOCK -->
    
      <!-- gradient top line -->
      

      
        🚀 Ready to Build
      
      
### Unlock Free Agent Requests

      
The proxy code runs locally. No APIs, no cloud bills, no per-token math. Just your Claude Max and the freedom to experiment.

      
        [
          View on GitHub →
        ](https://github.com/hash02)
