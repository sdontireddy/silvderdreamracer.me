Title: About Me
Author: sdontireddy
Slug: aboutme
Status: published
Save_as: aboutme.html

Hi, I'm Sarath Dontireddy
===============

I'm a Solution Architect with deep experience in building enterprise systems that actually work in production. I focus on integration architecture, warehouse automation, AS/RS systems, and using AI to solve real operational problems.

---

## What I Do

### Enterprise Integration & API Architecture
Integration is where most enterprise systems fail — not because the core logic is wrong, but because boundaries are unclear and failure modes aren't handled.

#### Approach

I treat integration as a product capability, not just a connection problem. I focus on:

- **Contract clarity** : stateless APIs, solid contracts, explicit versioning
- **Failure handling** : retries, circuit breakers, dead-letter queues, compensation flows
- **Middleware discipline** : use ESB for mediation, transformation, and governance — not as the business logic layer
- **Observability** : interface health, latency, queue depth, exception trends


### Warehouse Automation & AS/RS Systems
I've spent significant time working with automated storage and retrieval systems (AS/RS), integrating warehouse management systems with material handling equipment (MHE), and designing systems that run 24/7 in high-throughput environments.

#### Technical focus:

- Integrate WMS with AS/RS / MHE platforms: AutoStore, sortation, conveyance systems, robotic picking
- Build observability into automated operations
- Handle high-volume message flows between control systems and warehouse execution layers with focus on infrastructure stability ,relability and security 

**Recent work:**
- AutoStore integration: designed message flows for putaway, picking, cycle counts, and inventory reconciliation between warehouse control and automated storage systems
- Built automated test environments where QE teams can validate system behavior within automated facilities
- Extended Manhattan Active WMS systems with 25+ custom extensions across UI, Entity and Business extensions 

### Cloud Architecture & DevOps
I've led cloud migrations for enterprise systems, moving from on-prem monoliths to service-oriented architectures on AWS.

#### Practices:
- Phased migration using domain-based service extraction
- Pre-warming infrastructure for peak traffic (flash sales, holiday spikes, event-driven loads)
- RDS Proxy for connection pooling during traffic spikes
- Soft/hard limit awareness and capacity planning
- CI/CD pipelines that support both stabilization and incremental feature delivery
- Infrastructure-as-code for reproducible environments

### AI & RAG Systems
Recently, I've been building local AI tools and exploring how AI agents can improve enterprise workflows, operational support, and decision-making.

#### What I'm building:
- Local RAG (Retrieval-Augmented Generation) systems for private knowledge bases
- AI agents that triage support tickets, summarize meeting notes, and search project documentation
- Automated newsletter pipelines that curate technology signals from RSS feeds and podcasts
- Local-first tooling that runs on a VPS without relying on cloud APIs for every query

The goal is not to replace human judgment but to reduce time spent on repetitive context retrieval and decision-support work.

