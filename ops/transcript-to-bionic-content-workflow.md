# Transcript-to-Bionic Content Workflow

This documents Himanshu's natural content flow and turns it into a repeatable system.

## Raw flow

```text
Himanshu talks to any model / records thoughts / sends transcript
→ Hermes sharpens the idea
→ Hermes researches sources and competitors
→ Hermes creates Bionic artifact
→ Himanshu approves public distribution
```

## Better operating flow

### Step 1 — Capture

Input can be:

- Telegram voice transcript
- copied chat with another model
- rough idea dump
- article link
- market signal
- competitor post

### Step 2 — Prompt layer

Hermes converts raw input into:

```text
Goal:
Audience:
Claim:
Evidence needed:
Bionic angle:
Artifact type:
Distribution target:
Approval gate:
```

### Step 3 — Research layer

Check:

- source links
- competitor framing
- market context
- what is overdone/generic
- what Bionic can uniquely say

### Step 4 — Artifact layer

Pick one primary artifact:

- blog/source map
- tutorial
- LinkedIn post
- carousel
- checklist
- X thread
- Reddit discussion/comment
- lab/demo page

### Step 5 — Distribution layer

Adapt platform-native:

```text
Website = canonical source
LinkedIn = professional authority
X = short thesis / discourse
Reddit = helpful discussion, not link dump
Dev.to/Hashnode = tutorial/code/process
```

### Step 6 — Approval

Hermes may draft automatically.
Hermes stops before public posting/commenting/replying unless Himanshu approves.

## Content quality rule

Every Bionic artifact should include at least one of:

- source trail
- control map
- checklist
- risk boundary
- practical demo
- human-in-the-loop decision point

If it has none of those, it is probably generic content.

## Best prompt from Himanshu

A good short prompt is enough:

```text
I found this interesting: <link/transcript>. Turn it into a Bionic angle and tell me if it is worth posting.
```

Hermes should then do the sharpening internally and execute.
