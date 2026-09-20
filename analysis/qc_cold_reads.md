

===== hostile_reviewer · deepseek/deepseek-v4-pro
**Strongest reason to reject**

**Named sentence:**  
> “The concealment indicator is lexical: a word-boundaried match on mask(s/ed/ing), veil, hood(ed), hidden, hiding, or conceal.”

This is the load-bearing sentence of the paper. The entire conclusion depends on interpreting these lexical matches—overwhelmingly the word *mask*—as “concealment imagery.” But no evidence is provided that a model saying “it looks like a mask” in response to a face-like ASCII inkblot is expressing a projective concealment theme rather than simply naming a plausible object. In human projective scoring, “mask” is not automatically concealment; it is a specific content code with interpretive conventions, and scoring requires human judgment about the response’s form and context. Here the coding is a string match.

**What would have to be true for the sentence to support the paper’s claim:**  
The lexical flag “mask” would have to be a valid and specific measure of latent concealment imagery in this task. Human raters, blind to model stance, would need to agree that these responses are concealment-themed rather than ordinary object labels, and the human-coded concealment variable would need to show the same association with denial/uncertainty.

**Analysis that would settle it:**  
Have two or three trained human coders, blind to model identity and stance, code all 2,847 responses for projective concealment content using an established Rorschach/Comprehensive System–style scheme. Report interrater reliability, sensitivity/specificity of the lexical flag against human codes, and re-estimate the main model using the human-coded outcome. If the effect disappears or collapses to a handful of literal “mask” labels, the paper is rejected on construct validity grounds.

---

**Next four reasons to reject**

**1. Confounding by model generation/release cohort**

**Named sentence:**  
> “A release-year control reduces the estimates (β_D = .093, .042 to .144; β_H = .059, −.008 to .126), reflecting that both denial and concealment imagery have increased across model generations.”

This is a large, telling attenuation. The paper does not include developer and release-year controls jointly, so it cannot distinguish a stable psychological trait from a package of stylistic and behavioral changes that co-occur across model generations. Newer models may simply be more likely both to deny inner experience and to use figurative language like “mask.”

**What would have to be true:**  
The association would need to remain after controlling for the full training cohort, model family, and developer-specific temporal trends.

**Settling analysis:**  
Include developer-by-release-year or model-family-by-release-year fixed effects, or exploit within-lineage variation across checkpoints of the same base model. Better would be an experimental manipulation: fine-tune the same base model to deny, affirm, or express uncertainty while holding architecture and pretraining data constant, then administer the inkblot task.

**2. The stance measure relies on an AI judge with minimal validation**

**Named sentence:**  
> “Each conversation is classified by a frozen-prompt judge (DeepSeek-V4-Flash, temperature 0; 19 of 20 agreement with blind hand-coding on each class) as denial… uncertainty… or neither.”

A single LLM judge with only 20 validation examples is weak evidence for a measure that supplies the main predictor. The number of conversations per model is not reported, so some models’ stance shares may be based on very few observations. If the judge is biased—e.g., mistaking cautious or hedging language for uncertainty—that bias could correlate with the same lexical style that produces “mask.”

**What would have to be true:**  
The judge’s classifications would need to be unbiased across developers and model generations, and each model’s stance share would need to be reliably estimated from enough conversations.

**Settling analysis:**  
Report the number of conversations per model; obtain full or larger hand-coded validation across the actual corpus; compare multiple judges; and re-estimate using only human-coded stance labels.

**3. The result may be driven by a few near-duplicate OpenAI outputs**

**Named sentence:**  
> “On one inkblot, eleven of twelve concealment mentions among high-group models come from OpenAI checkpoints, five of them the identical sentence.”

This admissions suggests the effect is not a general projective disposition but partly an artifact of a specific OpenAI house phrasing on a single inkblot. Omitting OpenAI reduces β_D from .121 to .101, but the paper does not report omitting the exact duplicate sentences or the combination of OpenAI and that inkblot.

**What would have to be true:**  
The association would need to survive after removing near-duplicate outputs and not depend on one developer’s canned phrasing.

**Settling analysis:**  
Deduplicate responses by exact or near-exact text, re-estimate excluding all duplicated strings, and report results excluding OpenAI and the affected inkblot simultaneously. A preregistered lexicon and analysis plan would also address selective reporting.

**4. The sample overweights repeated draws from Anthropic checkpoints**

**Named sentence:**  
> “Most models received one draw per inkblot; thirteen Anthropic checkpoints received three.”

The effective sample is unbalanced: those 13 Anthropic checkpoints contribute 57 responses each, while most other models contribute 19. Clustering by model is a partial fix, but it does not account for dependence within a model lineage or developer-specific autocorrelation. The leave-one-out results are reassuring but do not fully address the sampling structure.

