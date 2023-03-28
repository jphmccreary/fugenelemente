# this could be problematic.
# how do we know we're replacing the correct umlauted vowel?
# working with the assumption that it's the one closest to the end of a word
# could there be more than one ?!
def deumlaut(s: str) -> tuple:
    # reverse the string so it searches from the back
    s = s[::-1]

    # not using str.replace because I want to be able to write in
    # different handling for when the umlaut isn't found, ie, return s, False
    i = s.find('ä')
    if not i == -1:
        return (s[:i] + 'a' + s[i+1:])[::-1], True

    i = s.find('ö')
    if not i == -1:
        return (s[:i] + 'o' + s[i+1:])[::-1], True

    i = s.find('ü')
    if not i == -1:
        return (s[:i] + 'u' + s[i+1:])[::-1], True

    i = s.find('Ä')
    if not i == -1:
        return (s[:i] + 'A' + s[i+1:])[::-1], True

    i = s.find('Ö')
    if not i == -1:
        return (s[:i] + 'O' + s[i+1:])[::-1], True

    i = s.find('Ü')
    if not i == -1:
        return (s[:i] + 'U' + s[i+1:])[::-1], True

    return s[::-1], False

def umlaut_add_e(s):
    if not s[-1] == 'e':
        return s
    return deumlaut(s[:-1])[0]

def umlaut_add_er(s):
    if not s[-2:] == 'er':
        return s
    return deumlaut(s[:-2])[0]

# (Länger, 1998)
operations = {
    'NULL': lambda x: x,
    'DEL_E': lambda x: x + 'e',
    'DEL_EN': lambda x: x + 'en',

    'ADD_S': lambda x: x if not x[-1] == 's' else x[:-1],

    'ADD_N': lambda x: x if not x[-1] == 'n' else x[:-1],

    'ADD_EN': lambda x: x if not x[-2:] == 'en' else x[:-2],
    'DEL_US_ADD_EN': lambda x: x if not x[-2:] == 'en' else x[:-2] + 'us',
    'DEL_UM_ADD_EN': lambda x: x if not x[-2:] == 'en' else x[:-2] + 'um',
    'DEL_ON_ADD_EN': lambda x: x if not x[-2:] == 'en' else x[:-2] + 'on',
    'DEL_A_ADD_EN': lambda x: x if not x[-2:] == 'en' else x[:-2] + 'a',

    'ADD_NEN': lambda x: x if not x[-3:] == 'nen' else x[:-3],

    'DEL_UM_ADD_A': lambda x: x if not x[-1] == 'a' else x[:-1] + 'um',
    'DEL_ON_ADD_A': lambda x: x if not x[-1] == 'a' else x[:-1] + 'on',

    'ADD_E': lambda x: x if not x[-1] == 'e' else x[:-1],
    'UMLAUT_ADD_E': umlaut_add_e,

    'ADD_ES': lambda x: x if not x[-2:] == 'es' else x[:-2],

    'UMLAUT_ADD_ER': umlaut_add_er,
    'ADD_ER': lambda x: x if not x[-2:] == 'er' else x[:-2],

    'ADD_IEN': lambda x: x if not x[-3:] == 'ien' else x[:-3],

    'DEL_E_ADD_I': lambda x: x if not x[-1] == 'i' else x[:-1] + 'e',
}
