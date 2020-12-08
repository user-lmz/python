# d = {'A': 'a', 'L': 'l', 'I': 'i', 'S': 's', 'T': 't',
#      'a': 'A', 'm': 'M', 'd': 'D', 'r': 'R'}
d = {'adam': 'Adam', 'LISA': 'Lisa', 'barT': 'Bart'}

def normalize(name):
    return d[name]

#L1 = 'adam'
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)