---
title: "Black October: How AI Found a Decade-Old Flaw Under 7 in 10 Websites"
description: "A plain account of the October 2026 PHP flaws under about 7 in 10 websites, how AI models found them, and what people can do."
date: "2026-10-29"
author: "Hash"
tags: ["Security", "AI", "Web"]
readTime: "8 min"
category: "Tech"
featured: false
slug: "black-october-php"
image: "/blog-visuals/black-october-php/black-october-bold.jpg"
imageAlt: "BLACK OCTOBER headline over a cracked glowing world map with an AI eye scanning it"
draft: false
---

By Hash

You have probably used a page today that PHP helped build. It might have been a shop, a school portal, a news article, or a government form. You did not install PHP. There is often no logo. It is the software on the server, the computer that answers when your browser asks for a site.

In October 2026, two old flaws in that software became an emergency. The public fix arrived on Oct 21. Within hours, attempts to use the flaws jumped from thousands to millions. Some governments took sites offline as a precaution. On Oct 23, CNBC and the Guardian reported that some people had started calling the moment Black October.

Here is the plain version: what PHP is, what the flaws allowed, how AI models found them, the day by day record, and what is still unconfirmed.

## What is PHP, in plain words

PHP is the hidden software under about 7 in 10 websites, where the software can be measured. W3Techs puts that share at about 69%.

A website is a short conversation. Your browser asks for a page. A server somewhere else builds the answer. It may look up a product, check a login, save a form, or pull a public notice. PHP is a common language for that work on the server. Because it is common, it is easy to forget. A site can run it for years with nothing on the screen that says so.

That is why a flaw here is not a niche story. If the software sits under most measurable sites, a mistake in it can sit under ordinary pages. About 7 in 10 is a measure of how widely PHP is used, where that use can be counted. It is not a claim that every site was attacked. Old copies linger because a site still works, or because a server was forgotten. A hidden flaw becomes urgent once someone can show where it is.

## The flaws

On Oct 21, 2026, PHP maintainers released an emergency fix for two critical flaws, CVE-2026-109618 and CVE-2026-109619. Those CVE numbers are public labels, so everyone can point at the same two bugs.

The patched versions are 8.5.12, 8.4.27, 8.3.36, and 8.2.35. If you run PHP, those are the version numbers that include this fix.

On an unpatched site, an attacker could make the server run commands with no password. The server would follow instructions from someone who never signed in. No account. No password prompt in the way. The machine that builds the page would do what that person told it to do.

That is different from a weak password. A password can be changed. On a server that had not taken the update, this flaw skipped the password entirely.

## How AI found them

The flaws had been in the code for more than a decade, back to PHP 5.4. They were not a new invention from October. They were old lines, carried forward while the web moved on.

Wiz, working with Calif and OpenAI, used AI models to find and test them. The flaws were found on Aug 19 and reported on Aug 24. Wiz says one researcher did in a week what used to take a world-class team months.

The models did not replace the person. They shortened the search. Someone still had to look, test, and report. A decade of this code sitting in public use, then a week of work to find and report it: that is the contrast Wiz is pointing at. The public repair still came later, on Oct 21. Between the August report and that fix, the flaws were still in software people were running.

## Timeline

- Aug 19: The flaws were found. There was no public fix yet.

- Aug 24: The flaws were reported. Wiz, working with Calif and OpenAI, had used AI models to find and test them. Wiz says one researcher did in a week what used to take a world-class team months. The code went back more than a decade, to PHP 5.4.

- Oct 17: Amazon threat intelligence saw an exploitation attempt, four days before public disclosure. Amazon said it was unclear whether those attempts succeeded. Someone was already trying. The public fix was not out. Success, for that early attempt, was not confirmed.

- Oct 21: PHP maintainers released the emergency fix in versions 8.5.12, 8.4.27, 8.3.36, and 8.2.35. The same day, some government sites went offline in Canada, the Netherlands, Finland, and France, as a precaution. CBC reported the Canadian outages. CNBC reported the European ones.

- Oct 21 to 22: Cloudflare saw attempts go from thousands to millions. Cloudflare's CEO said the jump happened within hours of the announcement, per the Guardian. A public fix tells defenders what to repair, and it also shows other people where the hole was.

