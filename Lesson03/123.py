
def f(t, tf):
    c = 0
    r = 0
    if c * 2 + r * 4 == tf:
        return print(c, r)
    c = t - r
    tf = 2 * c + 4 * r
    return c+1

print(f(83, 240))

