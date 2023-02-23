"""Main module."""

import re
# from IPython.core.getipython import get_ipython
from note4datacamp.tools import empSpecialWords


def transcript_section(text):
    """Transfer the transcript part

    Parameters
    ----------
    text : string
           Input text from datacamp video transcript

    Returns
    -------
    finaltext : string
        Dealed string can be directly used as note

    """

    finaltext = ""
    for line in re.split('\n', text):
        finalline = ""
        num = re.findall('^\d+', line)
        if len(num) > 0:
            finalline += "\n\n## "
        else:
            finalline += "\n"
        finalline += empSpecialWords(line)
        finaltext += finalline
    return finaltext
    # ip = get_ipython()
    # ip.set_next_input(transcript_section(text), replace=False)


def typesetting_instruction(text):
    """Transfer the instruction part

    Parameters
    ----------
    text : string
           Input text from datacamp exercise Instruction part

    Returns
    -------
    finaltext : string
        Dealed string can be directly used as note

    """
    finaltext = ''
    lineno = 0
    for line in re.split('\n', text):
        if lineno == 0:
            finaltext += line + ' '
        elif lineno == 1:
            finaltext += ' ' + re.findall('\d+', line)[0] + 'XP\n'
        else:
            if len(line.strip()) > 0:
                finaltext += '- ' + line.strip() + '\n'
        lineno += 1
    finaltext = empSpecialWords(finaltext)
    return finaltext
    # ip = get_ipython()
    # ip.set_next_input(typesetting_instruction(text), replace=False)


def typesetting_answer(text):
    """Transfer the answer part

    Parameters
    ----------
    text : string
           Input text from datacamp exercise Ansewer part

    Returns
    -------
    finaltext : string
        Dealed string can be directly used as note

    """

    finaltext = ''
    lineno = 0
    justpress = False
    for line in re.split('\n', text):
        if lineno == 0:
            finaltext += line + ' '
        elif lineno == 1:
            finaltext += ' ' + re.findall('\d+XP', line)[0] + '  \n'
        elif lineno == 2:
            finaltext += line + '\n- [ ] '
        else:
            if not justpress:
                if line.strip() == 'press':
                    justpress = True
                else:
                    finaltext += line.strip()
            else:
                justpress = False
                finaltext += '\n- [ ] '
        lineno += 1
    finaltext = empSpecialWords(finaltext)
    return finaltext
    # ip = get_ipython()
    # ip.set_next_input(typesetting_answer(text), replace=False)
