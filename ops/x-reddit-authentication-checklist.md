# X + Reddit Authentication Checklist for Bionic Distribution

Purpose: prepare the system for X/Reddit distribution without interrupting Himanshu until he is at the screen.

## Current status

- X: `xurl` is installed, but no app is registered.
- Reddit: no API credentials detected.
- Public posting remains gated. Research and drafts can continue without credentials.

## What Himanshu needs to provide when at the screen

### X / Twitter via xurl

Run or let Hermes run interactively when ready:

```bash
xurl auth apps add
```

Needed from X developer/app setup or browser auth flow:

- X app/client credentials required by `xurl`
- account authorization for Bionic/Himanshu posting
- confirmation whether Hermes may post drafts automatically or only prepare them

Preferred policy:

```text
Research: automatic
Drafting: automatic
Posting: approval required
Replying/commenting: approval required until trust is established
```

### Reddit

Option A — browser/manual workflow:

- log into Reddit in Wukong browser
- Hermes prepares comments/posts
- Himanshu approves before posting

Option B — Reddit API workflow:

Create Reddit app at:

```text
https://www.reddit.com/prefs/apps
```

Provide/store these in Hermes environment:

```bash
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USERNAME=
REDDIT_PASSWORD=
REDDIT_USER_AGENT="bionic-banker-research/0.1 by u/<username>"
```

Preferred policy:

```text
Subreddit monitoring: automatic
Comment drafting: automatic
Posting/commenting: approval required
No link dumping
Disclose affiliation when linking Bionic
```

## What can continue without credentials

- competitor radar
- web research
- Reddit public-page monitoring via search/extract
- X public web monitoring when available
- draft posts/threads/comments
- website/blog/checklist/tutorial creation
- visual/carousel improvements
- source maps and control maps

## Publication gates

Stop and ask before:

- posting to X/Reddit/LinkedIn
- replying to a person
- sending DMs
- using paid APIs/apps
- changing profile/account settings
- entering credentials into forms
- handling KYC/tax/bank/payout/payment settings
