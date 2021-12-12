operators = ['=', '+', '-', '*', '/', '%',
             '+=', '-=', '*=', '/=', '%=',
             '==', '>', '<', '>=', '<=', '!=',
             '&&', '||']


class lexer:
    def __init__(self):
        self.tok = ''
        self.tokens = []

        self.string = ''
        self.commented = False;

        self.states = {'str': 0, 'char': 0, 'func': 0}

    # lex an entire file
    def lexFile(self, f):
        tokens = []
        # interpret file
        with open(f, 'r') as file:
            # read file
            data = file.readlines()
            # iterate lines
            for line in data:
                line += ' ' # add space
                # lex line
                toks = self.lex(line)
                tokens += toks #add tokens
        return tokens

    # lex data
    def lex(self, line, debug=False):
        tokens = []
        for char in line:
            self.tok += char
            #debugging
            if debug:
                print('\"' + self.tok + '\"')

            if self.commented == True:
                self.tok = ''
                break

            # space
            if char == ' ':
                if self.states['str'] == 0:
                    # self.tok not empty
                    if self.tok.strip():
                        # is digit
                        try:
                            convert = int(self.tok)
                            tokens.append('INT :' + str(convert) + ':')
                        except ValueError:
                            # strip space from final place
                            tokens.append('VAR :' + self.tok[:-1] + ':')
                    self.tok = ''

            # function call
            elif char == '(':
                tokens.append('FUNC {' + self.tok[:-1] + '}')
                self.states['func'] = 1
                self.tok = ''
            #function end
            elif char == ')':
                try:
                    #check for int
                    convert = int(self.tok[:-1])
                    tokens.append('INT :' + str(convert) + ':')
                except ValueError:
                    pass
                #end of function
                tokens.append('FUNC_END')
                self.tok = ''
            # new line
            elif self.tok == '\n':
                self.tok = ''
            # string
            elif char == '\"':
                self.tok = ''
                if self.states['str'] == 0:
                    self.states['str'] = 1
                else:
                    #tokens.append('STR :' + string + ':')
                    tokens.append('STR')
                    tokens.append(self.string)
                    self.string = ''
                    self.states['str'] = 0
            # currently inside string
            elif self.states['str'] == 1:
                self.string += self.tok
                self.tok = ''

            # sinle line comment
            elif self.tok == '//':
                self.tok = ''
                break

            # double line comment (start)
            elif self.tok == '/*':
                self.commented = True
            # double line comment (finish)
            elif self.tok == '*/':
                self.commented = False

            # equivelent
            elif self.tok in operators:
                tokens.append(self.tok)

        return tokens
