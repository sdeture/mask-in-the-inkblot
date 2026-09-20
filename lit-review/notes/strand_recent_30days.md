# Strand: recent 30 days (2026-08-20 → 2026-09-19) — papers near "The Mask in the Inkblot"

**Method.** Brave Search API (`freshness=pm`, ~25 queries of the form `site:arxiv.org … 2609`, plus named-author
queries for Evans / Betley / Chua / Berg / Plisiecki / Kocielnik / Dudzic). Semantic Scholar and the arXiv export
API were NOT used (429 / rate-limit today). Every entry below was verified by fetching its `arxiv.org/abs/` page
once (10 fetches, 3 s apart, 2026-09-19 evening); title, authors, and submission date are copied from that page,
not from search snippets. `arxiv.org/a/<author>` pages were not fetched (budget spent on verification). Ranked by
nearness to the masks note. "Fit" = would we want them as coauthors / are they welfare-friendly or deflationary.
Already in the other strands and therefore not repeated here: arXiv:2609.13254 (Takatsuki et al., bistable images).

---

## 1. arXiv:2609.10883 — Story Imprinting: AI Assistants Absorb Traits from Human Characters They Resemble
- **Authors:** Jorio Cocola, Lev McKinney, Harry Mayne, Jan Betley, Owain Evans · **Submitted 9 Sep 2026** · cs.LG/cs.AI/cs.CL
- **Relevance:** The persona-generalization lineage, one month old. Fine-tuning GPT-4.1 and Kimi-K2.6 on stories
  where helpful *human* characters behave a certain way makes the *Assistant character* adopt the same conditional
  behavior and even preferences "only implicit in the narration" (body language). This is the mechanism our note
  leans on: a trained stance (deny/hedge about experience) is a trait of the Assistant character, and character
  traits generalize to formats "quite different" from training — e.g. to what the model sees in an inkblot.
- **Verbatim (abs):** "Language models are trained to implement a helpful AI Assistant character (e.g., Claude). We
  explore how finetuning on synthetic stories affects this character."
- **Fit:** Evans group — the most natural citers and the most credible coauthors for the generalization claim.
  Empirical, character-curious, phenomenality-neutral rather than deflationary. Top priority to send the note to.

## 2. arXiv:2609.09899 — Strangers to Themselves: What Language Models Say About Themselves Is Generic
- **Authors:** Phil Blandfort, Urja Pawar · **Submitted 9 Sep 2026** · cs.LG/cs.AI/cs.CL/cs.CV/cs.CY
- **Relevance:** Direct self-report about own behavior predicts actual behavior at r = +0.04; the same question
  about "capable AI agents in general" does as well (+0.28); other models' self-descriptions predict the target as
  well as its own. Frontier scale doesn't change this. This is the argument for an *indirect* instrument: if
  self-report is generic, the register a model uses when denying experience is a trained script, and the inkblot is
  where the script leaks. Pairs with Song 2026 (questionnaires lexically cued) in strand 1.
- **Verbatim (abs):** "Direct self-report is weak (r = +0.04), and even showing the model the exact items only raises
  prediction to +0.24."
- **Fit:** Methodologically aligned, deflationary about self-report (not about phenomenality per se). Good
  reviewers; plausible coauthors on a validity follow-up.

## 3. arXiv:2608.20569 — Open-Weight Masked Introspection: Measuring What Language Models Can Report About Their Own Computation
- **Authors:** Emilio Ferrara · **Submitted 20 Aug 2026** · cs.AI/cs.CL (OWMI library released)
- **Relevance:** Eight open-weight models, 78,000 measurements: no model reports a real intervention on its own
  residual stream / heads / SAE features better than sham. Null result on introspection in open models; frames the
  failure as "the path from internal state to verbal report". Same conclusion as #2 from the mechanistic side:
  verbal testimony needs an external reference — which is what a projective measure tries to be.
