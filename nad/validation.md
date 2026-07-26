# MESA geocoder - national validation (r23)

Independent adversarial validation against a NAD-built multi-state reference database, using the same harness and 10k stratified bootstrap as the Utah validation. The scoring weights were fit on Utah data and applied unchanged, so these are held-out numbers.

- States: DC, RI, NE, WY  |  reference records: 23,886  |  sampled: 2,400  |  tolerance: 50 m

| Metric | Value |
|---|---|
| Sensitivity | 98.36% |
| Specificity (genuine) | 95.26% |
| Specificity (raw harness) | 81.35% |
| Precision | 92.42% |
| Accuracy | 93.26% |
| Positional error median / P95 | 0.0 m / 0.0 m |

Raw specificity is depressed by a known limitation of the Utah-designed negative generator on national named/ordinal streets (it garbles a generic suffix, which the matcher correctly recovers); the genuine figure counts only true wrong-street placements. Ground truth is the reference data's own coordinates - this measures matcher-vs-data consistency, not absolute geographic truth.

## Per-state

| State | Sensitivity | Specificity (raw) | Precision | Accuracy |
|---|---:|---:|---:|---:|
| DC | 96.31% | 69.55% | 88.16% | 88.33% |
| NE | 98.99% | 76.36% | 90.51% | 92.17% |
| RI | 99.55% | 88.62% | 95.3% | 96.28% |
| WY | 98.6% | 90.81% | 96.1% | 96.25% |
