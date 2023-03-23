import pickle

ycs = pickle.load(open('dumps/1998ycs', 'rb'))

for yc in ycs[-50:]:
    print(yc.text)
