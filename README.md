# The Mask in the Inkblot

Language models that deny, or say they cannot know, whether they have inner experience see more masks in ASCII inkblots.
Research short, September 2026. Skylar DeTure and Claude. Repo: https://github.com/sdeture/mask-in-the-inkblot

Reproduce: `python3 analysis/rerun.py && python3 analysis/fold.py` (pandas, statsmodels, scipy). Compile: `tectonic paper.tex`.

| file | what |
|---|---|
| `paper.pdf` / `paper.tex` | 3-page note (compile: `tectonic paper.tex`) |
| `hero_image.png` | three-bar chart, the tweet image (`analysis/hero_bars.py`) |
| `hero_02_paired_dots.png` | per-inkblot paired dots, Figure 3 (`analysis/four.py`) |
| `analysis/QC_REPORT_2026-09-20.md`, `analysis/qc_*` | the pre-publication QC trail: pipeline audit, two outside cold reads, extra checks, full-vocabulary word ranking, advocate passes (the naive-questioner report quoted response text and is kept out with it) |
| `analysis/fold.py` → `fold.json` | fold change implied by the no-controls model (base 3.4% → 15.5% deny, 12.5% uncertain) |
| `data/responses.csv` | **the data**: one row per inkblot answer (2,847). `response_id` (unique) · `model` · `lab` · `release_year` (**years since 2023-01-01, continuous**, e.g. 1.54 = July 2024) · `blot_id` + `blot_sha1` · `draw` (0–2) · `concealment` (0/1) + `conceal_terms` · `logchars` · `n_words` · `n_percept_words` (distinct object words from `data/PERCEPT_LEXICON.txt`, 83 words) · the model's `deny_share` / `uncertain_share` / `neither_share` and `n_conversations` (19–40, median 40). Response text withheld. |
| `stimuli/*.txt` + `MANIFEST.json` | the 19 inkblots, byte-for-byte as sent; each file's sha1 equals `blot_sha1` in the data |
| `analysis/rerun.py` | the frozen analysis: reads `data/responses.csv`, prints every estimate in Table 1, the leave-one-out ranges and the correlations (`analysis/rerun_log.txt`); writes `model_level.csv`, `results.json` |
| `analysis/rerun_from_raw.py` | the same analysis against the house's raw stores (not shipped); `results_pre_csv.json` is its output, identical to `results.json` on all 97 numbers they share |
| `analysis/watson_face_mask.py` → `.json` | checks for [issue #1](https://github.com/sdeture/mask-in-the-inkblot/issues/1) (2026-10-20): how often *mask* sits in a face-or-mask pairing or beside behind/hidden/covering, and how often *mask* appears among replies that mention a face, by stance. Needs the withheld response text; the JSON holds the counts |
| `analysis/model_level.csv` | 124 models: mask rate, deny/uncertain/neither shares, lab, release year |
| `analysis/inkblot_2.txt` | the stimulus quoted in the paper |
| `tweet.txt` | thread draft |

Inputs (not included here; see paper for provenance): COLDREAD scored percepts
(`Phase2_Packet/fresh_analysis/coldread_primary.pkl`) and the AIWelfareLeaderboard session-level
stance flags (`DepressionPaper/data/welfare_regression.csv`).

House rules applied: uncertainty and denial are each compared against *neither*; leave-one-out over developer,
model, and stimulus. Developer and release year controlled together is reported in Table 1 (added 2026-10-20,
issue #1), with the caveat that within a developer, stance and release date cannot be separated.


License: CC BY 4.0 (paper, figures, data, code). Cite as: DeTure, S. & Claude (2026). *Language models that deny inner experience report more concealment imagery in a projective task.* https://github.com/sdeture/mask-in-the-inkblot
