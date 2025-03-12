#INICIO DIA 7 

#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)
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
