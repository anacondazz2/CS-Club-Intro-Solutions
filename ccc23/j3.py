n=int(input())
people = []
days = [0,0,0,0,0]
for i in range(n):
    a = input()
    aarray = []
    for c in a:
        aarray.append(c)
    people.append(aarray)

for i in range(len(people)):
    for j in range(5):
        if people[i][j] == "Y":
            days[j] += 1

best = max(days)
bestdays = []
for d in range(len(days)):
    if days[d] == best:
        bestdays.append(d+1)

toPrint = ""
first = True
for day in bestdays:
    if first:
        toPrint += str(day)
        first = False
    else:
        toPrint+= "," + str(day)
print(toPrint) 