import Core.chrome as chrome

operators = ['=', '+', '-', '*', '/', '%',
             '+=', '-=', '*=', '/=', '%=',
             '==', '>', '<', '>=', '<=', '!=',
             '&&', '||']


# parser
def parse(lex):
    print(lex)
    print() #empty line

    func = ''
    parameters = []

    varSetting = ['NAME', 'TYPE', 'VALUE']

    variables = {}
    for pos, tok in enumerate(lex):
        if tok == '+':
            pass

    #i = 0
    #while(i < len(lex)):
    for pos, tok in enumerate(lex):
        if tok[:5] == 'FUNC ':
            parameters = []
            # get function without the colons
            func = tok[6:-1]
        elif tok == 'FUNC_END':
            chrome.execute(func, parameters)
            func = ''
        elif func:
            parameters.append(tok)

        elif tok[:4] == 'VAR ':
            if lex[pos+1] in ['='] + operators[6:11]:
                varSetting[0] = tok[5:-1] # set name
