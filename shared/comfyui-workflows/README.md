# ComfyUI workflows

**Status:** not started. Built in **Weeks 9–12** on a cloud GPU (never on the Intel Mac).

Planned layout: `<project>/<workflow>.json` (API-format workflow) + `<workflow>.md` (purpose,
nodes, models with licences, custom-node review) and `client/` (Python ComfyUI API client, W12).

Rules: commit workflow JSON and metrics, **not** generated images (except small, deliberately
added contact sheets); record checkpoint hashes and seeds; review every custom node first.
