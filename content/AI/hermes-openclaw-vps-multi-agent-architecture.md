Title: Hermes and OpenClaw on a VPS: A Practical Multi-Agent Architecture
Date: 2026-07-10 12:31
Author: sdontireddy
Category: AI
Tags: AI, Hermes, OpenClaw, Multi-Agent, VPS, Telegram, Architecture
Slug: hermes-openclaw-vps-multi-agent-architecture
Status: published

Running more than one AI agent on a VPS does not have to mean building a large orchestration platform. A simpler pattern is to run separate agent runtimes, give each one a clear responsibility, and route requests to the right worker.

This post documents the current Hermes and OpenClaw arrangement on my VPS as a practical example. It focuses on the architecture, the role of each agent, Telegram routing, service boundaries, and the design decisions that keep the setup manageable.

## The high-level design

The VPS runs two independent agent platforms:

- **Hermes Agent** — a Python-based agent runtime with its own gateway, sessions, skills, memory, cron support, and Telegram connection.
- **OpenClaw** — a Node.js-based agent runtime with its own gateway, agent workspaces, skills, model configuration, and Telegram accounts.

They coexist on the same server rather than being collapsed into one process. This gives each platform an independent lifecycle and configuration boundary.

It is still too early to frame Hermes and OpenClaw as competing alternatives. They solve slightly different problems, and the goal of this setup is not to win that debate. The goal is to keep the **best of both worlds**: Hermes acts as the higher-level orchestrator, while OpenClaw handles selected tasks through its specialized agents and workflows.

The intended direction is cooperative rather than competitive:

```text
                         Internet / Telegram
                                  |
                                  v
                         Hermes orchestrator
                                  |
                 +----------------+----------------+
                 |                                 |
           Hermes-native work              Delegate selected tasks
                 |                                 |
                 v                                 v
       Hermes tools, skills,              OpenClaw gateway :18789
       memory, schedules                          |
                                                   v
                                      +------------+------------+
                                      |            |            |
                                     main      vps-admin      ogre / palki
                                  general work  VPS work     RAG / automation
```

In this model, Hermes does not need to replace OpenClaw, and OpenClaw does not need to replace Hermes. Hermes can interpret the user’s goal, decide which parts require OpenClaw, delegate those tasks, and combine the results into one response or workflow. The delegation boundary can remain explicit and narrow while the architecture matures.

The important idea is **separation by responsibility with orchestration above it**. A request should not be sent to the most powerful or most general agent by default. Hermes should route each task to the runtime or worker that is best suited to own it.

## The OpenClaw agent roster

OpenClaw currently defines four agent identities. Each identity has a separate purpose and, where needed, a separate workspace.

### `main`: general-purpose entry point

The `main` agent is the default general-purpose OpenClaw agent. It handles normal conversational requests and acts as the broad entry point when a more specialized route is not required.

Its workspace contains the general routing rules. Those rules intentionally keep the default agent lightweight and direct specialized work elsewhere.

### `vps-admin`: infrastructure operations

The `vps-admin` agent owns server administration tasks such as:

- VPS health checks
- CPU, memory, disk, and process checks
- OpenClaw cleanup
- Stuck-session troubleshooting
- Service and log investigation

This is a valuable boundary. Infrastructure work can require privileged commands or service changes, so it is better isolated from a general chat agent.

```text
User: "Check why the VPS is running out of disk"
                 |
                 v
              vps-admin
                 |
       inspect -> diagnose -> report
```

The current workspace instructions also require this agent to identify itself with a `[VPS-ADMIN]` prefix and restrict its normal tool usage to command execution for administration work.

### `ogre`: local RAG and private knowledge

The `ogre` agent owns questions that should be answered from the local knowledge base rather than from general model knowledge or public web search.

Its documented path is:

```text
OpenClaw request
      |
      v
 ogre agent
      |
      v
HTTP POST http://localhost:8090/ask
      |
      v
Local RAG application / indexed documents
```

This agent is intentionally constrained to the local RAG API. That reduces the chance of accidentally mixing private project information with unrelated web results.

Typical requests include questions about:

- uploaded documents
- private notes
- project notes
- indexed repository content
- ChromaDB or Ollama RAG knowledge

### `palki`: daily news reader

`palki` is OpenClaw's daily news reader agent — a quiet tribute to my favourite news anchor, **Palki Sharma**. Her IDENTITY.md describes the vibe she is meant to carry: *professional, eloquent, crisp, polished* — like the anchor herself, but focused on the feeds that matter.

She runs a dedicated workspace with her own `SOUL.md`, `AGENTS.md`, and the `/gold` command that triggers a gold-price and USD/INR summary. The narrow scope is the point: instead of bolting news-reading onto `main`, Palki has her own surface and her own routines.

This is an example of a narrow operational agent — a dedicated identity that owns a repeatable daily workflow rather than every agent juggling every capability.

## How Telegram routing works