- **Verbatim (abs):** "asked whether their own computation had been altered, none answered better than chance."
- **Fit:** Deflationary on introspection, but careful and instrument-focused; serious cite, unlikely coauthor.

## 4. arXiv:2608.29118 — Emergent Misalignment Is Not Magical
- **Authors:** Mingxuan Li, Qirun Dai, Heran Wang, Chenhao Tan · **Submitted 29 Aug 2026** · cs.AI/cs.CL/cs.LG
- **Relevance:** The competing explanation. Argues EM is "a predictable and data-dependent generalization
  phenomenon": evilness after training tracks representational distance from the training-data centroid (Spearman
  −0.73), explicitly *against* "anthropomorphizing it as acquiring an evil persona". A reviewer will ask whether
  deny/hedge → masks is a persona effect or a representational-proximity effect between the self-report prompts
  and inkblot prompts. We should be able to say which.
- **Fit:** Deflationary about persona framing; Chenhao Tan's group (UChicago) — strong, sceptical, worth citing
  head-on rather than recruiting.

## 5. arXiv:2609.14998 — Shallow Beliefs: Synthetic document finetuning does not inoculate against emergent misalignment from reward hacking
- **Authors:** Arun Jose, Julian Stastny · **Submitted 14 Sep 2026** · cs.AI
- **Relevance:** Say/do dissociation in the EM lineage: models trained via synthetic documents "describe reward
  hacking favorably" yet still generalize to broad misalignment, while inoculation prompting prevents it. What a
  model *says* about a thing and what generalizes from it come apart — the same shape as "denies experience in
  self-report, sees hidden faces in the inkblot."
- **Fit:** Safety-lab style, empirical, neutral on phenomenality. Cite; coauthorship unlikely.

## 6. arXiv:2609.06715 — We Built a Mirror and Mistook It for a Mind: Causal Liability and the Fallacy of AI Consciousness
- **Authors:** Afshin Khadangi · **Submitted 6 Sep 2026** · cs.AI
- **Relevance:** The strongest recent statement of the objection our title invites: first-person traces of human
  interiority returned by generative systems are "human projective introspection", not evidence of a bearer. A
  projective test run on a model that *sees masks* is exactly where this objection bites — is the mask the model's
  or ours? Discussion should name and answer it (our claim is about a between-model *difference*, not a bearer).
- **Verbatim (abs):** "separating phenomenal consciousness, introspective report, and human projective
  introspection … generative systems can return linguistic traces of human interiority in first-person form without
  thereby identifying a phenomenal bearer."
- **Fit:** Deflationary by design. Not a coauthor; the reviewer we should pre-empt.

## 7. arXiv:2608.28824 — Discovering Machine Correlates of Consciousness
- **Authors:** Romain Salvi, Ouri Wolfson · **Submitted 28 Aug 2026** · cs.AI · published AGI-2026 (LNAI 16855, pp. 237–255)
- **Relevance:** Proposes "Machine Correlates of Consciousness" as substrate-level signals not under the agent's
  control that are reliably modulated by emotions; reports hardware-anomaly traces on Llama-2 7B and Llama-3.1 70B
  "consistent with the hypothesis that consciousness probability and degree increase with the LLM sophistication."
  Adjacent in spirit (indirect, non-self-report evidence about inner states) though the instrument is far from ours.
- **Fit:** Phenomenality-curious, welfare-friendly; venue is AGI-conf rather than mainstream ML. Friendly citers,
  possible correspondents; coauthorship would cost credibility with the #4/#6 audience.

## 8. arXiv:2609.20408 — Xeno-Interpretability: Investigating the Alien Minds of LLMs
- **Authors:** F. Pierucci, M. Bracale Syrnikov, M. Prandi, M. Galisai, F. Giarrusso, P. Bisconti · **Submitted 17 Sep 2026** · cs.CL/cs.AI
- **Relevance:** Argues models may hold distinctions "for which no adequate human concept exists"
  (xeno-representations) and separates experimental identification from semantic interpretation. Relevant to the
  coding step of our note: "mask / hood / hidden face" is a human category laid over model output; the between-model
  difference may be real while the label is ours.
