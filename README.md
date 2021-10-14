# OULU-NPU metrics

This package implements the metrics (APCER, BPCER, ACER) for face anti-spoofing described at the reference and used in the OULU-NPU dataset (https://sites.google.com/site/oulunpudatabase/).

- APCER: Attack Presentation Classification Error Rate
- BPCER: Bona Fide Presentation Classification Error Rate
- ACER: Average Classification Error Rate

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install oulumetrics
```

## Usage

```python
import oulumetrics

# y_attack_types is a list with the attack types for each sample in the dataset
# 1 - live sample
# 2 - print attack 1
# 3 - print attack 2
# 4 - display attack 1
# 5 - display attack 2
# y_pred is the list of predictions
# 1 - live
# 0 - attack
y_attack_types = [1, 1, 2, 2, 1, 3, 5, 4, 5, 5, 1]
y_pred = [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1]

# returns the metrics APCER, BPCER and ACER
oulumetrics.calculate_metrics(y_attack_types, y_pred)

# you can also provide a y_pred array with float values and a threshold for binarization (0.5 by default if not provided)
y_pred = [0.8, 0.2, 0.1, 0.9, 0.3, 0.1, 0.7, 0.5, 0.5, 0.4, 1, 0.8]

# returns the metrics APCER, BPCER and ACER
oulumetrics.calculate_metrics(y_attack_types, y_pred, 0.6)
```

## References
Boulkenafet, Z., Komulainen, J., Li, L., Feng, X., & Hadid, A. (2017, May). Oulu-npu: A mobile face presentation attack database with real-world variations. In 2017 12th IEEE international conference on automatic face & gesture recognition (FG 2017) (pp. 612-618). IEEE.
