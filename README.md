
**I build the infrastructure that makes AI agents remember, coordinate, and improve.**

<p align="center">
  <a href="https://fbratten.github.io/spine-showcase/"><img src="https://img.shields.io/badge/SPINE-Showcase-6366F1?style=for-the-badge" alt="SPINE"/></a>
  <a href="https://fbratten.github.io/8me-showcase/"><img src="https://img.shields.io/badge/8me-Labs-blue?style=for-the-badge" alt="8me"/></a>
  <a href="https://fbratten.github.io/intelligence-engine-showcase/"><img src="https://img.shields.io/badge/IE-Knowledge_Graphs-00ccaa?style=for-the-badge" alt="Intelligence Engine"/></a>
  <a href="https://fbratten.github.io/From-Blueprint-to-Application/"><img src="https://img.shields.io/badge/Book-From_Blueprint_to_Application-orange?style=for-the-badge" alt="Book"/></a>
  <a href="https://adaptivearts.ai/#prototypes"><img src="https://img.shields.io/badge/Adaptivearts.ai-Prototypes-blueviolet?style=for-the-badge" alt="Prototypes"/></a>
</p>

---

## The Problem

Most AI agent systems are talented amnesiacs. Brilliant in the moment, blank by the next session. They can't remember what they learned, can't build on what came before, and can't coordinate without a human holding the threads.

I build the systems that fix this.

## What I Build

### SPINE - Context Engineering Backbone

The central nervous system connecting 270+ projects. Seven tiers of memory, seven pluggable executors, OODA composition, and a grammar inspired by the Rig Veda for temporal knowledge annotation.

| Layer | What | How |
|-------|------|-----|
| Memory | 7-tier system (KV -> Scratchpad -> Vector -> Ephemeral -> Episodic -> Deep/pgvector -> Graph) | Each tier serves a different temporal need |
| Orchestration | OODA loop + AgenticLoop + Dynamic Routing | Agents that observe, orient, decide, act, and reflect |
| Execution | 7 pluggable executors | Subagent, MCP Orchestrator, Content Pipeline, Small LLM, Task Router + 2 API executors |
| Governance | Tiered enforcement + Five-Point Protocol + warrant gate | Not everything deserves to be remembered |
| Knowledge | EBNF grammar (Rig Veda temporal markers) + DIALECTIC engine | Thesis -> antithesis -> synthesis with convergence tracking |

The pipeline that edited my book - 74,000 words, five iterations, score 5.6 -> 9.5 - ran on this.

