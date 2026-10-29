---
title: "Black October: How AI Found a Decade-Old Flaw Under 7 in 10 Websites"
description: "PHP runs under about 7 in 10 measurable websites. In October 2026, AI models helped find two old flaws, and the rush to patch was measured in hours."
date: "2026-10-29"
author: "Hash"
tags: ["Security", "AI", "Web"]
readTime: "5 min"
category: "Tech"
featured: false
slug: "black-october-php"
image: "/blog-visuals/black-october-php/black-october-blog.jpg"
imageAlt: "Robot hand placing a padlock on a shield inside a browser window"
draft: true
---

By Hash

A lot of the web sits on software you never see. In October 2026, two old flaws in that software turned into a public scramble. CNBC and the Guardian report that some have dubbed the moment Black October.

## The hidden software under the page

PHP is the hidden software under about 7 in 10 websites, where the software can be measured. W3Techs puts that share at about 69%.

You do not download PHP the way you download a phone app. It runs on the server that builds the page. A shop, a school, a newsroom, or a government office can be using it with no logo in sight. When something this common has a hole, the hole is common too.

## The emergency fix

On Oct 21, 2026, PHP maintainers released an emergency fix for two critical flaws, CVE-2026-109618 and CVE-2026-109619. The patched versions are 8.5.12, 8.4.27, 8.3.36, and 8.2.35.

On an unpatched site, an attacker could make the server run commands with no password.

The flaws had been in the code for more than a decade, back to PHP 5.4. They were not a new invention. They were old code that had been sitting there.

## How AI models found them

Wiz, working with Calif and OpenAI, used AI models to find and test the flaws. Wiz says one researcher did in a week what used to take a world-class team months.

The bugs had waited years. The search did not.

## The race after the fix

Amazon threat intelligence saw an exploitation attempt on Oct 17, four days before public disclosure. Amazon said it was unclear whether those attempts succeeded.

After the announcement, the pace changed. Cloudflare's CEO said attempts went from thousands to millions within hours of the announcement, per the Guardian.

Governments in Canada (CBC) and Europe, including the Netherlands, Finland and France (CNBC), took some sites offline as a precaution. Pulling a site down is a rough way to buy time while people check whether the fix is in place.

On Oct 26, CISA added both flaws to its Known Exploited Vulnerabilities list.

## The short lesson

AI shrinks the gap between a fix and its exploitation. Once the repair is public, the flaw is easier for other people to spot. Amazon says to measure patch timelines in hours, not weeks.

## What everyday people can do

This section is general security practice. It is not a special tool for this one flaw, and you do not need to know whether a site runs PHP.

- Update your phone, browser, and apps promptly. The ordinary update is often the fix.
- Distrust "urgent security update" emails or texts that ask you to log in. Go to the site directly, by typing the address or using a bookmark you already trust.
- Turn on two-step verification for email and banking.
- Site maintenance outages are often patching. A short closure can be the safer choice.

## What businesses can do

- Ask your web team or provider if you run PHP and are on a patched version.
- Inventory every site and server, including forgotten ones.
- Set a patch-in-hours plan for critical fixes.
- Watch CISA's KEV list and Canadian Cyber Centre alerts.
- Keep firewall and admin management pages off the public internet.

## What happened next (Oct 26 to 29)

CISA gave US federal civilian agencies until Oct 29 to patch.

On Oct 27, the Canadian Centre for Cyber Security said public reporting shows both flaws are being actively exploited.

Researchers confirmed working attacks, mostly on test 'trap' servers. Perplexity researcher Adel Karimi recorded 35 successful takeovers on three such servers (SecurityWeek, The Register). Wiz said exposed vulnerable machines dropped about 67% in the days after disclosure.

In one real campaign, security firm Dream reports that attackers it links to China chained PHP2Shell with a Linux flaw called Fragnesia (CVE-2026-46300) to take full control of 25 Palo Alto Networks firewall and management servers in the US, Japan, Taiwan and South Korea, including three at a US government-affiliated organization. Palo Alto's Unit 42 confirmed the findings and says about 0.02% of its customers were affected and all were contacted. Dream saw signs of AI tools on the attackers' setup but says it has no direct proof AI wrote the exploit.

On Oct 28, CISA added Fragnesia to its known-exploited list.

Nepal brought more than 1,000 government websites back online after patching (Kathmandu Post, Oct 26).

Bottom line: working attacks are confirmed but still limited, and they mostly hit systems left exposed to the internet.

## Sources

- [PHP release archive, 2026](https://www.php.net/archive/2026.php)
- [Wiz on the PHP flaws](https://www.wiz.io/blog/php2shell-php-rce)
- [Amazon threat intelligence](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/)
- [The Guardian](https://www.theguardian.com/technology/2026/oct/23/cybersecurity-ai-hacking-php-vulnerability)
- [CNBC on the PHP flaws and cybersecurity](https://www.cnbc.com/2026/10/23/php-vulnerabilities-ai-cybersecurity.html)
- [CNBC on government sites](https://www.cnbc.com/2026/10/21/government-websites-go-dark-as-software-flaw-sparks-security-scramble.html)
- [CBC](https://www.cbc.ca/news/business/canadian-government-sites-down-php-cybersecurity-9.7390368)
- [CISA alert](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching)
- [Canadian Centre for Cyber Security](https://www.cyber.gc.ca/en/alerts-advisories/al26-026-critical-vulnerabilities-impacting-php-cve-2026-109618-cve-2026-109619)
- [SecurityWeek](https://www.securityweek.com/php2shell-exploitation-moves-from-probes-to-working-shells/)
- [The Register](https://www.theregister.com/cyber-crime/2026/10/27/cisa-confirms-php2shell-under-attack-as-researchers-clock-successful-exploits/5305681)
- [Wiz on exploitation so far](https://www.wiz.io/blog/php2shell-exploitation-so-far)
- [Dream](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)
- [Palo Alto Unit 42](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)
- [BleepingComputer](https://www.bleepingcomputer.com/news/security/cisa-warns-of-fragnesia-linux-flaw-chained-in-php2shell-attacks/)
- [Kathmandu Post](https://kathmandupost.com/science-technology/2026/10/26/most-nepal-government-websites-back-online-after-php2shell-flaw)
