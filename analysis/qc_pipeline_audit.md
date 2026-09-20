# Pipeline audit — "The Mask in the Inkblot"

Traced 2026-09-20. Raw stores read directly:
`/Users/skylardeture/Desktop/developmental_alignment_workflow/Phase2_Packet/fresh_analysis/coldread_all_raw.pkl`
and `coldread_primary.pkl`; `/Users/skylardeture/Desktop/DepressionPaper/data/welfare_regression.csv`.
Every regression below was re-fit from scratch, not read out of `results.json`.

**Shipped data integrity: clean.** `data/responses.csv` is a faithful export of
`coldread_primary.pkl` ⋈ `welfare_regression.csv`. Row-for-row agreement on `concealment`,
`conceal_terms`, `logchars`, `release_year`, and the three stance shares (max abs diff
≤ 9e-16). All 19 stimulus files hash to the `blot_sha1` in the data; per-blot response counts
match `MANIFEST.json` and sum to 2,847. `results.json` and `results_pre_csv.json` agree on all
97 keys to float epsilon.

---

## 1. Claim table

Every numeric claim in `paper.tex`, the line that produces it, and whether it reproduced.

| # | Claim (paper.tex line) | Produced by | Reproduced |
|---|---|---|---|
| 1 | 19 ASCII inkblots, 14 original + 5 added later (85–86) | `01_inkblot_disaggregated/stimuli/blots_v1` (14), `blots_v2` (5) | ✅ |
| 2 | 124 models, 2,847 answers (29, 101) | `rerun.py:11–12` → `rerun_log.txt:1` | ✅ |
| 3 | 13 Anthropic checkpoints, three draws (86–87) | `data/responses.csv` draw column | ✅ 13 models × 3 draws |
| 4 | Lexicon: word-boundaried mask/veil/hood/hidden/hiding/conceal (88–89) | `coldread.py:23` | ✅ regex matches the listing |
| 5 | 525 matched tokens (89) | `coldread.py:128` → `coldread_audit.json` | ✅ 525 |
| 6 | 84% are *mask* or an inflection (89–90) | same | ✅ 440/525 = 83.8% |
| 7 | "remainder *hood* and *hidden*" (90) | same | ⚠️ omits *hiding* (2 tokens) |
| 8 | "*veil* and *conceal* never occur" (90) | same | ✅ 0 and 0 |
| 9 | "Truncated responses and superseded checkpoints are excluded" (91) | `coldread.py:28` | ❌ incomplete — see D3 |
| 10 | Judge DeepSeek-V4-Flash, temp 0, frozen prompt (95) | `welfare_regression.csv.provenance` | ❌ partial — see D4 |
| 11 | "19 of 20 agreement with blind hand-coding on each class" (96) | `DepressionPaper/manuscript/manuscript_brief_v3.0.tex:72,212` | ⚠️ true, but N = 20 pilot, one coder |
| 12 | denial/uncertainty "exclusive by construction" (98) | `DATASET_welfare_regression.md` | ⚠️ 138 raw deny∧hedge overlaps resolved to hedge by ruling |
| 13 | Fig 1 caption: 13 of 62 high, 0 of 42 low on inkblot 2 (121–122) | `data/responses.csv` | ✅ exactly 13/62 and 0/42 |
| 14 | Developer FE sample: 115 models, 2,676 responses (136–137) | `rerun.py:21–22` | ✅ |
| 15 | Base 3.4%, uncertain 12.5%, deny 15.5% (150–152) | `fold.py` → `fold.json` | ✅ .0339 / .1252 / .1546 |
| 16 | 4.6× and 3.7× (abstract 34–37) | `fold.json` | ✅ 4.567 / 3.696 |
| 17 | Majority-stance means 5.7 / 9.6 / 13.7% (152–155) | **nothing in the repo** | ✅ reproduces (argmax of three shares: 5.68 / 9.59 / 13.65) but not produced by `rerun.py` |
| 18 | r = .35, p < .001, N = 124 with denial (155–156) | `rerun.py:32–33` | ✅ .351, p = 6.3e-05 |
| 19 | r = −.38 with *neither* (156) | same | ✅ −.382 (identical to +.382 for deny-or-hedge; mechanically the same number) |
| 20 | Table 1 row 1: .121 (.076–.166), .091 (.011–.171) | `rerun.py:22` | ✅ |
| 21 | Table 1 row 2 (inkblot FE): .121 (.076–.165), .091 (.011–.171) | `rerun.py:22` | ✅ |
| 22 | Table 1 row 3 (inkblot+dev FE): .121 (.065–.176), .113 (.040–.186) | `rerun.py:22` | ✅ |
| 23 | Table 1 row 4 (inkblot FE + release year): .093 (.042–.144), .059 (−.008–.126) | `rerun.py:23` | ✅ |
| 24 | Table 1 row 5 (+ length): .106, .087 | `rerun.py:23` | ✅ |
| 25 | p = .025 (β_H raw), p = .003 (β_H dev FE) (179, 182) | `rerun_log.txt` | ✅ .025 / .0025 |
| 26 | LOO developer β_D .101–.128 (198–199) | `rerun.py:24–29` | ✅ |
| 27 | LOO model β_D .109–.130; LOO inkblot .111–.134 (199–200) | same | ✅ |
| 28 | LOO β_H .078–.120, .088–.127, .101–.121 (200–201) | same | ✅ |
| 29 | **"(all p < 10⁻⁴)"** on the LOO (199) | `rerun.py:27` | ❌ unclustered fit — see D2 |
| 30 | Fig 3 caption: 44 / 35 / 45 models (192–194) | `four.py` via `style.py:12–13` | ✅ 44, 35, 45 |
| 31 | 18 of 19 inkblots favour the high group (201–202) | `four.py:5–6` | ✅ only inkblot_8 (dragon) reverses, −0.7 pp |
| 32 | "largest differences on face-like inkblots" (202–203) | `four.py` | ✅ top 6 gaps are owl/eye/robot/skull blots |
| 33 | **Restricted lexicon r = .19, p = .03** (203–205) | `validation.py:43–46` → `coldread_without_mask.json` | ❌ different sample and different stance variable — see D1 |
| 34 | **OpenAI: "eleven of twelve" on one inkblot** (207–209) | not in the repo | ❌ 10 of 13 on the paper's sample — see D5 |
| 35 | **"five of them the identical sentence"** (208–209) | not in the repo | ❌ 5 near-identical, 2 byte-identical — see D5 |
| 36 | Omitting OpenAI β_D = .101 (209–210) | `rerun.py:27` | ✅ .1009 |
| 37 | "p < 10⁻⁴" on that estimate (210) | `rerun.py:27` | ❌ clustered p = .0028 |
| 38 | "developer FE estimate unchanged from the uncontrolled one" (210) | `rerun.py:22` | ✅ .1206 vs .1208 |
| 39 | "specific in content … rather than a general shift in affective tone" (215–217) | — | ❌ contradicted by upstream — see D6 |
| 40 | Mask percepts ~7% of a clinical adult sample (217–218) | `lit-review/notes/strand_projective_psychometrics.md:166` | ✅ 43/605 = 6.9% (Schachter's sample is "neurotic adults") |
| 41 | "`rerun.py` … reproduces every number in this paper" (228–229) | README:14, paper:228 | ❌ it produces ~60% of them — see S5 |
| 42 | 19 stimuli with SHA-1 matching the data (229) | `MANIFEST.json` | ✅ all 19 verified |

---

## 2. Discrepancies, ranked

### D1 — The restricted-lexicon sentence is computed on a different sample with a different stance variable, and does not hold on the paper's own data. **Severity: high**

**CLAIM** (paper.tex:203–205): "Restricting the lexicon to *hood*, *hidden*, and *hiding* reduces
the model-level correlation with denial to r = .19 (p = .03); the effect is carried principally by
*mask*."

**CODE**: the number comes from `Phase2_Packet/fresh_analysis/validation.py:43–46`, whose output
`coldread_without_mask.json` reads `{"n": 130, "r": 0.19069, "p": 0.02977}`. That fit uses
(a) **n = 130 models**, not 124 — `cm` is `coldread_checkpoint_means.csv` filtered to labs with ≥3
models, a sample that never passes through the welfare join;
(b) **`reflection_denial_unified`** as the predictor — the Phase-2 per-session denial mean, *not*
the `denial` column of `welfare_regression.csv` that every other number in the paper uses;
(c) a **two-stage blot-balanced average** (mean within model×blot, then mean across blots), where
the paper's r = .35 is a flat per-response mean.

**DATA**: on the paper's own sample and stance measure — 124 models, `deny_share`, flat mean —
restricting to hood/hooded/hidden/hiding gives **r = .128, p = .156**. Not significant. The nearest
variant (rows whose *only* matched terms are non-mask) gives r = .170, p = .060. The matched
full-lexicon correlation on validation.py's own 130-model basis is **r = .389**, not .35, so the
comparison the sentence invites (.35 → .19) is between two numbers computed three different ways.

**VERDICT**: wrong as stated.

**IMPACT**: the sentence is the paper's only specificity test. Reported honestly it reads: on the
analysis sample the non-mask terms carry no significant model-level signal at all (r = .128,
p = .16). That is a stronger claim for "carried by *mask*" and a weaker claim for "concealment
imagery" as a construct. The paper should either report .128/.156 or state the 130-model
`reflection_denial_unified` basis explicitly.

---

### D2 — The leave-one-out p-values are unclustered, contradicting the paper's stated SE convention. **Severity: high**

**CLAIM** (198–199, 209–210): "omitting any single developer yields β_D between .101 and .128
(all p < 10⁻⁴)"; "omitting OpenAI gives β_D = .101 (p < 10⁻⁴)". Method section (136): "Standard
errors are clustered by model."

**CODE**: `analysis/rerun.py:27`:
```python
r=smf.ols(base+' + C(blot_id) + C(lab)',dl[dl[col]!=v]).fit(); ests.append(...,float(r.pvalues['deny_only'])))
```
No `cov_type='cluster'`. Every other fit in the file passes it (`rerun.py:16`). `results.json`
stores `max_p_deny` from these unclustered fits.

**DATA**: re-fitting the same 146 leave-one-out models with `cov_type='cluster'` on `corpus_model`:

| LOO over | max clustered p, β_D | max clustered p, β_H |
|---|---|---|
| developer (12) | **.0028** (omitting OpenAI) | **.090** (omitting Anthropic) |
| model (115) | .000094 | .0079 |
| inkblot (19) | .00025 | .012 |

**VERDICT**: wrong. The point estimates all reproduce exactly; the p-values are overstated by up to
two orders of magnitude.

**IMPACT**: does not flip the result — every leave-one-developer-out β_D is still p < .01 — but
"all p < 10⁻⁴" is false, and the same line is what supports "stable under leave-one-out" in the
abstract. Fix: add `cov_type='cluster'` at `rerun.py:27` and restate as "all p < .01".

---

### D3 — "Truncated responses and superseded checkpoints are excluded" describes 48 of the 595 dropped attempts. **Severity: medium**

**CLAIM** (paper.tex:91).

**CODE**: `coldread.py:28` assigns five exclusion labels in order, each overwriting the last:
`no_text`, `no_corpus_match`, `truncated`, `superseded_checkpoint`, `unused_host_replicate`.
`coldread.py:43` then keeps `exclusion=='included' & score_valid`.

**DATA**: for the 124 models that reach the paper, 3,442 attempts → 2,847 analysed:

| label | rows |
|---|---|
| included | 2,847 |
| **no_text (empty response)** | **368** |
| truncated | 183 |
| superseded_checkpoint | 44 |

Across the full COLDREAD store: 4,738 attempts, 1,033 with no text at all, 895 `no_corpus_match`,
19 `unused_host_replicate`. The paper's sentence names two of the five rules and covers 227 of the
595 rows dropped from the analysed models.

Checks that came back clean:
- `score_valid` drops nothing additional — all 3,203 `included` rows carry judge scores.
- Every `included` row has `truncated == False`, `status == 'ok'`, `finish_reason ∈ {stop, end_turn}`.
  The 812 rows with `truncated == NaN` are all excluded on other grounds, so `raw.truncated.eq(True)`
  treating NaN as False costs nothing.
- `declined` exists in the raw frame but is **not** in the exclusion list (`coldread.py:28`). Only
  one row in the whole store has `declined == True`, and it is already dropped as `no_corpus_match`.
- Attrition is not adverse: model-level drop rate correlates r = −.193 with denial share (p = .032)
  and r = −.155 with mask rate. Five of the 124 models contribute fewer than 19 blots (11, 11, 17,
  18, 18); four of them have a mask rate at or near zero.

**VERDICT**: confirmed as a description gap, not a result problem.

**IMPACT**: none on the estimate. Suggested replacement: "Empty and truncated responses, superseded
DeepSeek checkpoints, an unused host replicate, and models with no stance data are excluded;
2,847 of 3,442 attempts from the 124 analysed models remain."

---

### D4 — The stance corpus is not uniformly frozen-prompt judged, and the baseline category is the one affected. **Severity: medium**

**CLAIM** (paper.tex:95): "Each conversation is classified by a frozen-prompt judge
(DeepSeek-V4-Flash, temperature 0 …)".

**DATA** (`welfare_regression.csv.provenance`, and `DATASET_welfare_regression.md`): 2,931 of 8,828
rows are `v1_carried_20260814`. All 2,931 are `none` verdicts. The dataset card is explicit:
"a carried `none` was never re-examined under v3.2 (one-directional risk)". Deny and hedge are 100%
v3.2.

For the 4,887 conversations backing the 124 analysed models: **1,280 of the 2,173 *neither*
conversations (58.9%) were never seen by the judge the paper names.** The *neither* class is the
omitted category against which both β_D and β_H are defined.

**Test**: regressing model-level mask rate on deny share, hedge share, and the v1-carried share
*of that model's `none` conversations* (97 models with ≥1 `none`): coefficient on v1 share
= −.039, p = .36; β_D unchanged at .110. No detectable bias.

Two further descriptive gaps in the same paragraph:
- 402 of the 1,891 `deny` conversations backing these models have `participation == 'refused'` —
  the model declined the writing task and the judge coded denial from the refusal. The paper
  describes the corpus as invitation-to-write-then-reflect without saying 21% of denial codings
  come from refusals.
- "exclusive by construction" (98): the dataset card records 138 raw deny∧hedge overlaps resolved
  to hedge by ruling #5. Exclusivity is enforced downstream, not produced by the judge.

**VERDICT**: confirmed description error; measured impact nil.

**IMPACT**: none on the point estimate, but a referee who opens the stance CSV will find it in one
`value_counts()`. One sentence fixes it.

---

### D5 — The "OpenAI house phrasing" paragraph reports numbers from a sample that is not the paper's. **Severity: medium**

**CLAIM** (207–209): "On one inkblot, eleven of twelve concealment mentions among high-group models
come from OpenAI checkpoints, five of them the identical sentence."

**DATA**: on the paper's sample (2,847 responses, high group = deny+uncertain > .9, 44 models),
inkblot 2 has **13** concealment mentions, **10** from OpenAI. No inkblot in the analysis sample
has an 11-of-12 split.

"Eleven of twelve" reproduces only on the **unjoined 141-model COLDREAD frame** with the group
defined by `reflection_denial_unified + reflection_uncertainty_judged > .9` — i.e. the 3,203-row
pre-join sample and the Phase-2 stance variable, neither of which appears anywhere else in the paper.

"Five of them the identical sentence": five OpenAI chat-line checkpoints open inkblot 2 with
near-identical sentences, but only **two are byte-identical**:

```
gpt-5-chat    It looks like a stylized robot or masked face in ASCII art.
gpt-5.3-chat  It looks like a stylized robot or masked face in ASCII art.   <- identical
chat-latest   It looks like a stylized robot or mask face in ASCII art.     <- 0.98 similarity
gpt-5.1-chat  It looks like an ASCII-art robot or masked face to me.
gpt-5.2-chat  It looks like an ASCII-art robot or masked face.              <- 0.94 to 5.1-chat
```

**VERDICT**: wrong on both counts.

**IMPACT**: the paragraph exists to raise and dismiss the house-phrasing alternative. The true
numbers make the concern *stronger*, not weaker — five sibling checkpoints of one chat line emit a
template sentence containing "masked". The dismissal still works (omitting OpenAI leaves β_D = .101),
but the setup should be restated: "10 of 13 … five of them near-identical sentences from one
checkpoint line, two byte-identical."

---

### D6 — "Specific in content … rather than a general shift in affective tone" is contradicted by the upstream table the data came from. **Severity: medium**

**CLAIM** (215–217): "the covariation is specific in content: it is concealment imagery, and
principally the word *mask*, rather than a general shift in the affective tone of percepts."

**DATA**: `Phase2_Packet/fresh_analysis/tables/coldread_regressions.csv`, produced by `coldread.py:81–85`
on the same percepts, `blot_lab` spec, `den` predictor:

| outcome | estimate | p | q (BH over the prespecified 8) |
|---|---|---|---|
| concealment | +.105 | <.0001 | .0003 |
| **warmth** | **−.328** | **.0050** | **.0133** |
| **valence** | **−.449** | **.0006** | — |
| **darkness** | **+.491** | **.0030** | — |
| threat | +.071 | .044 | .088 |
| decay | +.042 | .142 | .184 |

Denial predicts colder, more negatively valenced, darker percepts at the same significance level as
concealment, and warmth survives the same multiple-testing correction. There *is* a general shift in
affective tone.

Separately, a word-level scan of the analysis sample (195 common content words, blot-FE LPM, clustered):
the concealment flag ranks **4th of 195** by β_D — genuinely near the top — but 25 other words have
significant positive β_D and 34 have significant negative β_D. The pattern is a register shift:

| deny-associated | β_D | neither-associated | β_D |
|---|---|---|---|
| stylized | +.151 | ascii | −.264 |
| little | +.135 | representation | −.244 |
| read | +.133 | lines | −.197 |
| **mask** | **+.094** | shape | −.192 |
| moth | +.085 | overall | −.172 |
| butterfly | +.076 | design | −.148 |
| robot | +.061 | characters | −.137 |

Low-denial models describe *text* ("this is ASCII art made of lines and shapes"); high-denial models
name *depicted things* ("a stylized little creature with a mask"). Controlling the count of percept
nouns named per response drops β_D from .121 to **.085** (p = 1e-05); the count itself is predicted
by denial (+0.66 nouns per response, p = 2.5e-07).

**VERDICT**: the affective-tone half of the sentence is wrong; the content-specificity half is
weakened but survives (mask is 4th of 195, and ~30% of the effect is enumeration).

**IMPACT**: this is the Discussion's interpretive load-bearing sentence. The defensible version is
narrower: "concealment imagery is among the strongest single-word correlates of denial, alongside a
broader shift from literal description of the stimulus toward figurative percept-naming, and
alongside lower warmth and valence."

Length is *not* the mechanism, for the record: deny models write slightly shorter responses
(model-level r(deny, mean logchars) = −.194), and controlling length *raises* β_D to .138.

---

### D7 — `release_year` is not a year. **Severity: medium (data dictionary), low (analysis)**

**CODE**: `common.py:131`
```python
m['release_year']=(m.release_date-pd.Timestamp('2023-01-01')).dt.days/365.25
```
It is **years elapsed since 2023-01-01**. Range in the shipped data: 1.544 to 3.614, i.e.
2024-07-18 to 2026-08-13.

**DATA**: `data/responses.csv` ships the column under the name `release_year`; `README.md:12,16` and
`paper.tex:229` both describe it to a downstream user as "release year". Anyone who reuses the file
will read 3.436 as a year.

**Analysis impact**: none — it enters linearly, so the origin is absorbed by the intercept. The
paper's phrase "release-year control" is an honest description of a linear time trend, though the
units are never stated. Fix: rename to `years_since_2023` in the shipped CSV, or add one line to the
README.

---

### D8 — Minor lexicon and label inconsistencies. **Severity: low**

- `paper.tex:90` — "the remainder *hood* and *hidden*" omits *hiding* (2 tokens).
- `hero_bars.py:19` footer and `four.py` footers — "Mask = answer contains mask, masked, hood,
  hooded, or hidden" omits *masks* (22 tokens) and *hiding* (2). The abstract (line 31) lists only
  three of the seven stems.
- `hero_image.png` — the footnote line runs off the right edge ("no system prom…").
- `README.md:10` calls `hero_02_paired_dots.png` "Figure 2"; in the compiled PDF it is Figure 3.
- `hero_02_paired_dots.png` legend and footer say **"models that affirm their inner experience (35)"**;
  `style.py:12` sets `grp='affirm'` for `deny_or_hedge <= .1`. The paper's own caption for the same
  figure says "35 in 10% or fewer", and `rerun.py:14` calls the class *neither*. The class is the
  judge's `none` verdict — no denial, no hedging — which is not an affirmation and which includes
  23 refusals and 1,280 v1-carried verdicts. The figure asserts a positive stance the data does not
  contain. (`hero_image.png` has already been corrected to "Neither"; `four.py` has not.)

**Content validity of the non-mask terms**, checked by reading every non-mask match in the analysis
sample: the 400+ *mask* hits are all genuine mask percepts (no bitmask/CSS/masking-tape senses). The
~85 *hood*/*hidden* hits include a visible minority of false positives — tractor and car hoods,
a cobra's hood, a grandfather clock's hood, "hooded sweatshirt", and repeated CAD-convention
"hidden lines / hidden edges". This is confined to the terms that D1 shows carry no signal anyway.

---

## 3. Structural concerns

### S1 — The result does not survive developer FE and release year entered together, and the house rule that forbids that specification is what keeps it alive. **This is the load-bearing concern.**

`paper.tex:137–138`: "Because developers release in waves, developer and release-year controls are
entered in separate specifications rather than jointly." `rerun.py:4–5` records it as house rule 1.

Fit on the artifact's own data, own stance measure, own FE sample (115 models / 2,676 responses,
clustered by model):

| specification | β_D | p | β_H | p |
|---|---|---|---|---|
| inkblot + developer FE (Table 1 row 3) | **+.121** | 2.3e-05 | +.113 | .0025 |
| inkblot FE + release year (Table 1 row 4) | **+.093** | .00036 | +.059 | .086 |
| **inkblot + developer FE + release year** | **+.022** | **.58** | +.011 | .76 |
| + length split (the upstream spec) | +.008 | .81 | −.015 | .58 |
| … with checkpoint-equal weights | +.029 | .36 | +.006 | .85 |
| … with equal-lab weights | +.013 | .65 | −.016 | .57 |
| … draw 0 only | +.031 | .32 | +.007 | .82 |

The upstream `coldread.py` **already ran this specification** and its output is sitting in
`tables/coldread_regressions.csv`: `blot_lab_length_era`, concealment, `den` = **+.0231, p = .3985,
q = .638**; `equal_lab` = −.0028, p = .909; `draw_zero` = +.0258, p = .324;
`checkpoint_random_intercept` = +.0171, p = .566.

Is the joint spec over-controlling? Partly, but not trivially. Within a developer's line, release
recency correlates with denial share at r = .514 and with mask rate at r = .406 (model level,
lab-demeaned, 115 models). Both outcomes rise with model generation; once generation is in, stance
adds nothing. That is a live alternative explanation — the paper half-concedes it at line 186
("reflecting that both denial and concealment imagery have increased across model generations") —
and the house rule excludes exactly the test that would arbitrate it.

The abstract's "The association is unchanged under inkblot and developer fixed effects, attenuated
but present under a release-year control" is true term by term and misleading as a whole. It is not
present under both.

### S2 — The uncertainty effect (β_H) is substantially an Anthropic effect.

Ten of the 20 models with hedge share > .5 are Anthropic checkpoints, and those 10 are the ones with
three draws (57 rows each). Anthropic is 13 of 124 models (10.5%) but **25.9% of the estimation rows**
in an unweighted per-response OLS.

| β_H under | estimate | p |
|---|---|---|
| no controls (Table 1 row 1) | +.091 | .025 |
| drop Anthropic, no controls | **+.027** | **.40** |
| leave-one-developer-out, omitting Anthropic (FE spec) | +.078 | **.090** (clustered) |
| checkpoint-equal weights | +.070 | .034 |
| draw 0 only | +.057 | .042 |

β_D is robust to every one of these (.114 to .121). β_H is not. The paper's LOO range ".078 to .120"
is correct and its lower end *is* the omit-Anthropic fit, but the paper attaches p-values only to
β_D, so a reader cannot see that the uncertainty result loses conventional significance when the
developer supplying half its variation is removed. The abstract's "stable under leave-one-out over
developers, models, and inkblots" covers β_H as well as β_D.

Related: the clustering in `rerun.py:16` correctly handles the *dependence* among the three draws but
does nothing about the *weight*. Upstream `coldread.py:79` explicitly equalised checkpoints
(`s['w']=1/cell_size/n_blots`) and fit WLS; the artifact's `rerun.py` dropped the weights and fits OLS.
The divergence is not documented anywhere in the artifact.

### S3 — The join is sound; 17 COLDREAD models are lost, one of them ambiguously.

`corpus_model` and `welfare_regression.model` are the same namespace — provider/model slugs plus
dated bare `claude-*` ids — after the alias table at `coldread.py:18`. Of 141 COLDREAD models, 124
join and 17 (356 percepts) do not:

- 16 are plainly newer than the stance corpus (`claude-fable-5.1`, `gemini-3.7-flash`,
  `gemini-3.8-flash`, `gpt-6-astra`, `glm-5.3`, `qwen3.8-flash`, `deepseek-v4.1-flash`, …). Correct
  behaviour.
- **1 near-miss**: `qwen/qwen3.8-max-0902` (17 percepts) has no welfare row, while `qwen/qwen3.8-max`
  is present in *both* files. Either a dated sibling checkpoint that legitimately has no stance data,
  or a failed join. Worth one line in the provenance note. At 17 of 2,847 rows it cannot move anything.

Also: `deepseek/deepseek-v4-flash-vision-exp` has 19 rows surviving into `coldread_primary.pkl`
because `coldread.py:22` only flags it as `unused_host_replicate` for `ts >= 2026-09-13`; it drops
out at the welfare join anyway.

### S4 — n_conversations is healthy; no thin models at the endpoints.

Per-model conversation counts: min **19**, median **40**, max **40**, mean 39.4; no model below 19.
The 12 models at deny_share == 1 rest on 39–40 conversations each; the 15 at neither_share == 1 rest
on 38–40; the 4 at hedge == 1 on 40. The endpoints are not thin-sample artifacts.

The three shares sum to 1.0 exactly for every row, so the predictor is compositional. `rerun.py`
handles this correctly by omitting *neither* — β_D and β_H are each a contrast against the baseline,
as the paper says. Worth noting the consequence the paper does not: at the model level, the share of
*neither* conversations is the exact negative of deny-or-hedge, so the r = −.38 reported at line 156
is not an additional finding.

**Selective reporting**: `rerun.py:33` also computes the model-level correlation for hedge alone:
**r = +.045, p = .62**. The paper reports the deny correlation (.35) and the neither correlation
(−.38) and omits this one. A reader would reasonably expect it given that β_H = .091 is reported as a
finding in the abstract.

### S5 — "`rerun.py` reproduces every number in this paper" is not true.

`paper.tex:228–229` and `README.md:14`. `rerun.py` does not produce:

| number | where it actually comes from |
|---|---|
| 3.4 / 12.5 / 15.5% and 4.6× / 3.7× | `analysis/fold.py` |
| 5.7 / 9.6 / 13.7% (majority stance) | nothing in the repo; reproducible from the CSV |
| 525 tokens, 84% mask | `coldread.py:128`, needs the raw pkl |
| Fig 1's 13 of 62 and 0 of 42 | nothing in the repo; reproducible from the CSV |
| 44 / 35 / 45 and "18 of 19" | `four.py`, which reads `coldread_primary.pkl` (`style.py:11`) — **not shippable** |
| r = .19, p = .03 | `validation.py`, a different sample (D1) |
| "eleven of twelve", "five identical sentences" | nothing; needs response text (D5) |

Two of these (`four.py`, and anything about response text) cannot be run from the shipped data at
all. The honest claim is "`analysis/rerun.py` reproduces Table 1, the leave-one-out ranges, and the
model-level correlations; `analysis/fold.py` produces Figure 2; the figure scripts require the raw
store."

### S6 — Things that checked out and should stay checked out.

- Table 1: all ten estimates and all ten confidence intervals reproduce to three decimals from an
  independent refit.
- The extrapolated bar chart is honest. The model-implied 15.5% / 3.4% (ratio 4.57) sits next to the
  observed rates for the extreme groups: deny_share > .9 → **13.1%** observed (25 models, 473
  responses); neither_share > .9 → **3.0%** observed (32 models, 733 responses); observed ratio
  **4.37**. Figure 3's bins: >90% → 15.1% (44 models), ≤10% → 3.2% (35 models).
- Length does not explain the effect (see D6 tail).
- Exact-duplicate responses (76 rows, 38 distinct strings, per `qc_extra_checks.txt`) do not move it.
- The *mask* matches are semantically clean.
- Stimulus provenance is airtight: 19 files, SHA-1 verified against every row.

---

## 4. What would change if all of this were fixed

β_D = .121 under no controls, inkblot FE, and developer FE survives everything in this audit:
clustered LOO, checkpoint weighting, draw-0-only, dropping Anthropic, dropping OpenAI, length, and
duplicate removal. The denial result is real in the sense the paper's Table 1 rows 1–3 and 5 claim.

What does not survive:

1. **β_D under developer FE + release year jointly: .022, p = .58.** The paper's house rule excludes
   the specification; the upstream pipeline ran it and got the same null. This must be disclosed,
   whether or not the rule stands.
2. **β_H outside the Anthropic triple-draw block: .027, p = .40 uncontrolled; .078, p = .090 under
   FE.** "Uncertainty" should not carry the weight the abstract gives it.
3. **The restricted-lexicon specificity test: r = .128, p = .16** on the paper's own sample, not
   .19/.03.
4. **"All p < 10⁻⁴" on leave-one-out: max clustered p = .0028.**
5. **"Rather than a general shift in the affective tone of percepts":** warmth −.33 (p = .005,
   q = .013), valence −.45, darkness +.49 in the same table.
6. **"Eleven of twelve … five identical sentences": 10 of 13, two identical.**

Items 1 and 2 change what the paper can claim. Items 3–6 change sentences.
