import sys

def execute(func, parameters):
    strParam =  '[\"' + '\",\"'.join(parameters) + '\"]'
    a = eval('chrome'+func.capitalize()+'('+strParam+')')
    if a:
        print(a)

def chromeAimen(parameters):
    try:
        # interpret file
        with open(parameters[1], 'r') as file:
            tokens = aimen.lex(file)
            aimen.parse(tokens)
    except IndexError:
        pass


def chromeLog(parameters):
    #for key, value in enumerate(parameters):
    #    parameters[key] = value.replace('STR ', '').replace(':', '')
    print(' '.join(parameters))

def chromeExit(parameters):
    sys.exit(0)

def chromeAdd(parameters):
    a, b = parameters[:2]


# check for data types
def chromeType(var):
    if chromeInt(var[0]):
        return 'INT :0:'
    elif chromeStr(var[0]):
        return 'STR :"":'
    elif chromeBool(var[0]):
        return 'BOOL :true:'
    return "NULL"


def chromeInt(parameters):
    if 'INT' == parameters[0][:3]:
        return True
    return False

def chromeStr(parameters):
    if 'STR' == parameters[0][:6]:
        return True
    return False

def chromeBool(parameters):
    if 'BOOL' == parameters[0][:4]:
        return True
    return False

# ludwig7 
def chromeFishpog(parameters):
    with open('Core/Data/fishpog.txt', 'r') as pog:
        fishpog = pog.read()
        print(fishpog)
