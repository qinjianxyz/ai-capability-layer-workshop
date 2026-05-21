# Technical Reference

## Tokens

Tokens are the text units processed by models. Token budgets shape cost, speed, context length, and how much evidence can be inspected. Larger context windows help, but they do not replace retrieval, metadata, source policy, or review.

## Models

Choose models by job. Use stronger models for ambiguous design, research synthesis, stakeholder nuance, and complex coding. Use faster or local models for extraction, classification, template filling, and private experiments when quality is sufficient.

## Context Engineering

Context engineering defines what the model is allowed to know for a task. It includes source policy, retrieval plan, examples, output schema, data boundary, and refresh rules.

## GBrain And Database-Backed Memory

A memory layer needs a database because useful memory requires persistence, search, metadata, links, versions, and health checks. GBrain-style memory imports documents, chunks them, embeds chunks, stores metadata, supports keyword and vector search, tracks links and timelines, and retrieves context packets for workflows.

Postgres paths can use full-text search with `tsvector`, `GIN`, `ts_rank`, and `websearch_to_tsquery`, plus vector search with `pgvector` and HNSW indexes. PGLite gives a local embedded Postgres path for lower setup.

## Vector Embeddings

An embedding turns a chunk of text into a numeric vector representing semantic meaning. A query can be embedded and compared against stored chunk vectors to find semantically similar material. Embeddings help retrieval, but they do not prove truth. Retrieved chunks still need source labels and review.

## Skill Graph

A skill graph maps reusable procedures and their artifacts. Nodes are skills such as research, spec writing, context pack creation, artifact generation, governance review, and handoff. Edges define what each skill requires, produces, verifies, escalates, or teaches.

## Harness Engineering

A harness is the operating wrapper around AI work: objective, state, tools, permissions, logs, checks, receipts, review gates, and recovery. Harnesses make AI work inspectable and governable.

## Deep Research

Deep research should change the workflow spec, source policy, context pack, evaluation rubric, or pilot plan. Convert research into source maps, context files, prompts, governance rules, and artifact checks.
