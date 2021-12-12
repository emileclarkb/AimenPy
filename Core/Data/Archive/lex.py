operators = ['=', '+', '-', '*', '/', '%',
             '+=', '-=', '*=', '/=', '%=',
             '==', '>', '<', '>=', '<=', '!=',
             '&&', '||']


# lexer
def lex(line):
    tok = ''
    tokens = []

    string = ''
    commented = False;

    states = {'str': 0, 'char': 0, 'func': 0}

    # iterate lines
    for line in data:
        line += ' ' # add space
        for char in line:
            tok += char
            #debugging
            #rint('\"' + tok + '\"')

            if commented == True:
                tok = ''
                break

            # space
            if char == ' ':
                if states['str'] == 0:
                    # tok not empty
                    if tok.strip():
                        # is digit
                        try:
                            convert = int(tok)
                            tokens.append('INT :' + str(convert) + ':')
                        except ValueError:
                            # strip space from final place
                            tokens.append('VAR :' + tok[:-1] + ':')
                    tok = ''

            # function call
            elif char == '(':
                tokens.append('FUNC {' + tok[:-1] + '}')
                states['func'] = 1
                tok = ''
            #function end
            elif char == ')':
                try:
                    #check for int
                    convert = int(tok[:-1])
                    tokens.append('INT :' + str(convert) + ':')
                except ValueError:
                    pass
                #end of function
                tokens.append('FUNC_END')
                tok = ''
            # new line
            elif tok == '\n':
                tok = ''
            # string
            elif char == '\"':
                tok = ''
                if states['str'] == 0:
                    states['str'] = 1
                else:
                    #tokens.append('STR :' + string + ':')
                    tokens.append('STR')
                    tokens.append(string)
                    string = ''
                    states['str'] = 0
            # currently inside string
            elif states['str'] == 1:
                string += tok
                tok = ''

            # sinle line comment
            elif tok == '//':
                tok = ''
                break

            # double line comment (start)
            elif tok == '/*':
                commented = True
            # double line comment (finish)
            elif tok == '*/':
                commented = False

            # equivelent
            elif tok in operators:
                tokens.append(tok)
                tok = ''

    return tokens