Telegram is the front door for both platforms, but routing is explicit.

The OpenClaw configuration defines bindings for:

| Telegram route | Destination | Purpose |
|---|---|---|
| Direct chat binding for the primary user | `vps-admin` | Direct VPS administration path |
| `ogre-bot` account | `ogre` | Local RAG and private knowledge questions |
| `palki-bot` account | `palki` | Focused automation workflows |
| Other Telegram traffic | `main` | General OpenClaw conversations |

The conceptual flow is:

```text
Telegram message
       |
       v
OpenClaw binding matcher
       |
       +--> Direct admin binding ------> vps-admin
       |
       +--> ogre-bot account ----------> ogre ------> localhost:8090 RAG
       |
       +--> palki-bot account ---------> palki
       |
       +--> Default Telegram route ----> main
```

This is not just a convenience feature. It is an access-control and reliability pattern. The route determines the workspace, instructions, model defaults, and available tools before the agent starts working.

## Hermes as a separate agent surface — Sam

Hermes runs under a named profile called **Sam**. `sam` is the main Hermes agent and lives under its own profile directory (`~/.hermes/profiles/sam/`), with its own skills, memory, sessions, and SOUL.md. The name is small but meaningful — Sam has his own identity, not just a generic "Hermes instance."

Sam's surface on the VPS includes:

- An active Hermes gateway process, with Telegram as the home messaging platform
- A custom OpenAI-compatible endpoint backed by OpenRouter
- Persistent sessions, memory, and scheduled-job (cron) support
- Local terminal execution as the terminal backend
- Delegation to both short-lived child agents and longer-lived workers

Sam also has a set of **custom skills authored for his own workflows** — these sit alongside the plugin-provided skills but reflect the problems he is actually solving day-to-day:

| Custom skill | Purpose |
|---|---|
| `silver-dream-racer-blog-agent` | Publish and refine blog drafts for the Silver Dream Racer site |
| `supply-chain-newsletter` | Build the daily 8 AM ET newsletter from RSS/feeds |
| `job-market-watch` | On-demand shortlist of supply-chain / WMS roles |
| `teams-meeting-pipeline` | Summarize Teams meetings via the pipeline CLI |
| `idea-factory` | Triage and rank ideas from raw notes into `Ideas.md` |
| `ingest-chatgptto-hermes-wiki` | Ingest new files into the hermes-wiki knowledge base |

A simplified view of the runtime is:

```text
Telegram / CLI / other Hermes surface
                 |
                 v
          Hermes gateway  (profile: sam)
                 |
          Hermes agent loop
          /      |       \
     tools    skills    memory
                 |
        optional delegation to Hermes workers
                 |
                 +------ selected OpenClaw tasks
```

The distinction that matters:

- **OpenClaw named agents** (`main`, `vps-admin`, `ogre`, `palki`) are long-lived identities configured in OpenClaw, with their own workspaces and routing rules.
- **Sam (Hermes)** is the top-level orchestrator, with delegation into both Hermes subtasks and selected OpenClaw agents.

Both are multi-agent patterns. Hermes handles orchestration and deep tool workflows; OpenClaw handles narrow, routable jobs.

## Current integration boundary: orchestration without premature consolidation

Both Hermes (running as profile **sam**) and OpenClaw are active on the VPS. There is no single shared session store between them — and that is not a problem. It leaves room to establish a deliberate orchestration path without prematurely merging the two runtimes. OpenClaw's gateway listens on port `18789`, bound to loopback, so access is expected to come through the local host or a controlled reverse proxy rather than straight off the public internet.

The practical architecture is therefore:

```text
                 +-------------------+
                 |       Telegram    |
                 +---------+---------+
                           |
                     +-----v-----+
                     |  Hermes   |
                     |orchestrator|
                     +--+-----+--+
                        |     |
             Hermes-native    | delegate selected work
             tools and state  |
                              v
                       +------+------+
                       |  OpenClaw  |
                       |   gateway  |
                       +------+------+
                              |
                   OpenClaw agents and workspaces
```

This loose coupling is often a strength. One runtime can be restarted, upgraded, or investigated without requiring the other runtime to stop. The trade-off is that cross-platform coordination must be explicit—for example, through a webhook, a local API, a shared queue, a file contract, or a deliberately invoked CLI command. Hermes can own that coordination logic while OpenClaw remains free to specialize in the tasks it handles well.

## Why specialized agents are useful

A single agent with every tool and every instruction can become expensive and difficult to control. Specialization provides several practical benefits.

### Smaller context

An agent that only performs VPS checks does not need the complete RAG workflow, browser automation instructions, or content-generation tools. Smaller instructions and fewer tool schemas generally make the agent easier to reason about.

### Safer permissions

The `ogre` agent is restricted to a local RAG API for knowledge-base questions. The `vps-admin` agent is the designated path for server operations. This reduces accidental tool use in the wrong context.

### Clear ownership

When an agent has one job, its workspace instructions can be more precise:

