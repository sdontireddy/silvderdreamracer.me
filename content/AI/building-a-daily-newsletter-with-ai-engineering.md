Title: Building a Daily Newsletter with AI Engineering: What Actually Worked
Date: 2026-08-12 08:00
Author: sdontireddy
Category: AI
Tags: AI, Supply Chain, Automation, System Design
Slug: building-daily-newsletter-ai-engineering
Status: published

---

# AI Engineering: What I Learned Turning a Personal AI Project Into a Live System

Keeping up with technological change in the supply chain world had become increasingly difficult.

There was no shortage of information. Every week brought new articles, vendor announcements, podcasts, research, product updates, and opinions covering warehouse automation, robotics, AI, transportation, fulfillment, and emerging platforms.

The challenge was not finding information.

The challenge was separating useful signals from the noise.

I wanted a better way to stay current without spending hours reading through dozens of sources. At the same time, I had been developing my AI skills and wanted a practical project where I could apply them to a problem I understood well.

That led me to build [**Supply Chain Tech Signals**](https://supplychaintechsignals.com/).

The idea was simple:

> Build a system that continuously scans supply chain technology content, filters out low-value information, identifies the strongest signals, and explains why those developments matter.

Every morning, the system scans RSS feeds, podcast episodes, blog articles, and browser-extracted content across more than a dozen sources. It cleans and normalizes the content, removes duplicates, scores stories for relevance, selects the strongest signals, generates concise analysis with an LLM, and publishes the final newsletter.

At first, this sounded like a simple AI automation project.

It was not.

The first version was easy to build. The real learning started when I tried to make the system run every day and consistently produce something useful.

## How the Project Evolved

The first version was basic.

I passed an article title and summary to an LLM and asked:

> Why does this matter?

The responses were readable, but many were generic. They often summarized the article instead of explaining why the development mattered.

My first instinct was to improve the prompt.

But the real problem was the context.

The model was being asked to make a useful judgment with very little structured information.

So the system evolved.

Before a story reaches the LLM, the application now prepares information such as:

- cleaned and deduplicated content
- normalized technology tags
- supply chain themes
- company names
- source quality
- publication date
- freshness
- trend signals

The LLM no longer has to determine everything from scratch.

Its job is much narrower:

> Given this context, explain why this development matters.

That one change significantly improved the usefulness of the output.

## Lesson 1: Better Context Matters More Than Better Prompts

One of the biggest lessons from this project was that prompt engineering alone only gets you so far.

A better prompt can help, but it cannot compensate for weak or poorly structured input.

The surrounding application needs to prepare the right context first.

That changed the architecture.

Instead of asking the model to clean, classify, score, rank, interpret, and explain everything, I moved many of those responsibilities into normal application logic.

The model is now used mainly where judgment and language reasoning add value.

The principle became:

**Software prepares the facts and structure.AI explains what they mean.**

That made the system more predictable and easier to improve.

## Lesson 2: Do Not Use AI for Everything

As the project evolved, it became tempting to use the LLM for more and more tasks.

It could classify articles.

It could generate tags.

It could rank stories.

It could decide what was relevant.

But just because AI can do something does not mean it should.

Many tasks are more reliable when handled deterministically.

Today, normal application logic handles areas such as:

- deduplication
- classification
- tagging
- scoring
- taxonomy mapping
- freshness
- exclusions
- validation

The LLM is primarily responsible for:

- interpretation
- synthesis
- explanation
- why the story matters

This separation became one of the strongest architectural decisions in the project.

The application determines:

> What is this story about?

The LLM determines:

> Why should someone care?

## Lesson 3: Filtering Is More Important Than Collecting

Initially, adding more sources seemed like an obvious improvement.

But more sources also meant more noise.

A story could mention AI, robotics, logistics, or automation and still have very little practical relevance to supply chain technology.

So the system needed stronger filtering.

Stories are broadly classified into areas such as:

- direct supply chain
- adjacent technology
- general technology

Low-value content is removed before it reaches the LLM.

That includes content such as:

- job postings
- event promotions
- award announcements
- other editorial noise

This changed the objective of the system.

The goal was no longer:

> Collect as much information as possible.

It became:

> Find the small amount of information actually worth paying attention to.

That is a much more useful problem to solve.

## Lesson 4: Guardrails Need to Live Outside the Model

Once the newsletter started running every day, another issue became obvious.

Even a capable model can occasionally produce something too generic, too long, irrelevant, or overly promotional.

Simply adding another sentence to the prompt was not enough.

The system needed actual controls.

So guardrails were added around:

- relevance thresholds
- source quality
- freshness
- exclusions
- output length
- vendor neutrality
- post-generation validation

The important distinction is that these limits are enforced by the application.

The model generates the analysis.

The surrounding system decides whether the result stays within the expected boundaries.

That produced another practical lesson:

**Important rules should be enforced by software, not left entirely to the model.**

## Lesson 5: Real Usage Changes the Architecture

Some of the most useful improvements were not obvious when I started.

They appeared only after reviewing the newsletter every day.

Repeated runs exposed issues such as:

- duplicate reporting appearing as multiple signals
- older articles outranking breaking news
- vendor content receiving too much weight
- inconsistent source formats
- repeated themes dominating several issues
- keywords becoming noisy

Each problem led to another improvement:

- stronger deduplication
- freshness weighting
- source tiering
- taxonomy normalization
- diversity controls
- source normalization

This changed how I thought about the project.

The architecture was not something I designed once and completed.

It evolved through a simple loop:

> Build → Run → Review → Adjust → Repeat

The daily output became part of the development process.

## Lesson 6: Cost Is an Architecture Decision

As the system began processing more stories, cost became part of the design.

The easiest approach would have been to send every incoming article to the LLM and let the model decide what mattered.

That would also have been wasteful.

Instead, the pipeline performs cheaper processing first:

```text
Collect
   ↓
Clean
   ↓
Deduplicate
   ↓
Classify
   ↓
Score
   ↓
Filter
   ↓
Select
   ↓
LLM Analysis
```

Only the strongest stories reach the model.

A typical day may start with dozens of candidate stories, while only a much smaller set reaches the final AI-generation stage.

This significantly reduces unnecessary model calls.

The lesson was straightforward:

**One of the best ways to control AI cost is to avoid unnecessary AI calls.**

## Lesson 7: Production Systems Need to Expect Failure

Once a system runs every day, reliability matters.

Feeds can break.

Websites can change their format.

Requests can time out.

A model endpoint can become temporarily unavailable.

So the pipeline gradually gained:

- retry logic
- exponential backoff
- model fallback
- fallback analysis
- normalization for inconsistent source formats

The goal is not to pretend failures will never happen.

The goal is to make sure one failure does not stop the entire process.

## What the System Became

What started as a personal project to help me keep up with supply chain technology gradually became a practical AI engineering exercise.

The current flow is roughly:

```text
Sources
   ↓
Collect
   ↓
Clean and Normalize
   ↓
Deduplicate
   ↓
Classify and Tag
   ↓
Score and Filter
   ↓
Apply Guardrails
   ↓
Select the Best Stories
   ↓
Generate LLM Analysis
   ↓
Validate
   ↓
Publish
```

Every step exists because of something learned from running the system repeatedly.

That is what made the project interesting.

The AI model itself was never the hardest part.

The harder questions were:

- What information should I collect?
- What should I ignore?
- How should I structure the information?
- What should deterministic software handle?
- What should the LLM handle?
- How should quality be enforced?
- How should cost be controlled?
- How should failures be handled?

Those questions shaped the system far more than the original prompt.

## The Main Takeaway

I started Supply Chain Tech Signals because I wanted a better way to keep up with technological developments in supply chain without spending hours sorting through noisy information.

AI helped solve that problem.

But the biggest lesson from building the project was broader:

**A useful AI system is not built by putting a model in the middle of everything.**

Traditional software is still better at many things:

- structure
- rules
- filtering
- validation
- consistency
- control

AI is particularly useful where the process needs:

- interpretation
- synthesis
- explanation
- judgment

The strongest system combines both.

The surrounding application prepares reliable information and creates boundaries.

The model works inside those boundaries and handles the part where language reasoning adds real value.

**That is how this project evolved from**

- collecting articles --> filtering signals --> to refining context --> to applying AI selectively --> to building something useful enough to run every day

---

**This article documents engineering decisions from a live daily automation pipeline running since mid-July 2026. The examples reflect implementation choices made while operating and refining the system.**

**SEO summary:** Practical lessons from building an automated daily supply-chain newsletter with LLM-powered commentary, including context refinement, guardrails, deterministic-first processing, evaluation habits, reliability, and cost optimization for production AI systems.

**Suggested social excerpt:** I built a daily AI newsletter that scans 12+ sources and publishes every morning. The biggest lesson was not about prompts: production AI works better when software handles structure, rules, and guardrails, while the model is used selectively for judgment and explanation.
