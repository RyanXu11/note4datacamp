# tools for note4datacamp
import re


def findSpecialWords(text, myspecial=None):
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

    # User defined special words
    if myspecial != None:
        if isinstance(myspecial, list):
            if len(myspecial) > 0:
                myspecial = [x if isinstance(x, str) else str(x) for x in myspecial]
                result2 = [x for x in myspecial if re.search(x, text)]
            else:
                raise ValueError("The list variable 'myspecial' has at least one element in it.")
        else:
            raise ValueError("The type of 'myspecial' must be list.")
    else:
        result2 = []
  
    specialwords = [x[0].strip() for x in result] + result2
    find = False
    if len(specialwords) > 0:
        find = True
        # print('there are specialwords! \n', specialwords)
    return specialwords, find


def empSpecialWords(text, myspecial=None):
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
    # line by line, or there are more complicated situations:
    # the 1st is '\n' at the end of word token
    # the 2nd is punctuation with '\n' like '.\n' at the end of some word token.
    # the 3rd is like '.\n\n' because there're sevel space lines
    # the 4th is like '.\n\n-', the '-' at the beginning of lines below
    # re.split by '\n' will eliminate the above complex situations
    for line in re.split('\n', text):
        specialwords, find = findSpecialWords(line, myspecial)
        
        if not find:
            finaltext += line + '\n'    # restore the text from line
        else:
            # tokenize the line by ' ', word_token is a word token list
            word_token = re.split(' ', line)
            #print(word_token)
            # if the word in specialwords, add "`" at the beginning & end
            # this can deal with the specialwords without endwith punctuation
            word_token = ["`"+word+"`" if word in set(specialwords)
                          else word for word in word_token]

            # the case specialwords with punctuation, the token length must >1
            new_word_token=[]
            for word in word_token:
                if (len(word)<1):
                    new_word_token.append(word)
                elif (word[:-1] in set(specialwords)) & (word[-1] in punctuations):
                        new_word_token.append("`"+word[:-1]+"`"+word[-1])
                else:
                    new_word_token.append(word)

            word_token = new_word_token

            # convert words to sentences
            finalline = ""            
            for word in word_token:
                finalline += word + ' '
            finalline = finalline.strip()    # remove extra space
            #print(finalline)

            finaltext += finalline +'\n' # restore the text from processed line
    
    return finaltext