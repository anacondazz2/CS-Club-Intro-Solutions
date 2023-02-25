"""
This code was written by Jonathan, he gave it.

His Github: https://github.com/Lock-The-Door
"""
word = input()
rowCount = int(input())
columnCount = int(input())
rows = []
for r in range(rowCount):
    rows.append(str.join("", input().split(' ')))
# indexes of every trail
trails = []
# first letter
for r in range(rowCount):
    for c in range(columnCount):
        if rows[r][c] == word[0]:
            trails.append([r, c])
# check for next letter in each trail
newTrails = []
# new_full_trail = []
for t in trails:
    # get neighbors
    for nr in range(-1, 2):
        for nc in range(-1, 2):
            if abs(nr) + abs(nc) == 0 or t[0] + nr < 0 or t[1] + nc < 0:
                continue
            try:
                if rows[t[0] + nr][t[1] + nc] == word[1]:
                    newTrails.append([t[0] + nr, t[1] + nc, t[0], t[1], False])
            except:
                pass
trails = newTrails
# next passes
for i in range (2, len(word)):
    newTrails = []
    for t in trails:
        # get neighbors
        for nr in range(-1, 2):
            for nc in range(-1, 2):
                if abs(nr) + abs(nc) == 0 or t[0] + nr < 0 or t[1] + nc < 0:
                    continue
                # ensure going in right direction
                if (abs(nr) + abs(nc) == 1) != (abs(t[0] - abs(t[2])) + abs(t[1] - abs(t[3])) == 1):
                    continue
                strict_direction = t[4]
                if (t[0] - t[2] != nr) or (t[1] - t[3] != nc): # direction change
                    if strict_direction:
                        continue
                    strict_direction = True
                try:
                    if rows[t[0] + nr][t[1] + nc] == word[i]:
                        newTrails.append([t[0] + nr, t[1] + nc, t[0], t[1], strict_direction])
                except:
                    pass
    trails = newTrails
print(len(trails))