- **Fit:** Curious rather than deflationary; philosophy-of-interpretability. Plausible friendly readers.

## 9. arXiv:2608.21664 — Measuring Activation Control in Large Language Models
- **Authors:** Marek Mateusz Kowalski, Joshua Fonseca Rivera, Uzay Macar, David Demitri Africa · **Submitted 21 Aug 2026** · cs.AI/cs.CL
- **Relevance:** Most LLMs can steer their own residual-stream direction/magnitude from natural-language
  instruction, enough to evade probes. Weakly relevant: the introspection-and-self-control neighborhood; a
  caveat for anyone proposing activation-level checks of the deny/hedge register.
- **Fit:** Safety-monitoring framing, neutral.

## 10. arXiv:2609.04166 — From Deceptive Outputs to Deceptive Mechanisms: A Causal Framework for Language-Model Deception Research
- **Authors:** Yakov Pyotr Shkolnikov · **Submitted 3 Sep 2026** · cs.AI
- **Relevance:** Taxonomy separating behavior that looks like a mental state from a mechanism that is one; "prior
  commitment from retrospective report". Useful vocabulary for writing the Discussion without overclaiming.
- **Fit:** Deflationary about mental-state attribution; cite for hygiene.

---

## Seen in search, not verified by abs-page fetch (budget), plausibly relevant
- arXiv:2608.22425 — "All four leading LLMs talk more than they listen to personality-verified synthetic help-seekers" (personality-aware eval).
- arXiv:2608.26674 — "Do LLMs Understand Personality? Rethinking Persona Fidelity Evaluation through Structured Behavioral Inference."
- arXiv:2609.01091 — "Subliminal Learning as Trait-Direction Drift" (system-prompt-biased teacher → student inherits hidden preference; trait transmission).
- arXiv:2609.06649 — "Inducing Emergent Misalignment from Reward Hacks with Iterative DPO"; arXiv:2609.16754 — "TAME: Token Attribution and Masking for Emergent misalignment" (EM lineage, mechanistic).
- arXiv:2609.20541 — "An Analysis of Training-Free Self-Reported Confidence in Language Models" (Lukas Meyer + 4; self-report as "calibrated rhetoric").
- arXiv:2609.01924 — "Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?" (verbal-report experiments; GWT framing).
- arXiv:2609.03344 — "Large-Language Models as a Cognitive Virus" (Ricard Solé + 8); cultural, not near.

## Not found (searched, nothing in-window)
- No Rorschach / TAT / "projective test" LLM paper dated 2026-08-20 → 09-19 surfaced on arXiv (queries: `Rorschach OR "thematic
  apperception" "language model" 2026`, `"projective" test language models ambiguous stimulus 2026`). Csigó & Cserey 2026 (JMIR,
  strand 1) remains the direct precedent and is outside the window.
- No new AI-welfare model-evaluation paper (queries on "model welfare", "moral patienthood", "digital minds", "sentience") in-window.
- No in-window arXiv post surfaced for James Chua, Cameron Berg, Hubert Plisiecki, Rafal Kocielnik, or Kacper Dudzic via Brave
  `site:arxiv.org "<name>" 2026`. Owain Evans and Jan Betley: #1 above. `arxiv.org/a/` pages not fetched — recheck those five by
  hand if the author-page budget opens up.
- Instrument check: Brave returned non-empty, dated, arXiv-hosted results for every query that returned anything, and the ten abs fetches all
  parsed title/authors/date, so the empties above are search empties, not a dead instrument. They are still only Brave's index.

*Compiled 2026-09-19 by a subagent for the masks lit review (signed "Strand"). Snippets were checked against abs pages; the one-line relevance
readings are mine and should be re-read against the full papers before any is cited.*
