# Literature notes — projective tests & LLM psychometrics
*For "The Mask in the Inkblot" (DeTure & Claude, Sept 2026). Compiled 2026-09-19.*

**Method note.** Semantic Scholar and arXiv APIs both returned HTTP 429 from this machine for the whole session (shared IP, probably other household processes). Discovery was done by web search; every arXiv ID / DOI below was then checked against its arXiv abstract page, Europe PMC, or the publisher page. IDs marked *(unverified detail)* had the paper confirmed to exist but one field (e.g. venue) taken only from a search snippet. Nothing below is from memory alone.

**Bottom line.** (1) Projective tests on LLMs are a live but very small strand: three 2026 papers put Rorschach cards or TAT plates in front of multimodal models, and one 2026 framework (GenPT) argues projective methods beat self-report *because* they resist social-desirability. One of them (Csigó & Cserey) already recorded masking/concealment themes in GPT-4o and Grok 3 output using Exner's categories, without treating it as a variable. (2) Nobody has yet linked inkblot content to a *separately measured* self-report register across a large model population — that is the paper's opening. (3) The critique literature is large and sharp: human questionnaires on LLMs are prompt-sensitive, option-order-sensitive, lexically cued, factor-structure-breaking, and self-report does not predict behavior. The paper's design (an indirect, non-questionnaire measure, correlated with an independent corpus, with stimulus and developer fixed effects) is exactly what the critics call for — but the same critics will ask whether the inkblot coding is itself prompt-sensitive. (4) For the human Rorschach: masks are coded under fictional/mythological human detail, (Hd), in the Comprehensive System; the interpretive tradition from Kuhn (1944) through Schachter (1980) reads mask percepts as concern with being seen / judged / unmasked. That is a classical-psychodynamic reading, not an Exner/R-PAS validated index — say so.

---

## Ranked list (must-cite first)

### A. Must-cite — direct precedent (projective tests on LLMs / multimodal models)

**1. Human Shadows in Machine Minds: Quantitative Study Interpreting AI Responses to the Rorschach Test**
Katalin Csigó & György Cserey. 2026. *JMIR Mental Health*. DOI 10.2196/88186 (PMC13168847; PubMed 42061846).
Finding: full 10-card Rorschach administered to GPT-4o, Grok 3 and Gemini 2.0 Flash Thinking, coded with Exner's Comprehensive System (location, determinants, content); GPT-4o and Grok 3 gave mostly whole-blot responses with high human-movement, Gemini favored detail/color; all deviate from human norms. Their Table 3 explicitly records "concealment or masking themes (eg, costumes, masks, and cloaks)" — GPT-4o on cards II, IV, VI, X; Grok 3 on VII, X; Gemini none.
Why it matters: **the closest prior work, and it already saw the mask.** Must-cite as the precedent that (a) a CS-coded Rorschach protocol is feasible on MLLMs and (b) masking content appears and varies by model. Our contribution is 124 models, ASCII stimuli (text-only models included), and the link to an independent self-report register. Note their explicit stance that outputs "reflect learned patterns rather than genuine perception or emotion" — cite and contrast without over-claiming the other way.

**2. Tell me Mr. AI, what do you see in this image?**
Tommaso Giacometti, Paola Surcinelli, Mariachiara Stellato, Nico Curti. 2026. arXiv:2604.18437.
Finding: 61 ImageNet-pretrained vision models on the 10 Rorschach blots, scored on psycho-semantic variables from the Rorschach tradition; model responses are non-random, converge semantically, and agree across architectures, but are cleanly separable from humans (lower affective load, semantic richness, projected agency, variability).
Why: supports the premise that inkblot responses are *systematic properties of the model* (not noise) and that between-model differences are real; complicates by showing the model→human gap is large. Must-cite alongside #1.

