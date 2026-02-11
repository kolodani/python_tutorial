x = set(("apple", "banana", "cherry"))
xx = set(("microsoft", "sony", "apple", 1))

x.add("potato")
print(x)

y = x.copy()
print(y)

y.clear()
print(y)

y = x.difference(xx)
print(y)

print(xx)
xx.discard(1)
print(xx)

y = x.intersection(xx)
print(y)

print(x.isdisjoint(xx))

print(x.issubset(xx))

print(x.issuperset(xx))

y = xx.copy()
y.pop()
print(y)

y = xx.copy()
y.remove("sony")
print(y)

print(x.symmetric_difference(xx))

print(x.union(xx))

y = x.update(xx)
print(y)
