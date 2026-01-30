lalista = ["Daniel", "Alberto", "Vinzia"]

lalista.append("Grover")
print(lalista)

nuevalista = lalista.copy()
print(nuevalista)

nuevalista.clear()
print(nuevalista)

print(lalista.count("Alberto"))

lalista.extend("Best")
print(lalista)

print(lalista.index("Vinzia"))

lalista.insert(2, "Kolo")
print(lalista)

lalista.pop(4)
print(lalista)

lalista.remove("Kolo")
print(lalista)

lalista.reverse()
print(lalista)

lalista.sort()
print(lalista)