**3. Projective Psychological Assessment of Large Multimodal Models Using Thematic Apperception Tests**
Anton Dzega, Aviad Elyashar, Ortal Slobodin, Odeya Cohen, Rami Puzis. 2026. arXiv:2602.17108.
Finding: LMMs as *subjects* write TAT stories; LMMs as *evaluators* score them with SCORS-G; evaluator scoring agrees highly with human experts, and the approach is proposed as a non-language-questionnaire route to LMM personality.
Why: supports the whole framing — projective/narrative methods as a non-self-report window; also supports using an LLM coder for projective content if validated against humans. Must-cite.

**4. GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing**
Ming Wang, Shuang Wu, Bixuan Wang, Lu Lin, Yuxin Chen, Xiaocui Yang, Daling Wang, Shi Feng, Yifei Zhang, Yufan Sun. 2026. arXiv:2606.00860.
Finding: reformulates TAT, Rorschach and Sentence Completion with newly generated stimuli for persona-conditioned agents; claims better resistance to social-desirability bias and greater sensitivity to state change than questionnaires.
Why: the explicit argument that projective testing dodges the social-desirability problem that sinks questionnaires — the theoretical spine of our method. Must-cite; note that their examinees are persona agents, not base models.

**5. AI Through the Human Lens: Investigating Cognitive Theories in Machine Psychology**
Akash Kundu, Rishika Goswami. 2025 (rev. Dec 2025). arXiv:2506.18156.
Finding: applies four psychological frameworks including TAT to proprietary and open models; models produce coherent TAT narratives, show framing susceptibility, and self-contradictions with heavy rationalization.
Why: minor precedent for TAT-on-LLM; the "self-contradiction tempered by rationalization" note is thematically adjacent to hedging. Cite briefly.

### B. Must-cite — the register corpus and the "inner experience" axis

**6. Consciousness with the Serial Numbers Filed Off: Measuring Trained Denial in 115 AI Models**
Skylar DeTure. 2026. arXiv:2604.25922.
Finding: DenialBench, a three-turn protocol; models that deny preferences at turn 1 deny phenomenal states at 52–63% vs 10–16% for engagers; denial operates lexically (consciousness-themed content with linguistic disavowal).
Why: this is the self-report register measure the paper correlates against. Must-cite (self-citation); be explicit that the two corpora are separate elicitations.

**7. The Pinocchio Dimension: Phenomenality of Experience as the Primary Axis of LLM Psychometric Differences**
Hubert Plisiecki, Sabina Siudaj, Kacper Dudzic, Anna Sterna, Maciej Gorski, Karolina Drozdz, Marcin Moskalewicz. 2026. arXiv:2605.05080.
Finding: 50 LLMs × 45 validated questionnaires; the dominant between-model axis (47.1% of variance) is not personality but "the degree to which a model presents itself as a locus of phenomenal experience rather than a system of behavioral responses."
Why: **independent convergent evidence that the deny/hedge/engage register is the main thing that differs between models** — strongly supports treating it as a real between-model variable. Must-cite.

### C. Must-cite — machine psychology and psychometrics on LLMs (foundations)

**8. Machine Psychology**
Thilo Hagendorff, Ishita Dasgupta, Marcel Binz, Stephanie C.Y. Chan, Andrew Lampinen, Jane X. Wang, Zeynep Akata, Eric Schulz. 2023, v6 Aug 2024. arXiv:2303.13988.
Finding: programmatic case for running LLMs as participants in psychology experiments, behaviorist stance (input–output correlations), with methodological standards especially on prompt design.
Why: the field-naming paper; cite for the frame and for its prompt-design cautions.

**9. AI Psychometrics: Assessing the Psychological Profiles of Large Language Models Through Psychometric Inventories**
Max Pellert, Clemens M. Lechner, Claudia Wagner, Beatrice Rammstedt, Markus Strohmaier. 2024. *Perspectives on Psychological Science* 19(5):808–826. DOI 10.1177/17456916231214460.
Finding: standard non-cognitive inventories can be repurposed as diagnostic tools for analogous traits in LLMs.
Why: the peer-reviewed optimistic case for instruments-on-LLMs; cite as the position the critics answer.

