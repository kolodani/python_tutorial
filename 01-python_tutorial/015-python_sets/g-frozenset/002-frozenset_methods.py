x = frozenset({"apple", "banana", "cherry"})
xx = frozenset({"microsoft", "sony", "apple"})

y = x.copy()
print(y)

print(x.difference(xx))

print(x.intersection(xx))

print(x.isdisjoint(xx))

print(x.issubset(xx))

print(x.issuperset(xx))

print(x.symmetric_difference(xx))

print(x.union(xx))