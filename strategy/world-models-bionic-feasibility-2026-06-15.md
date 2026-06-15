# World Models Feasibility Note for Bionic Banker

Date: 2026-06-15
Status: research note, not installed

## Short answer

World models are worth covering as a tutorial/thought-leadership topic, but they are **not** the next production tool for Bionic Banker on Wukong.

The current machine has:

- NVIDIA GTX 1650
- 4GB VRAM
- CUDA available
- Ollama already using GPU memory
- system RAM under pressure during browser work

That is enough for small local LLMs, embeddings, lightweight computer-vision tests, and deterministic visual generation. It is not a comfortable environment for modern open-source interactive world models, which are usually video/generation-heavy and expect much larger GPUs.

## Why world models still matter

World models are a good Bionic topic because they connect to:

- simulation before action
- agents testing decisions before executing
- risk controls before real-world operations
- human review of imagined futures vs real evidence
- “do not confuse simulation with authority”

That fits the Bionic thesis:

> AI can simulate, predict, and propose. Finance still needs source trails, controls, and human authorization before action.

## Candidate open-source world-model signal

LingBot-World is an open-source world model project presented as an interactive, action-conditioned world simulator. Public materials describe:

- long-horizon world generation
- action-conditioned interaction
- video/simulation foundation
- Apache-2.0 open-source release
- scripts for fast inference and action/camera control

But practical install likely requires more VRAM than Wukong has for a usable demo. It is better to research and write first, then decide whether to test on cloud GPU or a larger local machine.

## Recommended Bionic tutorial angle

Title:

> What are world models, and why finance should care before agents act

Structure:

1. What a world model is
2. How it differs from a chatbot or video generator
3. Why it matters for agents: simulate before acting
4. Why simulation is not proof
5. Finance/risk example: agent wants to make a payment or strategy move
6. Human-in-the-loop control: review simulation, evidence, and authority boundary
7. Practical local reality: small machines can study concepts, not run frontier world simulators

## Recommended experiment

Do not install LingBot-World on Wukong tonight.

Instead:

1. Create a Bionic explainer/tutorial from public sources.
2. Build a small deterministic “world model lite” demo:
   - a toy transaction environment
   - agent chooses actions
   - simulator shows possible outcomes
   - human approval gate decides whether any real action happens
3. Publish it as a tutorial:
   - “World models for finance risk: simulate, then review”

This is better than forcing a heavy GPU demo that may fail or crawl.

## GPU usage status from live check

GPU is present and being used lightly:

- GTX 1650, 4GB VRAM
- about 793 MiB VRAM used at check time
- GPU utilization 0% at check time
- processes included `ollama` and a Python process

Interpretation:

- GPU is configured and visible.
- It is not actively doing heavy generation at the moment.
- It can support small local model workloads.
- It is not enough for comfortable modern world-model/video-generation research without careful constraints.

## Critical recommendation

Use world models as a **thought-leadership/tutorial lane**, not as an infrastructure dependency.

The Bionic position should be:

> The future is not “agents act autonomously because they can simulate.” The future is “agents simulate, humans review the boundary, then systems execute only inside approved controls.”
