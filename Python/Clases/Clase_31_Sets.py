'''

Sets o conjuntos

s.union(t)
s.intersection(t)
s.difference(t)
t.difference(s)

'''

s = set([1,2,3])
t = set([3,4,5])

print(s.union(t))
print(s.intersection(t))
print(s.difference(t))
print(t.difference(s))
