def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print('f1:%d\nf2:%d\nf3:%d'%(f1(), f2(), f3()))