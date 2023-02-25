n=int(input())
t = {
    "Poblano":1500,
    "Mirasol":6000,
    "Serrano":15500,
    "Cayenne":40000,
    "Thai":75000,
    "Habanero":125000
}

f = 0
for i in range(n):
    p = input()
    f += t[p]
print(f)