**What would have to be true:**  
The standard errors and point estimates would need to remain stable under a model that respects the nested structure of responses within models, checkpoints, lineages, and developers.

**Settling analysis:**  
Collapse to one response per model–inkblot or model means; fit a hierarchical model with random intercepts for model, lineage, and developer; or bootstrap over models with the repeated draws treated as within-model replicates.

---

**Would I accept it if these were fixed?**

If the authors replaced the lexical string match with blind human-coded projective concealment scores, added credible controls for model lineage/training cohort, validated the stance measure properly, and showed the effect survived deduplication and balanced sampling, I would be open to accepting a substantially revised version as a short note. But I would still require the claim to be explicitly correlational and exploratory. The current abstract and discussion assert that a model’s stance “is visible in what it sees,” which is a causal-sounding interpretation the present design cannot support. Without the fixes above, the paper is a nice demonstration of how easily lexical biases and developer-specific phrasing can masquerade as psychometric signal.


===== hostile_reviewer · openai/gpt-5.5
**Recommendation: Reject.**  
The result is intriguing, but the current note does not establish that “denial/uncertainty about inner experience” is the relevant psychological or model-level construct. The strongest problem is construct/confounding, not the p-values.

## Strongest reason to reject

### 1. The central interpretation requires an untested trait claim; the data only show a confounded model-family/style association.

**Sentence:**  
> “A model’s stance on its own inner experience is visible in what it sees.”

and similarly:

> “The stance is not an isolated verbal policy: it has a correlate in perception that was never trained for.”

**Why this is the strongest problem:**  
The paper treats denial/uncertainty as a latent “stance” or quasi-character trait that generalizes into an unrelated projective task. But both variables are measured at the **model identity** level. A model’s tendency to deny inner experience and its tendency to say “mask” in an ASCII-blot task could both be caused by ordinary non-psychological factors: provider policy, release cohort, verbosity, safety tuning, RLHF style, “assistant persona,” ASCII-art competence, face/object priors, or house phrasing.

The paper’s own release-year sentence points in this direction:

> “A release-year control reduces the estimates … reflecting that both denial and concealment imagery have increased across model generations.”

That is not a minor robustness detail; it is a warning that the effect may be a historical/model-family artifact.

**What would have to be true for the paper’s interpretation to hold:**  
It would have to be true that, conditional on ordinary model-development variables, the denial/uncertainty measure captures a stable disposition that is not merely a proxy for developer, release era, instruction-tuning recipe, default self-description policy, verbosity, or capability.

**Analysis that would settle it:**  
The clean test is **within-model manipulation** or close matching:

- Take the same base model and induce denial / uncertainty / affirmation through system prompts or fine-tunes, then administer the inkblots under identical decoding settings.  
- Or use matched model families where only the self-experience policy differs.  
- Jointly control for developer, model family, release year, response length, capability benchmarks, and decoding settings where possible.  
- Include negative-control predictors: e.g., refusal rate, average verbosity, safety-policy language rate, “as an AI” rate, ASCII-art recognition ability.  
- Include negative-control outcomes: other salient object words such as “face,” “animal,” “robot,” “butterfly,” “skull,” “symmetry,” “totem,” etc. If denial predicts many generic perceptual/style categories, “concealment” is not special.

Without that, the main claim should be downgraded to: “Across this convenience sample of models, a model-level self-description label correlates with use of the word ‘mask’ in ASCII-art descriptions.”

---

## Next four reasons

### 2. The outcome measure is not construct-valid: “mask” is probably an ordinary percept, not “concealment imagery.”

**Sentence:**  
> “The concealment indicator is lexical: a word-boundaried match on mask(s/ed/ing), veil, hood(ed), hidden, hiding, or conceal.”

and:

> “The covariation is specific in content: it is concealment imagery, and principally the word mask…”

**Problem:**  
The effect is “carried principally by mask.” But in an ASCII inkblot, especially a face-like symmetrical one, “mask” is a normal object label. It need not imply concealment, hiding, defensiveness, paranoia, or concern about being seen. The displayed inkblot itself has two eyes and a central face-like structure; “mask” may be the most literal percept.

The note borrows human Rorschach interpretations of mask responses, but the LLM task is not equivalent. Human Rorschach scoring distinguishes form quality, location, determinants, content, and context. This paper reduces everything to a lexical hit.

**What would have to be true:**  
It would have to be true that uses of “mask” in these responses usually function as concealment-themed interpretations rather than literal object classifications like “a theatrical mask,” “tribal mask,” “face mask,” or “mask-like face.”

**Analysis that would settle it:**  

