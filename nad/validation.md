# MESA geocoder - national validation (r23)

Independent adversarial validation against a NAD-built multi-state reference database, using the same harness and 10k stratified bootstrap as the Utah validation. The scoring weights were fit on Utah data and applied unchanged, so these are held-out numbers.

- States: AK, CT, DC, DE, MA, MT, NE, NM, RI, WI, WY  |  reference records: 218,740  |  sampled: 22,000  |  tolerance: 50 m

| Metric | Value |
|---|---|
| Sensitivity | 98.66% |
| Specificity (genuine) | 95.17% |
| Specificity (raw harness) | 84.63% |
| Precision | 93.69% |
| Accuracy | 94.45% |
| Positional error median / P95 | 0.0 m / 0.0 m |

Raw specificity is depressed by a known limitation of the Utah-designed negative generator on national named/ordinal streets (it garbles a generic suffix, which the matcher correctly recovers); the genuine figure counts only true wrong-street placements. Ground truth is the reference data's own coordinates - this measures matcher-vs-data consistency, not absolute geographic truth.

## Per-state

| State | Sensitivity | Specificity (raw) | Precision | Accuracy |
|---|---:|---:|---:|---:|
| AK | 99.72% | 90.26% | 95.93% | 96.88% |
| CT | 99.3% | 86.79% | 94.59% | 95.57% |
| DC | 96.23% | 68.88% | 87.94% | 88.08% |
| DE | 99.36% | 91.17% | 96.29% | 96.93% |
| MA | 99.11% | 78.27% | 91.37% | 92.89% |
| MT | 99.04% | 88.51% | 95.25% | 95.88% |
| NE | 99.1% | 79.53% | 91.61% | 93.19% |
| NM | 98.66% | 81.02% | 92.3% | 93.36% |
| RI | 99.51% | 88.26% | 95.24% | 96.17% |
| WI | 99.01% | 88.16% | 95.03% | 95.72% |
| WY | 96.17% | 90.09% | 95.69% | 94.34% |
