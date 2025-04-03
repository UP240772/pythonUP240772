#NIVEL 2
#Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

AB = A.union(B)
print(AB)

#Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))

#Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.issubset(B))

#Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))

#Join A with B and B with A
AB = A.union(B)
print(AB)
BA = B.union(A)
print(BA)

#What is the symmetric difference between A and B
print(B.symmetric_difference(A))

#Delete the sets completely
del A
del B
del AB
del BA

print("revisado")