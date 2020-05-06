# gluemotion: Glue Emotion Detection

![lint-test](https://github.com/Luke31/batmobile/workflows/lint-test/badge.svg?branch=master)
![package-upload](https://github.com/Luke31/batmobile/workflows/package-upload/badge.svg)

Example project for showcasing python library distribution.
Appends emotion columns to a Glue DynamicFrame

Install using
```bash
pip install -i https://test.pypi.org/simple/ gluemotion
```

Usage in AWS Glue
```python
from gluemotion import Gluemotion
gm = Gluemotion(text_col='text')
result_emotions_frame = Map.apply(frame = my_frame, f = gm.add_emotions)
```

# Credits
Using [pymlask](https://github.com/ikegami-yukino/pymlask)