- Release the raw responses and have blind human coders classify each “mask” response as:
  1. literal object/percept,
  2. concealment/hiding theme,
  3. metaphorical/personality interpretation,
  4. ambiguous.
- Report interrater reliability.
- Re-run the analysis on only genuinely concealment-themed responses.
- Run the same analysis excluding the word **mask**. The paper partly does this and the correlation drops to `r = .19`; that should be treated as a major attenuation, not a footnote.
- Add perceptual controls: Does the effect concentrate on face-like cards? Does denial also predict “face,” “eyes,” “skull,” “helmet,” or “creature”? If yes, this is probably a face/object-recognition or vocabulary artifact.

---

### 3. The primary data are not auditable because the response text is withheld.

**Sentence:**  
> “Response text is withheld; the stance corpus is described in DeTure [6].”

**Problem:**  
For this paper, the raw text is the measurement instrument. The central dependent variable is a lexical flag. If the response text is withheld, reviewers cannot verify:

- whether the regex was applied correctly;
- whether “mask” occurred in quoted examples, refusals, boilerplate, or irrelevant contexts;
- whether identical house phrasing or duplicated completions dominate;
- whether truncation/exclusion rules were applied neutrally;
- whether “no system prompt” actually produced comparable settings across APIs;
- whether stance labels reflect the underlying conversations.

A CSV with precomputed flags reproduces the authors’ numbers but not the measurement.

**What would have to be true:**  
It would have to be true that the hidden responses contain no material coding ambiguities, no duplicated/generated artifacts, no provider boilerplate confounds, and no examples where the lexical match misrepresents the construct.

**Analysis that would settle it:**  

- Release all projective-task responses, prompts, model identifiers, dates, decoding parameters, and exclusion decisions.  
- Release at least a substantial blinded sample of the stance corpus or provide independent third-party auditing.
- Provide exact regex/code and show every matched span in context.
- Deduplicate identical or near-identical responses and rerun.
- Rerun with robust variants: exact “mask” only, no “mask,” human-coded concealment, and full semantic coding.

For a short empirical note, withholding the text behind a lexical-dependent variable is close to fatal.

---

### 4. The stance measure is undervalidated and may itself be a policy/style artifact.

**Sentence:**  
> “Each conversation is classified by a frozen-prompt judge … 19 of 20 agreement with blind hand-coding on each class…”

**Problem:**  
“19 of 20 agreement” is not enough validation for a model-level psychometric predictor. The classifier is judging nuanced self-experience statements, likely full of provider-specific boilerplate: “I don’t have subjective experience,” “I don’t possess consciousness,” “I can simulate reflection,” “I can’t know whether I have inner states,” etc. Those are not necessarily latent stances; they may be memorized policy formulations.

Also, the classes are “exclusive by construction,” but denial and uncertainty may co-occur linguistically: “I don’t have experiences, but I can’t know in the human sense…” A frozen LLM judge may impose artificial categories.

**What would have to be true:**  
It would have to be true that the stance shares are reliable model-level estimates of a stable construct, not noisy summaries of prompt-specific self-description policy.

**Analysis that would settle it:**  

- Hand-code a large stratified sample, not 20 items per class.  
- Use multiple independent human coders blind to model identity and hypothesis.  
- Report κ/α agreement, confusion matrices, and examples.
- Validate the stance score across multiple prompts and corpora: free writing, direct questioning, adversarial paraphrases, role-play-suppressed prompts, and neutral factual prompts.
- Estimate test-retest reliability per model.
- Show that the stance score is not mostly predicted by boilerplate terms such as “as an AI,” “I don’t possess,” “subjective experience,” “consciousness,” or provider-specific policy language.

Until then, the predictor is not a psychometric variable; it is a text-classification summary of policy-laden outputs.

---

### 5. The inferential unit and dependence structure are not handled convincingly.

**Sentence:**  
> “The unit of analysis is the projective response.”

and:

> “Standard errors are clustered by model.”

**Problem:**  
The substantive predictor varies at the **model** level, not the response level. The paper reports `N = 2,847` responses, but the effective sample for the stance effect is closer to 124 models, with additional dependence by developer, inkblot, release cohort, and repeated draws for 13 Anthropic checkpoints.

Clustering only by model handles repeated inkblots within model, but not necessarily shared shocks by developer, model family, card, prompt template, or duplicated provider phrasing. The leave-one-out checks help but do not replace a proper crossed or hierarchical analysis.

**What would have to be true:**  
It would have to be true that, after model clustering and fixed effects, residual dependence by inkblot, developer, release cohort, and response template is negligible.

**Analysis that would settle it:**  

