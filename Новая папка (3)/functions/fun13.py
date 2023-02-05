import random

print("Hello! What is your name?")
s = str(input())

print("Well, KBTU, I am thinking of a number between 1 and 20.")
print("Take a guess.")

ans = random.randint(1, 20)
l = 1
r = 20
cnt = 0

while l <= r:
    md = (l + r) // 2
    print(md)
    print(end="\n")

    cnt += 1
    if md == ans:
        print("Good job,", s + "!", "You guessed my number in", cnt, "guesses!")
        exit(0)
    elif md < ans:
        print("Your guess is too low.")
        print("Take a guess.")
        l = md + 1
    else:
        print("Your guess is too high.")
        print("Take a guess.")
        r = md - 1