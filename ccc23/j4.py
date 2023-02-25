c = int(input())
one = input()

r1 = []
for char in one:
    if char != " ":
        r1.append(int(char))
two = input()
r2 = []
for char in two:
    if char != " ":
        r2.append(int(char))



sum=0
for i in range(c):
    if r1[i] == 1:
        sum+=3
    if r2[i] == 1:
        sum+=3

for i in range(c):
    try:
        if r1[i] == r1[i+1] == 1:
            sum-=2
        if r2[i] == r2[i+1] == 1:
            sum-=2
    except: pass

    if i % 2 == 0:
        if r1[i] == r2[i] == 1:
            sum-=2
print(sum)