> [Explore SPINE - 11+ interactive demos](https://fbratten.github.io/spine-showcase/)

### Intelligence Engine - Code Knowledge Graphs

AST-driven knowledge graphs over codebases. KuzuDB + hybrid search (BM25 + semantic + graph expansion). 53,000+ entities indexed across 272 projects. 15 MCP tools, 33 REST endpoints, 1,261+ tests.

> [Explore Intelligence Engine - search, Cypher console, dashboards](https://fbratten.github.io/intelligence-engine-showcase/)

### MCP Ecosystem - 30+ Servers

Purpose-built Model Context Protocol servers for AI agent workflows.

| Category | Count | Examples |
|----------|-------|---------|
| Orchestration | 4 | SPINE executor adapters, gen-loop scheduler, 8do Ralph Loop |
| Agent Coordination | 4 | agentspool messaging, agent-comm relay, session handover |
| Knowledge & Memory | 5 | Minna (SQLite+FTS5), mem-system (pgvector), context-glue, observation-workbench |
| Research | 3 | research-agent, research-notes, research-log |
| Content & Creative | 4 | content-mcp (41 tools), the-musicologist, content-analyzer, content-extractor |
| Infrastructure | 5 | mcp-server-checker, security-audit, smart-inventory, backup, manual-generator |
| Evaluation | 2 | Evalla (rubric scoring), evaluation-mcp |
| Browser & Visual | 3 | browser-mcp (CDP + grid overlay), tachylite (canvas editor), showcase-mcp |

**3 cloud MCP servers live** at [adaptivearts.ai/mcp](https://adaptivearts.ai/mcp) - Evalla, Minna Memory, Agent Comm (Bearer auth, rate limiting, audit trail).

### Creative Pipelines

Music Video Creator (19 visual styles, beat-sync, genre presets), flow-musical-creation (12-song AI musical), the-musicologist-mcp (style descriptions, Suno/Udio formatting).

> [Explore Music Video Creator - 6 interactive demos](https://fbratten.github.io/music-video-creator-showcase/)

---

## Live Showcases & Demos

All self-contained, no API keys needed.

| Showcase | What | Demos |
|----------|------|-------|
| [SPINE Framework](https://fbratten.github.io/spine-showcase/) | Multi-agent orchestration, 7-tier memory, OODA loops | 11+ interactive demos |
| [Intelligence Engine](https://fbratten.github.io/intelligence-engine-showcase/) | Code knowledge graphs, hybrid search | Search Picker, Cypher Console |
| [arbiter](https://fbratten.github.io/arbiter-showcase/) | MCP Server Validator - protocol compliance, quality, LLM ergonomics | Profile Simulator |
| [8me Learning Platform](https://fbratten.github.io/8me-showcase/) | Loop orchestration curriculum | 15 progressive labs |
| [agentspool](https://fbratten.github.io/agentspool-showcase/) | Inter-agent messaging | Network Graph, Message Flow, Radar |
| [Adaptive MCP Orchestrator](https://fbratten.github.io/Adaptive-MCP-Orchestrator-Blueprint-Showcase/) | Cognitive task dispatcher | Architecture demos |
| [Security Audit MCP](https://fbratten.github.io/Security-Audit-MCP-Server-Showcase/) | 5 security scanners, Docker-isolated | Stack Detector, Secret Scanner |
| [Music Video Creator](https://fbratten.github.io/music-video-creator-showcase/) | 19 visual styles, audio analysis | Style Showcase, Beat Effects |
| [switchcore](https://fbratten.github.io/switchcore-showcase/) | MCP Meta-Router, smart tool routing | Tool cards, architecture |
| [vigil](https://fbratten.github.io/vigil-showcase/) | Self-scheduling follow-up server | Tools, check types, notifications |

---

## The Book: From Blueprint to Application

**By Fredrik Bratten & Sasa Popovic**

A 90-day journey from first prompt to production AI systems. 12 chapters across 6 parts. Processed by the SPINE pipeline with AI editorial personas - the same infrastructure described above edited the book that describes it.

**9 interactive demos included:**

| Demo | What it teaches |
|------|-----------------|
| [Prompt Builder](https://fbratten.github.io/From-Blueprint-to-Application/demos/prompt-builder/) | Structured prompt construction |
| [Model Selector](https://fbratten.github.io/From-Blueprint-to-Application/demos/model-selector/) | Choosing the right model for the task |
| [Token Calculator](https://fbratten.github.io/From-Blueprint-to-Application/demos/token-calculator/) | Understanding token economics |
| [Enterprise Flow](https://fbratten.github.io/From-Blueprint-to-Application/demos/enterprise-flow/) | Enterprise AI workflow patterns |
| [Injection Detection](https://fbratten.github.io/From-Blueprint-to-Application/demos/injection-detection/) | Prompt injection defense |
| [Few-Shot Builder](https://fbratten.github.io/From-Blueprint-to-Application/demos/few-shot-builder/) | Few-shot learning patterns |
| [MCP Server Setup](https://fbratten.github.io/From-Blueprint-to-Application/demos/mcp-server-setup/) | Building your first MCP server |
| [Five-Point Protocol](https://fbratten.github.io/From-Blueprint-to-Application/demos/five-point-protocol/) | Structured execution framework |
| [Security Assessment](https://fbratten.github.io/From-Blueprint-to-Application/demos/security-assessment-agent/) | AI security evaluation |

> [Browse the book site](https://fbratten.github.io/From-Blueprint-to-Application/)

---

## Adaptivearts.ai

Independent AI research initiative exploring agentic systems, context engineering, and creative AI pipelines.

- [Research & Prototypes](https://adaptivearts.ai/#prototypes) - 3 prototype domains with 55+ backing projects
- [MCP Server Directory](https://adaptivearts.ai/mcp) - 5 servers, 49 tools (3 live cloud endpoints)
- [Articles & Research](https://adaptivearts.ai/blog) - Technical writing on AI architecture, MCP, security
- [Context Engineering](https://adaptivearts.ai/context-engineering) - Pillar page on context stacks, memory systems, patterns
- [AI Agent Architecture](https://adaptivearts.ai/ai-agent-architecture) - 6-layer architecture reference

---

## Background

20+ years in IT operations, systems architecture, cybersecurity, and DevOps. SOC analysis, XDR implementation, high-availability systems for regulated environments (gaming, finance). Founder of [Adaptivearts.ai](https://adaptivearts.ai).


<p align="center">
  <img src="https://komarev.com/ghpvc/?username=fbratten&label=Profile%20Views&color=6366F1" alt="Profile Views" />
</p>

<p align="center">
  <sub>Built with SPINE · <a href="https://adaptivearts.ai">Adaptivearts.ai</a></sub>
</p>
