# Description

This package implements the metrics (APCER, BPCER, ACER) for face anti-spoofing described at the reference and used in the OULU-NPU dataset (https://sites.google.com/site/oulunpudatabase/).

- APCER: Attack Presentation Classification Error Rate
- BPCER: Bona Fide Presentation Classification Error Rate
- ACER: Average Classification Error Rate

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## References
Boulkenafet, Z., Komulainen, J., Li, L., Feng, X., & Hadid, A. (2017, May). Oulu-npu: A mobile face presentation attack database with real-world variations. In 2017 12th IEEE international conference on automatic face & gesture recognition (FG 2017) (pp. 612-618). IEEE.
