Title: Projects
Author: sdontireddy
Slug: projects
Status: published
Save_as: projects.html

# Projects

Open source work and reference implementations I've built. Each project tackles a specific problem I've run into in production or research contexts.

---

<div class="project-grid">

<div class="project-card card-supply-chain">
  <h3><a href="https://github.com/sdontireddy/mawm-automate-environment-management" target="_blank" rel="noopener">MAWM Environment Automation</a></h3>
  <p class="project-tag">Enterprise Automation · Python · REST APIs</p>
  <p>Python-based orchestration tool for creating and managing Manhattan Active WMS environments through sequential API execution. Handles multi-environment provisioning (DEV / QA / Stage) via header-based routing, dependency-aware API chaining, clone-from-golden workflows, OAuth 2.0 token management, and rollback on failure.</p>
  <p class="project-meta">Pattern: <strong>orchestrated sequential execution with rollback</strong> — same shape applies to any enterprise admin API stack that lacks native workflow support.</p>
</div>

<div class="project-card card-testing">
  <h3><a href="https://github.com/sdontireddy/raven" target="_blank" rel="noopener">Raven</a></h3>
  <p class="project-tag">Load Testing · Java · JMeter · Middleware</p>
  <p>JMeter + Java utility for generating bulk XML payloads (100K+ orders, ASNs, POs, invoices) for middleware load testing. YAML-driven configuration + XML template — generate thousands of varied variants for stress testing Mule / ESB systems without hand-crafting each file.</p>
  <p class="project-meta">Solves: <strong>"I need 50K distribution orders with different field combinations to stress-test my Mule app"</strong> — a recurring problem in integration-heavy projects.</p>
</div>

<div class="project-card card-ai">
  <h3><a href="https://supplychaintechsignals.com/" target="_blank" rel="noopener">Supply Chain Tech Signals</a></h3>
  <p class="project-tag">Content Pipeline · RSS · Cloudflare Pages</p>
  <p>Automated daily newsletter curating warehouse, automation, fulfillment, visibility, transportation, and AI insights from RSS feeds, podcasts, and vendor content. Weighted editorial scoring selects the highest-signal items each day.</p>
  <p class="project-meta">Live: <a href="https://supplychaintechsignals.com/" target="_blank">supplychaintechsignals.com</a> · GitHub: <a href="https://github.com/sdontireddy/supplychaintechsignals.com" target="_blank">supplychaintechsignals.com</a></p>
</div>

<div class="project-card card-ai">
  <h3><a href="https://github.com/sdontireddy/rag-knowledge-base" target="_blank" rel="noopener">Local RAG Knowledge Base</a></h3>
  <p class="project-tag">RAG · Ollama · ChromaDB · FastAPI</p>
  <p>Docker-based local RAG stack for indexing markdown notes and searching them semantically. Demonstrates the full flow: ingestion, embeddings, vector search, retrieval, grounded answer generation, and citations — without relying on cloud APIs.</p>
  <p class="project-meta">Stack: Docker · Ollama · ChromaDB · FastAPI · Streamlit</p>
</div>

<div class="project-card card-devops">
  <h3><a href="https://github.com/sdontireddy/silverdreamracer.me" target="_blank" rel="noopener">silverdreamracer.me</a></h3>
  <p class="project-tag">Static Site · Pelican · GitHub Actions · S3</p>
  <p>This site. Pelican-based static blog where Markdown is the source of truth. Automated build + deploy to AWS S3 via GitHub Actions, Route 53 DNS, CloudFront-ready architecture. Operationally lightweight and cost-effective.</p>
  <p class="project-meta">Pattern: <strong>content-as-code</strong> — version-controlled, PR-driven publishing.</p>
</div>

</div>

---

## What I'm Working On Now

- Integrating AI agents into VPS-orchestrated workflows (Hermes + OpenClaw multi-agent architecture)
- Expanding <strong>Supply Chain Tech Signals</strong> with podcast ingestion and vendor insight feeds
- Building local-first RAG patterns that work without cloud APIs for every query
- Automating WMS environment management across multiple tenants and stages

---

Have a question or want to collaborate? [Get in touch](/aboutme.html#lets-connect).