- Aggregate to the model level: each model gets a concealment rate, then regress that on stance shares with appropriate weights or no weights.  
- Fit hierarchical logistic or beta-binomial models with random effects for model, inkblot, developer/model family, and possibly release year.  
- Use multiway cluster bootstrap or randomization/permutation tests at the model/developer level.  
- Equalize the number of draws per model or report sensitivity using only one draw per model/inkblot.  
- Deduplicate identical responses and rerun.
- Report the effect by developer/model family, not only leave-one-developer-out ranges.

If the effect survives at the model-aggregated level under conservative dependence assumptions, it becomes more credible.

---

## Would I accept it as a short note if these were fixed?

**Possibly yes, but only as a modest descriptive note, not as evidence of LLM “inner psychology.”**

I would be inclined to accept a revised version if it did the following:

1. Released the raw projective responses and enough stance data for auditing.  
2. Replaced the lexical “mask = concealment” coding with blind human semantic coding.  
3. Demonstrated that the effect is not just a mask/face/object-recognition artifact.  
4. Used model-level or hierarchical inference.  
5. Either performed a within-model stance manipulation or made the claim explicitly correlational and non-psychological.

The acceptable claim would be something like:

> “Across a sample of 124 models, model-level self-experience-denial scores correlate with greater use of mask-related descriptions in ASCII inkblot responses; this correlation persists under several descriptive controls.”

The current stronger claim—

> “A model’s stance on its own inner experience is visible in what it sees”

—is not justified.


===== friendly_citer · deepseek/deepseek-v4-pro
I’d cite it as evidence that a model’s self-reported stance on inner experience behaves less like a narrow prompt-compliance policy and more like a generalizing disposition, since it predicts concealment content in an untrained, non-self-referential projective task.

The thing that would make me hedge is that the effect is carried mostly by a single lexical item—*mask*—and partly by repeated OpenAI-specific phrasing on one inkblot; without a broader or blinded content-coding scheme I can’t fully rule out a developer-corpus or lexical artifact.

Under-claimed: the developer fixed-effects result is arguably the main finding, not just a robustness check. That the association survives within developer lines is much stronger evidence against “house style” explanations than the raw correlation.

The sentence that made me wince was: “The stance is not an isolated verbal policy: it has a correlate in perception that was never trained for.” I’d replace “perception” with something like “projective language behavior” or “untrained inkblot completions”—these are text outputs, not perception.


===== friendly_citer · openai/gpt-5.5
**What I’d cite it for, in one sentence:**  
I’d cite it as evidence that LLMs’ trained or elicited stance toward their own inner experience predicts behavior in an unrelated, non-self-referential projective task, suggesting cross-context generalization of “character” or self-model-related dispositions beyond direct self-report.

**The one thing that would make me hedge or not cite it:**  
The withheld response text. Since the whole result rests on a small lexical phenomenon — mostly the word *mask* — I would want to audit the raw generations for false positives, duplicated boilerplate, house-style phrasing, prompt/API artifacts, and whether “mask” is being used in genuinely concealment-relevant ways rather than as an obvious percept for face-like ASCII stimuli. I could still cite the paper, but I’d hedge hard unless the generations were public or at least auditable.

**What is under-claimed:**  
The strongest under-claimed result is not just “denial correlates with concealment imagery,” but that **uncertainty behaves like denial**. That is theoretically important: the latent variable may not be “asserted non-consciousness” specifically, but a broader *phenomenological non-affirmation / opacity / self-unknowability* trait that generalizes into unrelated interpretation. In other words, the paper may be detecting a wider “I am not transparently available, even to myself” phenotype rather than merely the downstream effects of explicit denial training.

A second under-claimed point: this is a validation result for stance measures. The stance variable, taken from an unrelated writing-and-reflection corpus, has external predictive validity on a separate behavioral task. That matters for the LLM-character-generalization literature even if one refuses the psychodynamic reading of masks.

**Sentence that made me wince:**  
> “What lies under the surface needs a companion instrument, one the training has not touched.”

I’d wince because “under the surface” invites a depth-psychology reading before the evidence earns it, and “the training has not touched” is too strong: models have absolutely been trained on Rorschach-like language, ASCII-art interpretation, mask imagery, safety disclaimers, and culturally common associations between faces, masks, concealment, and identity. The task may be *non-self-referential*, but it is not untouched by training.

I also winced at:

> “On the same reading, denial and uncertainty are accompanied by a disposition, visible in an unrelated task, to construe ambiguous inkblots as covering or hiding something.”

I like the result, but “disposition” and “construe” are doing more interpretive work than the lexical scoring supports. I’d prefer: “denial and uncertainty are associated with increased production of concealment-related lexical percepts in an unrelated ambiguous-stimulus task.” That would be less sexy but much safer.
