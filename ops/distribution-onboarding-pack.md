# Bionic Distribution Onboarding Pack

Use when Himanshu is at Wukong screen.

## Goal

Enable X and Reddit distribution while keeping public actions approval-gated.

## Current status

- Website: live and working.
- LinkedIn: manual/browser workflow works.
- X: `xurl` installed, not authenticated.
- Reddit: no API credentials configured; browser/manual recommended first.

## X setup

Run:

```bash
xurl auth apps add
xurl auth status
```

If `xurl` asks for app/client details, use the X developer app for the account that should post Bionic content.

After auth, verify with a read-only command first:

```bash
xurl me
```

Posting policy after setup:

```text
Hermes may draft automatically.
Hermes must ask before posting, replying, quote-posting, or DMing.
```

## Reddit setup — recommended first mode

Use browser/manual first:

1. Open Reddit in Wukong Firefox.
2. Log in manually.
3. Tell Hermes it is ready.
4. Hermes will prepare comments/posts and stop before submit.

Why: Reddit trust is community-based. API posting too early can look like automation/spam.

## Reddit API later, if needed

Create app:

```text
https://www.reddit.com/prefs/apps
```

Provide credentials into Hermes env only when ready:

```bash
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USERNAME=
REDDIT_USER_AGENT="bionic-banker-research/0.1 by u/<username>"
```

Posting policy:

```text
Monitoring: automatic
Drafting: automatic
Posting/commenting: approval required
No link-first posts
Disclose affiliation when linking Bionic
```

## First platform actions after auth

### X

- post one short thesis from the agentic-payments checklist
- then one 5-part thread if the short post lands well

### Reddit

- observe 3–5 relevant threads
- write helpful comments without links first
- only link Bionic if the thread asks for framework/resources and affiliation is disclosed

## What Himanshu can do to make it possible

- Be at Wukong screen.
- Confirm which X account should be used.
- Complete any browser/OAuth screens.
- Log into Reddit manually if choosing browser mode.
- Confirm whether posting remains approval-gated. Recommended: yes.
