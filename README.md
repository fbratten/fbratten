# Fredrik Brattén

**AI Engineer building retrieval systems, agent orchestration, user-facing AI products and reliable execution infrastructure.**

I combine applied AI with more than 20 years in enterprise IT, automation, operations and cybersecurity. My work focuses on systems that are useful in practice: searchable knowledge, controlled agent actions, product-facing AI workflows, auditability and operational safeguards.

<p align="center">
  <a href="https://fbratten.github.io/intelligence-engine-showcase/"><img src="https://img.shields.io/badge/Intelligence_Engine-Retrieval_%26_Graphs-00bfa5?style=for-the-badge" alt="Intelligence Engine"/></a>
  <a href="https://fbratten.github.io/mads/"><img src="https://img.shields.io/badge/MADS-Human--in--the--Loop-7c6cff?style=for-the-badge" alt="MADS"/></a>
  <a href="https://fbratten.github.io/adaptivearts-ai/"><img src="https://img.shields.io/badge/Adaptivearts.ai-AI_Product-2563eb?style=for-the-badge" alt="Adaptivearts.ai"/></a>
  <a href="https://fbratten.github.io/gate-monitor/"><img src="https://img.shields.io/badge/Gate_Monitor-Runtime_Governance-f59e0b?style=for-the-badge" alt="Gate Monitor"/></a>
</p>

---

## Four current proof-of-work flagships

These four projects provide complementary evidence across retrieval, product engineering, agent interaction and runtime reliability.