- Oct 23: The Black October nickname appeared in CNBC and the Guardian. Both reported that some people had dubbed the moment Black October.

- Oct 24: Perplexity researcher Adel Karimi recorded 35 successful honeypot exploits on three test trap servers, machines put out to catch attacks rather than to run an ordinary public site. SecurityWeek and The Register reported the count. Working attacks were confirmed, and these ones were mostly on trap servers.

- Oct 26: CISA added both PHP flaws to its Known Exploited Vulnerabilities list and gave US federal civilian agencies until Oct 29 to patch. The same day, Nepal brought more than 1,000 government websites back online after patching, the Kathmandu Post reported.

- Oct 27: The Canadian Centre for Cyber Security said public reporting shows both flaws are being actively exploited. Wiz said exposed vulnerable machines dropped about 67% in the days after disclosure.

- Oct 28: CISA added Fragnesia, a Linux flaw numbered CVE-2026-46300, to its known-exploited list.

- Oct 29: Palo Alto's Unit 42 confirmed a campaign reported by the security firm Dream. Dream reports that attackers it links to China chained PHP2Shell with Fragnesia to take full control of 25 Palo Alto Networks firewall and management servers in the US, Japan, Taiwan, and South Korea, including three at a US government-affiliated organization. Unit 42 says about 0.02% of its customers were affected and all were contacted. Dream saw signs of AI tools on the attackers' setup, but says it has no direct proof AI wrote the exploit.

## Why AI changes the game

AI shrinks the gap between a fix and its exploitation.

The old plan was weeks. Hear about a serious flaw, test an update, and ship it at the next maintenance window. Amazon says to measure patch timelines in hours, not weeks. The October record is the reason. Found on Aug 19, reported on Aug 24, fixed in public on Oct 21, then a jump from thousands of attempts to millions within hours, across Oct 21 to 22.

Discovery sped up too. One researcher with AI models did in a week what Wiz says used to take a world-class team months, on bugs dating back to PHP 5.4. Once the fix was public, the repair also showed other people what to aim at, on any server still missing the update.

The change is the clock. Delay is the risky part. A patch-in-hours plan asks who can update a server the day a critical fix drops, including servers people forgot. Wiz later said exposed vulnerable machines dropped about 67% in the days after disclosure. The systems still easy to hit were the ones left exposed to the internet.

## What's confirmed and what isn't

Working attacks are confirmed, but they are still limited, and they mostly hit systems left exposed to the internet.

Confirmed: Amazon's Oct 17 attempt, with success unclear; Karimi's 35 honeypot exploits on three trap servers; active exploitation reported by the Canadian Centre for Cyber Security on Oct 27; and Dream's campaign, confirmed by Unit 42 on Oct 29, against 25 firewall and management servers, about 0.02% of Palo Alto customers, all contacted. Also confirmed: Wiz's drop of about 67% in exposed machines, and Nepal restoring more than 1,000 government sites after patching. The attacks that landed mostly hit systems left open to the internet.

No bank breach is confirmed.

Some claims circulating online are unverified. Stories about stolen passwords, botnets, and big unpatched percentages are in that group. They are not the counts above from Amazon, CISA, Wiz, the Canadian Centre for Cyber Security, or Unit 42. A striking number in a social post is not a confirmed measurement. If it is not in the record above, treat it as unverified.

## What you can do

### For everyday people

This part is general security practice. You do not need to know whether a given site runs PHP.

- Update your phone, browser, and apps promptly.
- Distrust "urgent security update" emails or texts that ask you to log in. Go to the site directly, by typing the address or using a bookmark you already trust.
- Turn on two-step verification for email and banking.
- Site maintenance outages are often patching. A short closure can be the safer choice, as when some government sites went offline on purpose and Nepal later restored more than 1,000 after the fix.

### For businesses

- Ask your web team or provider if you run PHP and are on a patched version: 8.5.12, 8.4.27, 8.3.36, or 8.2.35.
- Inventory every site and server, including forgotten ones.
- Set a patch-in-hours plan for critical fixes. Amazon's line is hours, not weeks.
- Watch CISA's KEV list and Canadian Cyber Centre alerts.
- Keep firewall and admin management pages off the public internet. Dream's confirmed campaign took full control of firewall and management servers attackers could reach.

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
