=============
note4datacamp
=============

## Badges

[![workflow for Codecov](https://github.com/RyanXu11/note4datacamp/actions/workflows/workflow.yml/badge.svg)](https://github.com/RyanXu11/note4datacamp/actions/workflows/workflow.yml)


A Python package to help with note-taking in DATACAMP courses.

It can type setting in order to read in jupyter notebook, and `emphasize` the functions, variables such as `__version__`, `pyspark.sql.functions()` or `createOrReplaceTempView`, etc.



Features
--------

There are 3 functions for different type documents:
- `transcript_section(text)`
Typesetting for video transcript and main part for exercise.

- `typesetting_instruction(text)`
Typesetting for instruction part of exercise.

- `typesetting_answer(text)`
Typesetting for answer part which are checkbox.

Of course, there are other types document in the exercises, hope I can update later for more situations.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