| Project | Problem solved | Implementation evidence | Public proof |
|---|---|---|---|
| **Intelligence Engine** | Makes structured source material searchable through lexical, semantic and graph retrieval rather than one search method alone | Python, FastAPI, React, TypeScript, Sigma.js, KuzuDB, LanceDB, BM25, schema-driven domains, REST and MCP | [Explore the showcase](https://fbratten.github.io/intelligence-engine-showcase/) |
| **MADS — Multi-Agent Developer Sandbox** | Lets AI agents propose code and commands without giving them uncontrolled host access | Electron, React, TypeScript, Zod, policy-gated execution, reviewable ChangeSets, durable audit, 125 Vitest tests and 13 Electron E2E scenarios at the pinned implementation receipt | [Try the synthetic proof package](https://fbratten.github.io/mads/) |
| **Adaptivearts.ai** | Turns research, editorial work and AI experiments into a deployed user-facing product | Astro, React, TypeScript, Supabase Auth and role handling, editorial workflows and an authenticated server-side Gemini provider boundary | [Read the architecture case study](https://fbratten.github.io/adaptivearts-ai/) · [Visit the product](https://adaptivearts.ai/) |
| **Gate Monitor** | Governs long-running AI-agent sessions using deterministic policy rather than relying on the agent to self-report that everything is fine | Python, Typer, Pydantic, JSONL evidence, cost/time/progress/error thresholds, quality and memory findings, reports and MCP; source history records 279 passing tests plus three dogfood scripts | [Use the synthetic decision demonstrator](https://fbratten.github.io/gate-monitor/) |

### What the four cases demonstrate together

```text
source material and operational signals
-> structured ingestion and typed contracts
-> retrieval, policy or decision logic
-> user-facing React / web / desktop surfaces
-> explicit approval, evidence and audit boundaries
-> reproducible verification receipts
```

- **Applied AI:** hybrid retrieval, provider integrations, agent workflows and AI-assisted product features.
- **Modern application engineering:** Python/FastAPI, React/TypeScript, Astro, Electron and Supabase.
- **Reliable execution:** policy gates, reversible changes, deterministic decisions and durable evidence.
- **Security-aware design:** credentials kept out of browser or renderer surfaces, path confinement, workspace boundaries and explicit non-claims.

The detailed source pins, verification limits and publication status are recorded in [`docs/recruiter-proof-evidence-2026-08-02.md`](docs/recruiter-proof-evidence-2026-08-02.md).

---

## Supporting systems

### Adaptive MCP Orchestrator Blueprint

A multi-provider task-routing and orchestration system combining provider selection, fallback, learning, LanceDB, Neo4j, FastAPI and observability.

> [Explore the public showcase](https://fbratten.github.io/Adaptive-MCP-Orchestrator-Blueprint-Showcase/)

### Broker Lane Sandbox

A public, default-deny execution boundary for agent workflows with policy validation, environment scrubbing, resource limits, output caps and local-model support.

It is a bounded process-execution layer, not a kernel or container isolation boundary.

> [View the public source repository](https://github.com/fbratten/broker-lane-sandbox)

### SPINE

A broader context-engineering and orchestration backbone covering compiled plans, execution transports, memory, routing, observability and multi-agent coordination.

> [Explore the SPINE showcase](https://fbratten.github.io/spine-showcase/)

---

## Public MCP product family

A set of smaller public products demonstrates narrow, explainable MCP capabilities:

| Project | Purpose | Public surface |
|---|---|---|
| **switchcore** | Discovers MCP tools and recommends bounded workflows | [Showcase](https://fbratten.github.io/switchcore-showcase/) |
| **vigil** | Schedules durable follow-up checks with retry and expiry | [Showcase](https://fbratten.github.io/vigil-showcase/) |
| **spawn** | Turns recurring agent patterns into generated MCP projects | [Showcase](https://fbratten.github.io/spawn-showcase/) |
| **arbiter** | Validates MCP protocol behavior, quality and remediation paths | [Showcase](https://fbratten.github.io/arbiter-showcase/) |
| **agentspool** | Provides inter-agent messaging and delivery semantics | [Showcase](https://fbratten.github.io/agentspool-showcase/) |

---

## Additional showcases and applied work

| Showcase | Focus |
|---|---|
| [8me Learning Platform](https://fbratten.github.io/8me-showcase/) | Progressive loop-orchestration labs |
| [Security Audit MCP](https://fbratten.github.io/Security-Audit-MCP-Server-Showcase/) | Security scanning and isolated analysis patterns |
| [Music Video Creator](https://fbratten.github.io/music-video-creator-showcase/) | Audio analysis, beat-aware rendering and multimodal output |
| [From Blueprint to Application](https://fbratten.github.io/From-Blueprint-to-Application/) | Book and interactive demonstrations covering structured AI delivery |

### Applied AI-assisted local newsroom prototype

A controlled audio-first pipeline for a local morning brief in Västra Götaland:

```text
approved public sources
-> collection and deduplication
-> ranking and rundown
-> Swedish script generation
-> editorial QA
-> voice and script-anchored captions
-> human review
```

The prototype is AI-assisted and human-reviewed. It is not presented as an autonomous newsroom or as permission to reproduce copyrighted source articles.

---

## How I approach AI engineering

I prefer systems where claims can be inspected:

- source and implementation commits are pinned;
- tests and runtime receipts are distinguished from documentation claims;
- private data is replaced by synthetic fixtures in public demonstrations;
- limitations and non-claims sit beside strengths;
- risky actions pass through explicit policy or human approval;
- preserve-first change practices keep earlier evidence available.

This is also why many of the public proof packages are explanatory or synthetic. They demonstrate the product and control model without publishing credentials, prompts, private patches, operational logs or customer-like data.

---

## Adaptivearts.ai

[Adaptivearts.ai](https://adaptivearts.ai/) is my independent applied-AI initiative for research, prototypes, technical writing and product experiments.

- [Research and prototypes](https://adaptivearts.ai/#prototypes)
- [Articles and research](https://adaptivearts.ai/blog)
- [MCP directory](https://adaptivearts.ai/mcp)
- [Context engineering](https://adaptivearts.ai/context-engineering)
- [AI-agent architecture](https://adaptivearts.ai/ai-agent-architecture)

---

## Background

More than 20 years across enterprise IT operations, systems engineering, automation, cybersecurity and DevOps, including SOC/XDR work, identity and endpoint environments, monitoring, incident-oriented operations and business-facing technical delivery.

My current focus is the intersection of:

- applied AI and AI enablement;
- automation and integration;
- retrieval and knowledge systems;
- agentic workflows;
- security, governance and observability;
- translating technical capability into practical business value.

## Personal side quest: music

Occasionally the human also emits audio.

🎧 [Spotify artist profile](https://open.spotify.com/artist/0c5DZx6gt2uBkDkkChERGC)

---

The previous, broader profile README is preserved at [`archived/README.pre-canonical-recruiter-landing-2026-08-02.md`](archived/README.pre-canonical-recruiter-landing-2026-08-02.md).

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=fbratten&label=Profile%20Views&color=6366F1" alt="Profile Views" />
</p>

<p align="center">
  <sub>Applied AI · Automation · Reliable agent systems · <a href="https://adaptivearts.ai">Adaptivearts.ai</a></sub>
</p>