| Agent | Owns | Should not own by default |
|---|---|---|
| `main` | General OpenClaw conversations | Privileged administration and private RAG retrieval |
| `vps-admin` | VPS operations and diagnostics (uses the `vps-cleanup` skill) | General knowledge-base answers |
| `ogre` | Local RAG and private project knowledge (RAG API only) | Public-web research as a substitute for local retrieval |
| `palki` | Daily news reading and `/gold` routines | Broad infrastructure administration |
| `sam` (Hermes) | Orchestration, custom skills, memory, and automation | Blindly duplicating OpenClaw's specialized workflows |

### Easier troubleshooting

If a request fails, the routing path gives an immediate starting point:

1. Did Telegram deliver the message?
2. Did the binding select the expected agent?
3. Is the target gateway healthy?
4. Is the target workspace instruction file correct?
5. Is the required local service, such as the RAG API, available?

## Operational practices for this design

A small multi-agent VPS benefits from a few explicit rules:

1. **Keep gateway ports private.** Bind administrative gateways to loopback where possible and use authenticated access.
2. **Keep secrets out of documentation.** Record service names, ports, routes, and responsibilities—not bot tokens or gateway credentials.
3. **Give every agent one clear owner.** Avoid overlapping instructions that make two agents believe they are responsible for the same operation.
4. **Keep workspaces separate.** Separate workspaces make it easier to audit instructions and prevent accidental context leakage.
5. **Route private knowledge deliberately.** Use the RAG agent for local documents instead of sending private questions to public web search.
6. **Inspect before changing.** Check service status, configuration, bindings, and logs before restarting or editing a gateway.
7. **Use health checks for each runtime.** Hermes and OpenClaw can be healthy independently, so monitor them independently.

## The main design lesson

The most important part of a multi-agent system is not the number of agents. It is the clarity of the boundaries between them.

In this VPS setup:

- **Sam (Hermes)** provides the orchestration layer and his own extensible agent runtime, with custom skills built for real workflows (`silver-dream-racer-blog-agent`, `supply-chain-newsletter`, `job-market-watch`, `teams-meeting-pipeline`, `idea-factory`, `ingest-chatgptto-hermes-wiki`).
- OpenClaw provides specialized capabilities through an independent runtime with named agents and Telegram routing.
- `main` handles general conversations.
- `vps-admin` owns infrastructure operations, powered by the `vps-cleanup` skill.
- `ogre` owns local RAG retrieval.
- `palki` is the daily news reader — a tribute to Palki Sharma — and runs the `/gold` routine.
- Telegram bindings decide where a request goes before the work begins.

That is enough to create a useful multi-agent architecture without forcing an early platform choice. Start with **Sam** as the orchestrator, keep responsibilities and permissions narrow, make both runtimes observable, and delegate only the work that benefits from OpenClaw. Let the integration grow from real workflows rather than from an abstract debate about which platform should replace the other.

## Final diagram

```text
                             USER
                              |
                         Telegram / CLI
                              |
              +---------------+----------------+
              |                                |
       Sam (Hermes orchestrator)        Delegate selected work
              |                                |
      tools / skills / memory                  v
              |                         OpenClaw gateway
              |                    +-------------+-------------+
              |                    |             |             |
              |                   main       vps-admin        ogre
              |                    |             |             |
              |              general work   VPS checks    localhost:8090
              |              (skills/       (vps-cleanup    Local RAG
              |               memory)         skill)
              |

                         +------------------+
                         |      palki       |
                         |  daily news /    |
                         |  /gold routines  |
                         +------------------+
```

The result is a practical pattern: **one VPS, Sam as the orchestrator with custom skills built from real workflows, OpenClaw as a specialized delegated runtime, and focused workers — Palki the news reader, Ogre the librarian, vps-admin the operator — that keep each job in the right place.**

---

*Architecture details in this post are intentionally summarized from the live configuration. Production deployments should review authentication, filesystem permissions, firewall rules, Telegram pairing policies, and secret rotation separately.*

## Further reading

- [How to Connect Hermes to a Local Browser from a VPS with an SSH Reverse Tunnel](hermes-remote-browser.md)
- [How I Reduced OpenClaw Token Usage by Tightening Instructions](open-claw-reduce-token-usage.md)
- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [OpenClaw](https://openclaw.ai/)

---

**Diagram legend:** arrows show request flow; separate boxes show independent runtime or workspace boundaries; `localhost` indicates a service intended to remain on the VPS.

---

**SEO summary:** A practical guide to the current Hermes and OpenClaw multi-agent architecture on a VPS, including Telegram routing, specialized agents, local RAG, gateway boundaries, and simple diagrams.

**Suggested social excerpt:** One VPS, four named OpenClaw agents, and Hermes running as Sam. Here is how `vps-admin`, `ogre`, `palki` (my tribute to Pakli Sharma), and `main` fit together — with custom skills on each side doing the actual work.
