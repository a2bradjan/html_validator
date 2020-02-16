#!/bin/python3

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    html = _extract_tags(html)
    index = 0
    while index < len(html)-1:
        e = html[index]
        f = "<" + "/" + e[1:]
        g = html[index+1]

        if g != f:
            e = g
            f = "<" + "/" + e[1:]
            index+=1
            if e[1:2] == "/":
                return False
        else:
            html.remove(f)
            html.remove(e)
            index=0
    if len(html) != 0:
        return False
    else:
        return True


    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

def _extract_tags(html):
    '''
    '''
    s = []
    listhtml = list(html)
    index = 0
    while index < len(listhtml):
        e = listhtml[index]
        if e == '<':
            string = ''
            while listhtml[index] != '>':
                string = string + listhtml[index]
                index = index + 1
            string = string + listhtml[index]
            s.append(string)
        index = index + 1
    return s
