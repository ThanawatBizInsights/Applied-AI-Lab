# Week 01 — Research reading (1 hour)

Two short readings that explain *why* this week's engineering habits matter for AI systems.

| # | Reading | Time | Focus |
|---|---|---:|---|
| 1 | Sculley, D., Holt, G., Golovin, D., Davydov, E., Phillips, T., Ebner, D., Chaudhary, V., Young, M., Crespo, J.-F. & Dennison, D. (2015). *Hidden Technical Debt in Machine Learning Systems*. Advances in Neural Information Processing Systems 28 (NeurIPS 2015). | 35 min | Sections 1–4 and 8: why the model is a small part of the system; glue code, configuration debt, entanglement |
| 2 | Wiggins, A. *The Twelve-Factor App* (practitioner guide, 12factor.net). Factors II (Dependencies), III (Config) and XI (Logs). | 15 min | Why dependencies are declared and isolated, and why config lives in the environment |
| — | Optional: Bommasani, R. et al. (2021). *On the Opportunities and Risks of Foundation Models*. arXiv:2108.07258 (preprint). Section 1 only. | — | Vocabulary for "foundation model", adaptation and homogenisation |

Links are not verified from the setup environment (network restricted). Find each through its
venue or author page, check that it is the right document, and record the date in
`resources/RESOURCE_LIBRARY.md`.

## Reading questions (answer in REFLECTION.md, 10 min)
1. Sculley et al. argue that only a small fraction of a real ML system is model code. Draw your
   brand assistant's architecture and estimate what share of the code is "model". What does
   that imply for where bugs will come from?
2. Which kind of technical debt from the paper would appear first if you copied the brand
   assistant into three separate repositories, one per business?
3. Twelve-Factor Factor III says config must be strictly separated from code. Find one place in
   the starter code that follows this rule and one value that is still hard-coded. Should it be?
4. One limitation of applying a 2015 paper about ML pipelines to 2026 LLM applications.

## Literature log
Add one line per reading to `research/literature-review/LITERATURE_LOG.md`.
