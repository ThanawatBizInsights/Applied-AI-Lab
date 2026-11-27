# Little Snowy Owl Studio — Animal Pairs — Project context

Status tags: **[VERIFIED]** read from the repository · **[USER-PROVIDED]** from the learner's
brief · **[PROPOSED]** learning work, not an existing feature · **[NEEDS CONFIRMATION]**.
Verified on 2026-11-27 by read-only inspection. No changes were made to any project repository.

## Repositories
| Repository | Visibility | Commit inspected | Last commit date |
|---|---|---|---|
| `ThanawatBizInsights/AnimalPairs` | public | `1e6848c` | 2026-11-24 |
| `ThanawatBizInsights/LittleSnowyOwlStudio` | public | `763580c` | 2026-11-19 |

## [VERIFIED] What the repository shows
- A gentle animal memory-matching game for iPad for children of about 3–7, with ten animal characters. No timers, lives, failure screens, ads or accounts; works fully offline.
- Classic and Exact Pose modes; board sizes 6–20 cards; optional one-time purchase **Full Game Unlock** with a local StoreKit configuration for testing.
- Requirements stated in the README: Xcode 16+, iPadOS 17+ SDK, Swift 5 language mode. A Swift package (`Packages/AnimalPairsKit`) holds core logic tests (the README lists 93 core tests).
- `Tools/audio/` contains ElevenLabs music and SFX generation scripts. `ci_scripts/` exists.
- Studio website repo: a Next.js static site served by a Cloudflare Worker, with no analytics, cookies, trackers or accounts. Mascot: Snowy, a snowy owl.

## [USER-PROVIDED] Focus and constraints
- Focus: SwiftUI development; automated code review and testing; consistent game character generation; transparent game-ready assets; App Store release automation; in-app purchase testing; AI-assisted QA.

## [PROPOSED] Role in this curriculum
- W1: parent-facing description generator with child-safety rules
- W11: character LoRA trial for an Animal Pairs friend
- W18: AI code-review agent on historical diffs (read-only)

## [NEEDS CONFIRMATION]
- Purpose of the `backend/` directory in the AnimalPairs repo.
- Whether App Store release automation (fastlane, Xcode Cloud) is wanted, or only checklists.

## Decisions log
| Date | Decision | Why | Who |
|---|---|---|---|
| | | | |
