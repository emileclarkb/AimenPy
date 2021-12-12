import sys

from Core.lexer import lexer
from Core.parser import parse

operators = ['=', '+', '-', '*', '/', '%',
             '+=', '-=', '*=', '/=', '%=',
             '==', '>', '<', '>=', '<=', '!=',
             '&&', '||']

#\[(.*?)\]

if __name__ == '__main__':
    lex = lexer()

    # file given
    if len(sys.argv) > 1:
        tokens = lex.lexFile(sys.argv[1])
        parse(tokens)
    else:
        try:
            while True:
                line = input('>> ')
                tokens = lex.lex(line, debug=False)
                parse(tokens)

        except KeyboardInterrupt:
            pass

    '''
    # file given
    if len(sys.argv) > 1:
        # interpret file
        with open(sys.argv[1], 'r') as file:
            tokens = lex(file.readlines())
            parse(tokens)
    else:
        try:
            while True:
                line = input('>> ')
                tokens = lexLine(line)
                parse(tokens)

        except KeyboardInterrupt:
            pass
    '''