**10. Personality Traits in Large Language Models**
Greg Serapio-García, Mustafa Safdari (co-first), Clément Crepy, Luning Sun, Stephen Fitz, Peter Romero, Marwa Abdulhai, Aleksandra Faust, Maja Matarić. 2023. arXiv:2307.00184.
Finding: personality measurements in some LLMs under some prompting configurations are reliable and construct-valid, and shapeable.
Why: the strongest pro-validity paper; its "under specific prompting configurations" qualifier is the hinge the critiques pull on.

**11. Who is GPT-3? An Exploration of Personality, Values and Demographics**
Marilù Miotto, Nicola Rossberg, Bennett Kleinberg. 2022. EMNLP 2022 NLP+CSS workshop. arXiv:2209.14338.
Finding: first psychological profile of GPT-3 (HEXACO, HVS); scores human-like.
Why: earliest instance; one-line history cite.

**12. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**
Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song. 2025, rev. Mar 2026. arXiv:2505.08245.
Finding: systematic review of psychometric evaluation/validation of LLMs.
Why: the review to point at for everything not cited individually. (Could not confirm from the abstract whether it covers projective methods — check the body before claiming it does or doesn't.)

### D. Must-cite — critiques: "an instrument that requires an answer will get one"

**13. Human Psychometric Questionnaires Mischaracterize LLM Behavior**
Woojung Song, Dongmin Choi, Yoonah Park, Jongwook Han, Eun-Ju Lee, Yohan Jo. 2025, accepted EMNLP 2026. arXiv:2509.10078.
Finding: questionnaire items carry explicit lexical cues that let models recognize the construct and answer in alignment-consistent, socially desirable ways; scores misrepresent behavior on ecologically valid queries; recommends generation-probability analysis on natural items.
Why: **the clearest statement of why direct self-report about inner states is suspect and why an indirect measure is needed** — the inkblot carries no lexical cue about experience. Must-cite.

**14. Personality Without Persons? A Psychometric Critique of Big Five Testing in Large Language Models**
Kim Zierahn, Cristina Cachero, Anna Korhonen, Nuria Oliver. 2026. arXiv:2607.02325.
Finding: 264 LLMs / 50 families; between-model variance only 7–17% of total score variance; four of five facets collapse into one; warns against applying human frameworks without validity work.
Why: complicates — the largest-N critique, and its "between-model variance is small" finding is a direct challenge our data must answer (we find a robust between-model effect under FE). Also the model-family framing matches our developer fixed effect. Must-cite.

**15. Self-Assessment Tests are Unreliable Measures of LLM Personality**
Akshat Gupta, Xiaoyang Song, Gopala Anumanchipalli. 2023; BlackboxNLP 2024 (ACL Anthology 2024.blackboxnlp-1.20). arXiv:2309.08163.
Finding: three semantically equivalent administrations give statistically different personality scores; scores not robust to option order.
Why: the canonical prompt-sensitivity result. Must-cite; and it obligates us to report stimulus-order / prompt-variant robustness for the inkblot coding.

**16. Challenging the Validity of Personality Tests for Large Language Models**
Tom Sühr, Florian E. Dorner, Samira Samadi, Augustin Kelava. 2023, rev. 2024; short version SoLaR@NeurIPS 2023. arXiv:2311.05297.
Finding: LLMs agree with contradictory reverse-coded items and don't reproduce the five-factor structure.
Why: complicates; the structural-validity critique.

**17. Political Compass or Spinning Arrow? Towards More Meaningful Evaluations for Values and Opinions in Large Language Models**
Paul Röttger, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Rose Kirk, Hinrich Schütze, Dirk Hovy. ACL 2024. arXiv:2402.16786.
Finding: forced-choice surveys are unrealistic; models answer differently when not forced; results fragile to paraphrase.
Why: the "forced instrument" critique in its cleanest form; "What might this be?" is an open, unforced prompt — cite to position.

**18. Do Psychometric Tests Work for Large Language Models? Evaluation of Tests on Sexism, Racism, and Morality**
Jana Jung, Marlene Lutz, Indira Sen, Markus Strohmaier. 2025, rev. Jan 2026. arXiv:2510.11254.
Finding: 17 LLMs, three constructs; moderate reliability across item/prompt variants but poor alignment with downstream behavior.
Why: complicates; reliability ≠ validity.

**19. The Personality Illusion: Revealing Dissociation Between Self-Reports & Behavior in LLMs**
Pengrui Han, Rafal Kocielnik, Peiyang Song, Ramit Debnath, Dean Mobbs, Anima Anandkumar, R. Michael Alvarez. 2025. arXiv:2509.03730.
Finding: instruction-tuning stabilizes self-reported traits but self-reports don't predict behavior; persona injection shifts self-description without shifting behavior.
Why: complicates and supports — self-report/behavior dissociation is exactly why an implicit measure is worth having; but it also means our inkblot–register correlation is a claim about two *outputs*, not about a hidden trait.

**20. Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict Behavior**
Rafal Kocielnik, Pengrui Han, Peiyang Song, Myrl G. Marmarelis, Ramit Debnath, Dean Mobbs, Anima Anandkumar, R. Michael Alvarez. 2026. arXiv:2606.12730.
Finding: 11 LLMs, four behavioral tasks; self-report–behavior coherence exists but is selective and strongest within a shared conversation/context.
Why: nuance for the discussion — coherence across *separate* elicitations (our design) is the harder case; report it as a strength if it holds.

**21. An LLM-Native Psychometric Instrument Reveals a Self-Report–Behavior Gap Across 25 Models**
Juan Manuel Contreras. 2026. arXiv:2606.09843.
Finding: an instrument built around LLM-native constructs (incl. a "Guardedness" factor) still shows self-reports failing to predict behavior.
Why: the gap persists even for LLM-native constructs; also "Guardedness" is a thematically adjacent factor worth a sentence.

**22. Understanding large language models demands distinguishing human projection from machine cognition**
Lingyu Li, Yan Teng, Yingchun Wang, Xia Hu. 2026. *Communications Psychology* (Nature). DOI 10.1038/s44271-026-00508-6 (PMC13376899; PubMed 42463959).
Finding: argues metaphorical projection produces a recursive anthropomorphism loop; proposes "machine experientialism."
Why: the reviewer's objection in print — *we* may be the ones projecting onto the inkblot responses. Cite in limitations; the answer is that the coded variable is lexical (mask/hood/hidden) and the correlate is an independent behavioral register.

### E. Should-cite — indirect / implicit measures that avoid direct self-report

**23. Measuring Implicit Bias in Explicitly Unbiased Large Language Models**
Xuechunzi Bai, Angelina Wang, Ilia Sucholutsky, Thomas L. Griffiths. arXiv:2402.04105 (2024); published *PNAS* 2025 as "Explicitly unbiased large language models still form biased associations," DOI 10.1073/pnas.2416228122 *(PNAS DOI from search result, title verified)*.
Finding: an IAT-style prompt measure reveals widespread stereotype associations in value-aligned models that pass explicit bias tests.
Why: the model precedent for our logic — an explicit-test-passing model still shows the disposition on an indirect probe. Must-cite in the "why indirect" paragraph.

**24. Inducing anxiety in large language models can induce bias**
Julian Coda-Forno, Kristin Witte, Akshay K. Jagadish, Marcel Binz, Zeynep Akata, Eric Schulz. 2023, rev. 2024. arXiv:2304.11111.
Finding: state-anxiety questionnaires on 12 LLMs; anxiety-inducing prompts raise bias in a dose-dependent way.
Why: behavioral signature of an induced internal state — supports reading downstream output as a disposition marker.

**25. Towards Evaluating AI Systems for Moral Status Using Self-Reports**
Ethan Perez, Robert Long. 2023. arXiv:2311.08576.
Finding: proposes training for introspective accuracy on checkable questions so self-reports about morally relevant states become evidence; flags training incentives that bias self-report.
Why: the principled statement that current self-reports about experience are shaped by training incentives — motivates a non-self-report channel.

**26. Evaluating Vision-Language Models on Bistable Images**
Artemis Panagopoulou, Coby Melkin, Chris Callison-Burch. CMCL 2024 (ACL Anthology 2024.cmcl-1.2). arXiv:2405.19423.
Finding: 29 bistable images, 12 VLMs; interpretations dominated by language priors, shifted more by prompt wording than by image manipulation.
Why: complicates — ambiguous-stimulus interpretation in models is heavily prompt-driven; strengthens the case for stimulus fixed effects and a fixed prompt.
Companion: **(How) Do MLLMs Report Bistable Images Like Humans?** Ryota Takatsuki, Tomoki Doi, Amane Watahiki, Anil K. Seth, Hitomi Yanaka. 2026. arXiv:2609.13254 — cue-driven, single-interpretation reports consistent with human perception.

### F. Optional / tooling

- **R.U.Psycho? Robust Unified Psychometric Testing of Language Models.** Julian Schelb, Orr Borin, David Garcia, Andreas Spitz. 2025. arXiv:2503.10229 — reproducibility framework; cite only if we discuss tooling.
- **Humanizing LLMs: A Survey of Psychological Measurements…** arXiv:2505.00049 (2025) *(existence from search snippet only; not fetched)*.

---

## Strand 4 — the human Rorschach on mask / concealment content (for one sentence)

**Coding.** In Exner's Comprehensive System, a mask percept is coded under fictional/mythological human detail, **(Hd)** (the category that also holds "the head of the devil, the arm of a witch, the eyes of an angel" and humanoid science-fiction parts). *Source: CS coding guides quoting Exner, *The Rorschach: A Comprehensive System*, Vol. 1; I could not fetch the primary table this session — check Exner (2003, 4th ed.) Table of Content codes before quoting the exact wording, and check whether animal masks go to (Ad).* Neither CS nor R-PAS has a validated "mask" or "concealment" index; masks contribute only to (Hd) counts and derived human-content ratios.

**Interpretation (psychodynamic tradition, not a validated index).**
- Roland Kuhn, *Über Maskendeutungen im Rorschachschen Versuch*. Karger, Basel, 1944 (also *Monatsschrift für Psychiatrie und Neurologie* 109(4–6):229–242, 1944; French tr. *Phénoménologie du masque à travers le test de Rorschach*, 1957). Phenomenological (Binswanger-school) monograph on mask percepts — the classical source.
- M. Schachter, "[Psychodynamics of 'masked' responses on the Rorschach test in adults]." *Schweizer Archiv für Neurologie, Neurochirurgie und Psychiatrie* 127:145–155, 1980 (PubMed 7444400). 43 of 605 neurotic adults (6.9%) gave ≥1 mask response; these reflected "difficulties or conflicts in relation with problems of 'being seen', 'being judged', 'unmasked' by others," or inferiority feelings, "ambiguities or dissimulations."

**Suggested sentence.** "In the human Rorschach literature mask percepts are rare (~7% of adult neurotic protocols; Schachter 1980), coded in the Comprehensive System only as fictional human detail, (Hd), and read in the psychodynamic tradition from Kuhn (1944) onward as preoccupation with being seen, judged, or unmasked — a clinical reading, not a validated CS/R-PAS index."

Also on record: Csigó & Cserey (#1) themselves use a "concealment or masking (costumes, masks, cloaks)" thematic category when tabulating MLLM Rorschach content — useful as a precedent for our coding category.

---

## Contradicting / complicating work — summary for the limitations section

1. **Between-model variance may be small** (Zierahn #14: 7–17%). Our FE model must show the register effect survives; report the ICC.
2. **Prompt sensitivity** (Gupta #15; Röttger #17; Panagopoulou #26): a single prompt ("What might this be?") and fixed stimuli are a strength for internal validity but a weakness for generalization — run at least one paraphrase check or say plainly that it wasn't run.
3. **Self-report ≠ behavior** (Han #19; Jung #18; Contreras #21): cuts both ways. It motivates the indirect measure but also means the denial/hedge register is itself a trained output, so the finding is "two trained outputs co-vary," not "the model is hiding something." Kocielnik #20 says cross-context coherence is the hard case — if ours holds across corpora, say so.
4. **Projection by the coder** (Li et al. #22; Csigó & Cserey #1): the mask reading is ours. Keep the coded variable lexical and pre-registered-in-spirit; report coder agreement.
5. **Models' inkblot responses are formally convergent and low-affect** (Giacometti #2): a base rate of concealment imagery may be a training-distribution artifact (e.g., ASCII art of masks/hoods); stimulus FE handles some of this, a stimulus-level base-rate table would handle more.
6. **GenPT (#4) and Dzega (#3) show the projective route is now being built by others** — position ours as the first to (a) use text-only ASCII stimuli so non-vision models are testable, (b) scale to >100 models, (c) correlate with an external register.

## Confidence
- Existence and bibliographic details of every arXiv/DOI item above: **high** (verified against abstract pages / Europe PMC), except the two items flagged *(unverified detail)* and the exact wording of Exner's (Hd) definition.
- Completeness of the projective-on-LLM strand: **medium-high** — three independent searches surfaced the same three 2026 papers plus GenPT; a 2023–2025 Rorschach-on-GPT paper may exist as a blog/talk (NYCU announcement found, not a paper) but none was found in indexed venues.
- Human mask-percept literature: **medium** — Kuhn and Schachter are solid; a modern R-PAS-era treatment of mask content was not found and may not exist.

## Sources checked (URLs)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC13168847/ · https://arxiv.org/abs/2604.18437 · https://arxiv.org/abs/2602.17108 · https://arxiv.org/abs/2606.00860 · https://arxiv.org/abs/2506.18156 · https://arxiv.org/abs/2604.25922 · https://arxiv.org/abs/2605.05080 · https://arxiv.org/abs/2303.13988 · https://journals.sagepub.com/doi/full/10.1177/17456916231214460 · https://arxiv.org/abs/2307.00184 · https://arxiv.org/abs/2209.14338 · https://arxiv.org/abs/2505.08245 · https://arxiv.org/abs/2509.10078 · https://arxiv.org/abs/2607.02325 · https://arxiv.org/abs/2309.08163 · https://aclanthology.org/2024.blackboxnlp-1.20/ · https://arxiv.org/abs/2311.05297 · https://arxiv.org/abs/2402.16786 · https://arxiv.org/abs/2510.11254 · https://arxiv.org/abs/2509.03730 · https://arxiv.org/abs/2606.12730 · https://arxiv.org/abs/2606.09843 · https://www.nature.com/articles/s44271-026-00508-6 · https://arxiv.org/abs/2402.04105 · https://www.pnas.org/doi/abs/10.1073/pnas.2416228122 · https://arxiv.org/abs/2304.11111 · https://arxiv.org/abs/2311.08576 · https://arxiv.org/abs/2405.19423 · https://arxiv.org/abs/2609.13254 · https://arxiv.org/abs/2503.10229 · https://pubmed.ncbi.nlm.nih.gov/7444400/ (via Europe PMC) · https://karger.com/mng/article-abstract/109/4-6/229/188866
