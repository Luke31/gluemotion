# gluemotion: Glue COVID Detection

![lint-test](https://github.com/Luke31/gluemotion/workflows/lint-test/badge.svg)
![package-upload](https://github.com/Luke31/gluemotion/workflows/package-upload/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/7af5042424d365aa5c6b/maintainability)](https://codeclimate.com/github/Luke31/gluemotion/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7af5042424d365aa5c6b/test_coverage)](https://codeclimate.com/github/Luke31/gluemotion/test_coverage)

Example project for showcasing python library distribution.
Appends `covid_mentioned` columns to a Glue DynamicFrame

Install using
```bash
pip install -i https://test.pypi.org/simple/ gluemotion
```

Usage in AWS Glue
```python
from gluemotion import Gluemotion
gm = Gluemotion('text')
result_frame = Map.apply(frame = my_frame, f = gm.add_covid_check)
```
