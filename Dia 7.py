#INICIO DIA 7 

#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies = {'Amazon', 'Oracle', 'IBM', 'Twitter', 'Microsoft', 'Google', 'Apple', 'Facebook'}
it_companies.update(["Youtube", "Wikipedia"])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies = {'Microsoft', 'Twitter', 'Facebook', 'Google', 'Youtube', 'Apple', 'Wikipedia', 'Oracle', 'Amazon', 'IBM'}
it_companies.remove("Wikipedia")
print(it_companies)

#What is the difference between remove and discard
print("Con remove quitamos un elemento de forma permanente del set")
print("Con Discard descartamos un elemento pro una sola vez, hasta que se vuelve a ejecutar")


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

#NIVEL 3

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
st = set(age)
print(st)
LongitudSt = len(st)
LongitudAges = len(age)
MásGrande = LongitudSt.symmetric_difference(LongitudAges)





