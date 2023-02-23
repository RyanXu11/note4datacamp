# tools for note4datacamp
import re


def findSpecialWords(text):
    """Use to find the Special Words in the text.
    The Special Words need to be 'coded' by '``, there are following types:
        - functions include '()', such as pyspark.sql.functions() or replace()
        - variables with '_', like my_variable_, _token
        - in '', such as 'note',
        - in "", like "note"
        - humpString, such as myStringExample
        - functions without '()', but with '.', like as pyspark.sql.functions
        - functions begin with '.', such as .filter

    Parameters
    ----------
    text : string
           Input text

    Returns
    -------
    specialwords : list
          The list result for special words.
    find: boolean
          If find special words, find is Ture, or False.
    """
    # 7 regex patterns for special words
    pattern1 = '(\w*\.?)+(?=\(\))\(\)'   # find liek pyspark.sql.functions() or replace()
    pattern2 = '\w*_\w*'    # find variables like my_variable_
    pattern3 = r'[\s\n]\'.+?\''    # find content in '  ', not greedy
    pattern4 = r'\".+?\"'    # find content in "  ", not greedy
    pattern5 = '[a-zA-Z]+[A-Z][a-z0-9]+\w*?'   # humpString
    pattern6 = '(\w+\.)+\w+'      # find funtions like pyspark.sql.functions
    pattern7 = '\s\.(\w+\.)*\w+(\(\))?'      # find funtions like .sql.functions

    result = re.findall(f'({pattern1}|{pattern2}|{pattern3}|{pattern4}|{pattern5}|{pattern6}|{pattern7})', text)

    specialwords = [x[0].strip() for x in result]
    find = False
    if len(specialwords) > 0:
        find = True
        # print('there are specialwords! \n', specialwords)
    return specialwords, find


def empSpecialWords(line):
    """Emphasize the special words by add '`` at the beginning and end
    of all special words.

    Parameters
    ----------
    line : text
        Each line in the whole text need to be deal with

    Returns
    -------
    finaltext : text
        Emphsized of all special words in the line, return the new line

    """
    specialwords, find = findSpecialWords(line)
    finaltext = ""
    punctuations = ['.', ',', '!', '?', ':', '\n', '\t']
    new_word_token = []

    if find:
        # tokenize the line by ' '
        word_token = re.split(' ', line)
        print(word_token)
        # if the word in specialwords, add "`" at the beginning & end
        word_token = ["`" + word + "`" if word in set(specialwords) else word for word in word_token]

        # the case specialwords at the end with punctuation
        for word in word_token:
            if word != word_token[-1]:
                new_word_token.append(word)
            else:
                if (word[:-1] in set(specialwords)) & (word[-1] in punctuations):
                    new_word_token.append("`" + word[:-1] + "`" + word[-1])
                else:
                    new_word_token.append(word)

        word_token = new_word_token
        # convert words to sentences
        for word in word_token:
            finaltext += word + ' '

        finaltext = finaltext.strip()
    else:
        finaltext = line
    return finaltext
