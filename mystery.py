# mystery.py -- AI 230, Project 01, Part B.
# Three sorting functions. All three are correct: each returns a new,
# sorted copy of its input list. One is insertion sort, one is merge
# sort, one is counting sort. The names and variables tell you nothing.
# Do NOT rename anything. Import them into your harness and make them
# confess: identification is by measured behavior, not by reading.

def sort_x(a):
    if len(a) < 2:
        return list(a)
    h = len(a) // 2
    p = sort_x(a[:h])
    q = sort_x(a[h:])
    r = []
    i = 0
    j = 0
    while i < len(p) and j < len(q):
        if p[i] <= q[j]:
            r.append(p[i])
            i += 1
        else:
            r.append(q[j])
            j += 1
    r += p[i:]
    r += q[j:]
    return r


def sort_y(a):
    r = list(a)
    for i in range(1, len(r)):
        v = r[i]
        j = i - 1
        while j >= 0 and r[j] > v:
            r[j + 1] = r[j]
            j -= 1
        r[j + 1] = v
    return r


def sort_z(a):
    if not a:
        return []
    u = min(a)
    w = max(a)
    c = [0] * (w - u + 1)
    for v in a:
        c[v - u] += 1
    r = []
    for k in range(len(c)):
        n = c[k]
        while n:
            r.append(k + u)
            n -= 1
    return r