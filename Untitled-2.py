set1={"Bmw","audi","mercedes","honda","Bmw","mercedes"}
set2={"Bmw","audi","honda","mercedes","honda"}
print("orignal set:",set1)
print("Union set:",set1.union(set2))
print("Common set:",set1.intersection(set2))
print("Difference set:",set1.difference(set2))
print("symmetric Difference:" ,set1.symmetric_difference(set2))
