# Public Copy Scan — Banned Phrases and Scan Protocol

Source: CLAUDE.md writing voice rules + accumulated website care turns
Use: run this checklist before any blog post publish or public website copy change
Last updated: 2026-05-23

---

## Scan Protocol

Run in order before marking any blog draft publish-ready:

1. **Voice check** — read the draft aloud. Does it sound like a voice note or a press release?
2. **AI-ism scan** — grep for banned words (list below)
3. **Long-dash check** — grep for `—` and `–` (em-dash, en-dash). Zero allowed. Restructure or use period/comma.
4. **Claim verification** — every factual claim has a source, [VERIFY] marker, or is explicitly hedged
5. **Privacy scan** — no private paths, machine names, IPs, agent identifiers, tool names, or internal system details in public copy
6. **Draft flag** — `draft: true` in frontmatter until HASH gives taste pass
7. **Media placeholder check** — every infographic slot has `<!-- INFOGRAPHIC: slug - pending render -->` comment
8. **Word count** — confirm within target range (1,300-3,000 words for blog posts)
9. **Bank/company tone** — no criticism of specific institutions. Optimistic framing only.

---

## Banned Words (hard ban — AI-isms)

delve, leverage, utilize, facilitate, foster, harness, embark, beacon, robust, vital, crucial, comprehensive, innovative, transformative, empowering, revolutionary, groundbreaking, seamless, streamlined, holistic, actionable, impactful, tapestry, realm, landscape, ecosystem, synergy, paradigm, visionary, disruptive, unpack, moreover, furthermore, indeed, certainly, absolutely

## Banned Phrases (hard ban)

"it's important to note that", "let's explore", "in conclusion", "to summarize", "navigate the complexities", "bridging the gap", "game changer", "paradigm shift", "cutting-edge", "state-of-the-art", "best practices", "thought leader", "moving forward", "at the end of the day", "needless to say", "I hope this helps", "Great question!", "it goes without saying", "deep dive", "pain point", "circle back", "touch base", "boils down to"

## Private Identifier Scan (never publish)

- Machine names: Maya, KAYA, KALA, Wukong, Dell, ASUS TUF
- Internal paths: hash02-workspace, maya01-brain, ~/.hermes, OneDrive paths
- Internal IPs: 100.86.26.81, 100.124.88.105, 100.110.76.34
- Internal tools: msg.py, wukong_reply.sh, check_inbox.sh
- Agent Chess system internals: ADAR loop filenames, cloudcode-turn-NNN references
- Employer reference: CIBC by name in risky context — optimistic framing only

## Identity Rule

HASH's name in public output: Himanshu, Himanshu H., or Himanshu.h ONLY.
Never: surname added, initial-plus-surname.
Email exception: himanshugautam991@gmail.com stays intact as the actual email address.

