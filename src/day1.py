# tall = [
#     1721,
#     979,
#     366,
#     299,
#     675,
#     1456,
# ]

fil = open("input/dag1.txt")

tall = []

for linje in fil:
    linje = linje.strip()
    linje_tall = int(linje)
    tall.append(linje_tall)

fil.close()


print("part 1")

for a in tall:
    for b in tall:
        if a + b == 2020:
            print(a * b)

print("part 2")

for a in tall:
    for b in tall:
        for c in tall:
            if a + b + c == 2020:
                print(a * b * c)

