# MESA geocoder - national validation (r23)

Independent adversarial validation against a NAD-built multi-state reference database, using the same harness and 10k stratified bootstrap as the Utah validation. The scoring weights were fit on Utah data and applied unchanged, so these are held-out numbers.

- States: AK, CT, DC, DE, NE, RI, WI, WY  |  reference records: 63,458  |  sampled: 6,400  |  tolerance: 50 m

| Metric | Value |
|---|---|
| Sensitivity | 98.82% |
| Specificity (genuine) | 94.99% |
| Specificity (raw harness) | 84.64% |
| Precision | 93.76% |
| Accuracy | 94.59% |
| Positional error median / P95 | 0.0 m / 0.0 m |

Raw specificity is depressed by a known limitation of the Utah-designed negative generator on national named/ordinal streets (it garbles a generic suffix, which the matcher correctly recovers); the genuine figure counts only true wrong-street placements. Ground truth is the reference data's own coordinates - this measures matcher-vs-data consistency, not absolute geographic truth.

## Per-state

| State | Sensitivity | Specificity (raw) | Precision | Accuracy |
|---|---:|---:|---:|---:|
| AK | 99.53% | 91.66% | 96.45% | 97.17% |
| CT | 99.09% | 81.35% | 92.79% | 93.95% |
| DC | 96.52% | 71.19% | 88.65% | 88.92% |
| DE | 99.46% | 92.81% | 96.98% | 97.48% |
| NE | 98.99% | 78.03% | 91.11% | 92.67% |
| RI | 99.61% | 85.09% | 94.27% | 95.42% |
| WI | 99.07% | 88.22% | 95.06% | 95.77% |
| WY | 98.31% | 88.72% | 95.27% | 95.42% |
