# Week 19 — Assignment (3 hours): Project-scoped MCP servers

**Linked projects:** [Billionslight](../../../projects/billionslight/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md)

## Brief
Build two MCP servers in `shared/mcp-servers/`: a Billionslight product-knowledge server (search, spec lookup, citation) and a Phonics Pond curriculum server (read-only access to curriculum JSON and the decodability checker). Each server can see only its own project's data.

## Deliverables
- Two servers with README, tests and Inspector screenshots
- Security review of each tool (inputs, outputs, side effects)

## Acceptance criteria
- [ ] Servers are read-only by default; any write tool needs explicit confirmation
- [ ] Input schemas validated; errors return structured messages
- [ ] Cross-project data access impossible (test)
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Tool-call success rate from a client
- Latency per tool call
- Test coverage

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- stdio server prints logs to stdout and breaks the protocol: log to stderr.
- Client does not see tools: check capability negotiation and server start command.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