#### Live projects:
- [Supply Chain Tech Signals](https://supplychaintechsignals.com/) — automated daily newsletter curating warehouse, automation, fulfillment, visibility, transportation, and AI insights from RSS feeds, podcasts, and vendor content. Built with automated ingestion pipelines, editorial scoring, and static site deployment to Cloudflare Pages.

---

## A Project That Shaped My Thinking

### Enterprise OMS Migration (Fanatics)

At Fanatics, I worked on modernizing a legacy global order management platform from a tightly coupled on-prem setup toward an AWS-based, service-oriented architecture.

**The approach was phased, not big-bang:**

1. **Stabilize first** — We didn't start by rebuilding. We stabilized the legacy stack, understood peak-day failure patterns, and created stress-testing capability to expose bottlenecks early. This gave us a reliable baseline.

2. **Map the landscape** — We documented the full legacy ecosystem: core business components, upstream/downstream dependencies, shared databases, integration touchpoints, and cross-functional flows. This helped us distinguish between true business domains, shared technical services, and brittle dependencies that needed decoupling.

3. **Extract by domain** — We identified major business capabilities that could be separated into domain-oriented services:
   - Order Status Service (for frontend and customer service)
   - Mapping Service (for distribution center mappings)
   - Order Scheduling Service (for scheduling and inventory interaction)
   - Order Routing Service (for routing based on business rules)

4. **Incremental migration** — We used the **Strangler Fig pattern**: route selected capabilities to the new platform based on the site they originate from, while keeping the legacy system running. Early interactions remained synchronous to reduce migration risk, but over time we moved more flows toward loosely coupled asynchronous and event-driven patterns.

**Result:** About 90% of the stack moved away from on-prem while significantly improving throughput and operational stability.

**Lesson learned:** Understanding the business need and outcome of the change is critical for developers. Migration isn't just a technical exercise — it's a business transformation.

---

## How I Think About Delivery

### Operational Excellence

A solution is only as good as its production behavior. I measure operational health across multiple dimensions:
- **Functional readiness**: core flows work as expected
- **Technical readiness**: integrations are stable, scalable, and secure
- **Operational readiness**: dashboards, alerts, support procedures, and escalation models are in place
- **Organizational readiness**: teams understand the handoff model and what success looks like in hypercare

### Design Philosophy
I prefer **separation by responsibility with orchestration above it**. A request should not be sent to the most powerful or most general system by default — it should be routed to the component or worker that is best suited to own it.

This applies to:
- **System architecture**: separate core business logic from integration layers, from customer-facing APIs
- **Integration architecture**: use middleware for mediation, not as the business logic layer
- **AI systems**: separate retrieval from reasoning, separate agents from orchestration

### What I Value
- **Measurable outcomes** over activity status
- **Visible risk tracking** over informal awareness
- **Process ownership** over hero-driven fixes
- **Observability as a feature**, not an afterthought
- **Standardization where possible, controlled variation where necessary**

---

## Tools & Technologies

**Systems:** Enterprise integration platforms, AS/RS systems, WMS, OMS, MHE integration, slotting optimization, labor standards

**Integration:** REST APIs, event-driven architecture (Kafka, SQS, SNS), SOAP/REST bridging, Saga pattern, middleware platforms

**Cloud:** AWS (EC2, RDS, Lambda, API Gateway, SQS/SNS), infrastructure-as-code, CI/CD

**Observability:** Dashboards, alerting, exception tracking, latency monitoring, queue depth visibility

**AI/ML:** Local RAG systems, AI agents, prompt engineering, vector databases (ChromaDB), chunking strategies, Ollama, Docker-based stacks

**Languages:** SQL, Python, JavaScript, Velocity templates, Shell scripting

---

## What I've Built

A small set of focused projects — full details on the [Projects page](/projects.html), but highlights:

- **[MAWM Environment Automation](https://github.com/sdontireddy/mawm-automate-environment-management)** — orchestrator for provisioning Manhattan Active WMS environments via sequential API execution with rollback on failure
- **[Supply Chain Tech Signals](https://supplychaintechsignals.com/)** — automated daily newsletter curating high-signal content from the supply chain / warehouse automation space
- **[Local RAG Knowledge Base](https://github.com/sdontireddy/rag-knowledge-base)** — Docker + Ollama + ChromaDB stack for private semantic search over markdown notes
- **[silverdreamracer.me](https://github.com/sdontireddy/silverdreamracer.me)** — this site; Pelican + GitHub Actions + S3, content-as-code publishing
- **[Raven](https://github.com/sdontireddy/raven)** — JMeter + Java loader for generating 100K+ middleware payloads from YAML-driven templates

---

## What I'm Working On Now

The pattern I'm experimenting with: **Hermes (AI orchestrator) + specialized agents for narrow, routable jobs**. One agent handles orchestration and deep tool workflows; others handle focused tasks like daily news reading, infrastructure operations, or local knowledge retrieval.

---

## Let's Connect

I write about enterprise architecture, AI agents, and integration patterns at [silverdreamracer.me](https://www.silverdreamracer.me).

If you're working on integration architecture, AS/RS systems, cloud migrations, or AI-powered enterprise tools, I'd like to hear from you. Pls feel to drop a note at sarath.dontireddy@outlook.com
