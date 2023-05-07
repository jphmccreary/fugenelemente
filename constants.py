# (Länger, 1998)
# out of 46700 total
# these are also the keys for the dicts that reference them

FUGENELEMENTE_FREQUENCY_ORDER = (
    'NULL',             # 48.7%
    'ADD_S',            # 20.6%
    'ADD_N',            # 11.4%
    'ADD_EN',           # 9.2%
    'ADD_NEN',          # 5.6%
    'DEL_US_ADD_EN',    # 1.3%
    'DEL_UM_ADD_EN',    # 0.7%
    'DEL_UM_ADD_A',
    'DEL_E',
    'DEL_A_ADD_EN',
    'ADD_E',
    'UMLAUT_ADD_E',
    'DEL_ON_ADD_EN',
    'ADD_ES',
    'UMLAUT_ADD_ER',
    'DEL_EN',
    'DEL_ON_ADD_A',
    'ADD_ER',
    'ADD_IEN',
    'DEL_E_ADD_I',
)

SOURCE_TYPE_MAP = {
    0: 'news'
}

CORPUS_ID_MAP = {
    0: 'PDW'
}

INVALID_CHARS = {'…', '\xad', '\u200b', '\x80', '%', '”', ';', '^', '`', '/', '‚', '>', '~', '–', '•', '\x10', '�', '"', ')', '‹', '´', '“', '@', '+', '’', '°', '®', '!', '(', '?', '₂', '#', '\\', 'ł', '\x96', '\x92', '·', '{', '|', '\ufeff', '\x84', '„', '$', '‑', '¼', '=', '.', '\uf003', '™', '³', '\x94', ']', ',', '[', '‐', '*', '›', '‘', '<', '̈', "'", '&', '«', '-', '}', '»', '²', '\x93', '_', ':'}

PREPOSITIONS = {
    # AKKUSATIV
    'bis',
    'durch', 'durchs',
    'für', 'fürs', 'fuer', 'fuers'
    'gegen',
    'ohne',
    'um',
    'wider',
    # AKKUSATIV UND SELTEN
    'betreffend',
    # DATIV
    'aus',
    'außer', 'ausser',
    'bei', 'beim',
    'mit',
    'nach',
    'seit',
    'von', 'vom'
    'zu',
    # DATIV UND SELTEN
    'ab',
    'entgegen',
    'entsprechend',
    'gegenüber', 'gegenueber'
    'gemäß', 'gemäss' 'gemaeß', 'gemaess'
    'samt', 'mitsamt',
    'nahe',
    # WECHSELPRÄPOSITIONEN
    'an', 'ans', 'am',
    'auf', 'aufs',
    'hinter', 'hinters', 'hinterm',
    'in', 'ins', 'im',
    'neben',
    'über', 'übers', 'überm', 'ueber', 'uebers', 'ueberm',
    'unter', 'unters', 'unterm'
    'vor', 'vors', 'vorm',
    'zwischen',
    # GENITIV GESCHRIEBEN, DATIV GESPROCHEN
    'anstatt', 'statt',
    'trotz',
    'während', 'waehrend',
    'wegen',
    # IMMER GENITIV
    'außerhalb', 'innerhalb', 'oberhalb', 'unterhalb', 'ausserhalb',
    'diesseits', 'jenseits', 'beiderseits',
    # WECHSELPRÄPOSITION AM ENDE, GENITIV AM ANFANG
    'entlang',
    # !GIBTS MEHR GENITIV, ABER SIE SIND SEHR SELTEN

}
