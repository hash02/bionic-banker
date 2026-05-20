---
title: "How to Build a Folder Agent"
description: "Part 2 of the folder-agent idea: the pieces, the missing parts, and the small script that made the folder feel alive."
date: "2026-03-09"
tags: ["AI", "Agents", "Code"]
readTime: "12 min"
category: "AI"
featured: false
slug: "folder-agent-part2"
---

Part 2 of building a folder-watching agent in Python: the gap between an event listener and a real agent, the watchdog library for filesystem events, and the routing script that made the folder respond to file changes instead of just detecting them.

## The Honest Confession

      
After I published Part 1, I asked myself a question that I should've asked before writing a single word: *is this actually an agent?*

      
And the honest answer is no. Not yet.

      
What I built in Part 1 is a really well-organized set of scripts with good file hygiene. The outcome tracker detects patterns. The rule proposer generates proposals. The event router logs everything. It looks like agency. It *feels* like agency. But here's the test that breaks the illusion:

      
**If I close my laptop and walk away for a week, does anything happen?**

      
No. Nothing runs unless I open a chat window and trigger it. That's not an agent. That's a toolkit. A really good toolkit, but a toolkit. The difference between a toolkit and an agent is the same difference between a car with no ignition and a car that drives itself. The engine is there. The transmission works. But nothing moves until someone push-starts it.

      
So this article is about building the ignition.

      
        
        </iframe>
        
INTERACTIVE What separates scripts from agents: the four missing pieces

The four missing pieces are: a trigger that fires without human input, a loop that keeps running after the trigger fires, a recovery path when something breaks, and a way to report what happened. Without all four, what you have is a toolkit. A useful toolkit, but not an agent.

## The Trigger Problem

My Part 1 scripts ran when I told them to. I typed a command, the script ran, it finished, it stopped. That is the definition of a tool with a handle. You pick it up. You put it down.

An agent needs to pick itself up.

For a folder-watching agent, the trigger is a file system event. Something lands in the folder. That is the input. Not a human saying "run now." The file itself is the instruction.

Python's watchdog library solves this. You define a handler class that inherits from FileSystemEventHandler, override the on_created method, and tell watchdog to watch a path. When a file appears, your handler fires automatically.

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class FolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            route_file(event.src_path)

observer = Observer()
observer.schedule(FolderHandler(), path='./inbox', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

That while True loop at the bottom is the ignition. The observer is watching. The loop keeps the process alive. The handler fires when something happens.

## The Routing Problem

Knowing that a file appeared is not enough. You need to know what to do with it.

In my folder agent, routing is a decision about what kind of file just appeared. A PDF needs different handling than a CSV. A file named report-2026-05-20.json needs different handling than a file named alert-HIGH-wallet-flagged.json.

I built a simple router. It looks at the filename, checks it against a set of patterns, and dispatches to the right handler function. Nothing clever. Just a chain of if-else blocks that cover the cases I expect and log loudly when something shows up that I did not expect.

```python
def route_file(path):
    filename = os.path.basename(path)
    
    if filename.startswith('report-') and filename.endswith('.json'):
        handle_report(path)
    elif filename.startswith('alert-') and filename.endswith('.json'):
        handle_alert(path)
    elif filename.endswith('.csv'):
        handle_data_import(path)
    else:
        log_unknown(path)
```

The log_unknown call matters as much as the other handlers. An agent that silently drops unexpected inputs is an agent you cannot trust. The unknown log is how you find the gaps in your routing logic.

## The Recovery Problem

Scripts die quietly. You run a script, it throws an exception, it exits, and you find out when you come back and the output is not there.

An agent that dies is a gap in your coverage. If the folder watcher crashes at 2am, files are sitting in the inbox and nothing is processing them. You will find out in the morning when you look at the output and the timestamps are wrong.

Recovery has two layers.

The first layer is exception handling inside the handler. Wrap the processing in a try-except block. If something fails, log the error with the filename and the stack trace, and move the file to an error folder rather than leaving it in place.

```python
def handle_report(path):
    try:
        with open(path) as f:
            data = json.load(f)
        process_report(data)
        move_to_processed(path)
    except Exception as e:
        log_error(path, e)
        move_to_error(path)
```

The second layer is process-level recovery. If the whole observer crashes, it needs to restart itself. I use a supervisor script for this. The supervisor runs a loop. It checks whether the observer process is alive. If it is not, it restarts it and logs the restart event. Restarts get logged because frequent restarts mean something is broken at a deeper level and needs investigation.

## What the Working Agent Looks Like

Once all four pieces are in place, the agent has a different character than the toolkit that came before it.

You drop a file in the inbox. The observer fires within a second. The router decides what kind of file it is. The right handler processes it, moves it to processed, and writes output to the output folder. If something goes wrong, the file moves to error, the exception gets logged, and the observer keeps running. If the process crashes, the supervisor restarts it and logs the event.

I check the output folder in the morning. I check the error folder if something looks off. I check the restart log once a week.

That is it. The agent is handling the work. I am reviewing the output.

## What This Does Not Solve

A folder-watching agent is local. It runs on one machine. It monitors one path. It has no network awareness, no API surface, no way for another system to talk to it except by dropping files in the inbox.

That constraint is also the design. Dropping a file is a simple, explicit action. It is easy to audit. It is easy to test. It is easy to debug when something goes wrong.

The more interesting architecture question is what drops the files. If another agent generates a report and drops it into this agent's inbox, you have two agents coordinating without direct communication. One writes, one reads. The folder is the message bus.

That was actually how the multi-agent system I described in the agent-evolution post ended up being organized. Not by design. By the same problem-following logic: the simplest coordination mechanism that actually works is usually a shared folder with known file naming conventions.

Build the ignition first. The rest follows from there.
