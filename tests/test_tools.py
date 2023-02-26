# tools for note4datacamp
# import pytest
from note4datacamp.tools import findSpecialWords


class TestFindSpecialWords(object):
    def test_findSpecialWords1(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = """
_help_
_F _B test _.
"""
        result, find = findSpecialWords(example)
        expectation = ['_help_', '_F', '_B', '_']
        assert find
        assert expectation == result

    def test_findSpecialWords2(self):
        # each special word type test 2 examples,
        # one in the middle of the scentence, one at the end with punctuation.
        example = """
pyspark.sql.functions.split()
pyspark.sql.functions() spark.getOrCreate() test reverseString().
"""
        result, find = findSpecialWords(example)
        expectation = ['pyspark.sql.functions.split()', 'pyspark.sql.functions()',
                       'spark.getOrCreate()', 'reverseString()']
        assert find
        assert expectation == result

    def test_findSpecialWords3(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = """
'zzz'
'_there' 'yyy' test '_NumPy'.
"""

        result, find = findSpecialWords(example)
        expectation = ["'zzz'", "'_there'", "'yyy'", "'_NumPy'"]
        assert find
        assert expectation == result

    def test_findSpecialWords4(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = '''
"xxx"
"www" ".uuu" test "-vvv".
'''
        result, find = findSpecialWords(example)
        expectation = ['"xxx"', '"www"', '".uuu"', '"-vvv"']
        print('expectation: ', expectation, 'result:', result)
        # assert find
        assert expectation == result

    def test_findSpecialWords5(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = """
createOrReplaceTempView
PySpark test numPy test NumPy.
"""
        result, find = findSpecialWords(example)
        expectation = ['createOrReplaceTempView', 'PySpark', 'numPy', 'NumPy']
        print('expectation: ', expectation, 'result:', result)
        assert find
        assert expectation == result

    def test_findSpecialWords6(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = """

pyspark.sql.functions
pyspark.sql test test.test pandas.DataFrame.
"""
        result, find = findSpecialWords(example)
        expectation = ['pyspark.sql.functions', 'pyspark.sql', 'test.test', 'pandas.DataFrame']
        print('expectation: ', expectation, 'result:', result)
        assert find
        assert expectation == result

    def test_findSpecialWords7(self):
        # each special word type test 4 examples,
        # one as whole line, one at the beginning of a sentence,
        # one in the middle of the scentence, and the last at the end with punctuation.
        example = """
.mean()
.sql.mean Yes, .yes.yes this the .last.
the last.
"""
        result, find = findSpecialWords(example)
        expectation = ['.mean()', '.sql.mean', '.yes.yes', '.last']
        print('expectation: ', expectation, 'result:', result)
        assert find
        assert expectation == result

    def test_findSpecialWords8(self):
        # each special word type test 2 examples,
        # one in the middle of the scentence, one at the end with punctuation.
        example = '''
_help_
_F _B test _.

pyspark.sql.functions.split()
pyspark.sql.functions() spark.getOrCreate() test reverseString().

'zzz'
'_there' 'yyy' test '_NumPy'.

"xxx"
"www" ".uuu" test "-vvv".

createOrReplaceTempView
PySpark test numPy test NumPy.

pyspark.sql.functions
pyspark.sql test test.test pandas.DataFrame.

.mean()
.sql.mean Yes, .yes.yes this the .last.
the last.
True or False? new test
'''
        myspecial = ['True', 'False']
        result, find = findSpecialWords(example, myspecial)
        expectation = ['_help_', '_F', '_B', '_',
                       'pyspark.sql.functions.split()', 'pyspark.sql.functions()',
                       'spark.getOrCreate()', 'reverseString()',
                       "'zzz'", "'_there'", "'yyy'", "'_NumPy'",
                       '"xxx"', '"www"', '".uuu"', '"-vvv"',
                       'createOrReplaceTempView', 'PySpark', 'numPy', 'NumPy',
                       'pyspark.sql.functions', 'pyspark.sql', 'test.test', 'pandas.DataFrame',
                       '.mean()', '.sql.mean', '.yes.yes', '.last', 'True', 'False']
        print('expectation: ', expectation, 'result:', result)
        assert find
        assert expectation == result
