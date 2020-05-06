# gluemotion: Glue COVID Detection

![lint-test](https://github.com/Luke31/gluemotion/workflows/lint-test/badge.svg)
![package-upload](https://github.com/Luke31/gluemotion/workflows/package-upload/badge.svg)

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
