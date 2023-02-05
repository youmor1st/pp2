def solve(numheads, numlegs):
    if numheads >= numlegs:
        return "incorrect"
    elif numlegs % 2 != 0:
        return "incorrect"
    else:
        rabbit = (numlegs - 2 * numheads) / 2
        chicken = (numheads - rabbit)
        return rabbit, chicken

numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))