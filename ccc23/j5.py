w = input()
r = int(input())
c = int(input())
grid = []
times = 0
for i in range(r):
    row = input()
    toAdd=[]
    for i in row:
        if i != " ":
            toAdd.append(i)
    grid.append(toAdd)

reverse = w[::-1]
for i in range(r):
    for j in range(c):

        # Horizontal reverse
        match = True
        for x in range(len(w)): 
            try:
                if grid[i][j+x] != reverse[0+x]:
                    match = False
            except:
                match = False
                break
        if match == True:
            times += 1
        

        # Horizontal normal
        match = True
        for x in range(len(w)):
            try:
                if grid[i][j+x] != w[0+x]:
                    match = False
            except:
                match = False
                break
        if match == True:
            times += 1

        # vertical reverse
        match = True
        for x in range(len(w)):
            try:
                if grid[i+x][j] != reverse[0+x]:
                    match = False
            except:
                match = False
                break
        if match == True:
            times += 1

        # vertical normal
        match = True
        for x in range(len(w)):
            try:
                if grid[i+x][j] != w[0+x]:
                    match = False
            except:
                match = False
                break
        if match == True:
            times += 1
        
        # diagonal reverse
        match = True
        for x in range(len(w)): # go left
            try:
                if grid[i+x][j-x] != reverse[0+x]:
                    match = False
                    break
            except:
                match = False
                break
        if match == True:
            times += 1
        match = True
        for x in range(len(w)): # go right
            try:
                if grid[i+x][j+x] != reverse[0+x]:
                    match = False
                    break
            except:
                match = False
                break
        if match == True:
            times += 1

        # diagonal normal
        match = True
        for x in range(len(w)): # go left
            try:
                if grid[i+x][j-x] != w[0+x]:
                    match = False
                    break
            except:
                match = False
                break
        if match == True:
            times += 1
        match = True
        for x in range(len(w)): # go right
            try:
                if grid[i+x][j+x] != w[0+x]:
                    match = False
                    break
            except:
                match = False
                break
        if match == True:
            times += 1
print(times)
