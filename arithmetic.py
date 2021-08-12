# write your code here
import random
score = 0
while True:
    level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n")
    if level == "1":
        description = "simple operations with numbers 2-9"
        break
    elif level == "2":
        description = "integral squares of 11-29"
        break
    else:
        print("Incorrect format.")
        level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n")
if level == "1":
    for i in range(5):
        y = [random.randint(2, 9), random.choice(["+", "-", "*"]), random.randint(2, 9)]
        print(f"{y[0]} {y[1]} {y[-1]}")
        if y[1] == "+":
            answer = int(y[0]) + int(y[-1])
        elif y[1] == "-":
            answer = int(y[0]) - int(y[-1])
        elif y[1] == "*":
            answer = int(y[0]) * int(y[-1])
        x = input()
        while True:
            if x.lstrip("-").isdigit():
                x = int(x)
                break
            elif len(x) == 0:
                x = input("Incorrect format.\n")
            else:
                x = input("Incorrect format.\n")
        if x == answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
else:
    for i in range(5):
        y = random.randint(11, 29)
        answer = y ** 2
        print(y)
        x = input()
        while True:
            if x.lstrip("-").isdigit():
                x = int(x)
                break
            elif len(x) == 0:
                x = input("Incorrect format.\n")
            else:
                x = input("Incorrect format.\n")
        if x == answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

need_save = input(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
if need_save == "yes" or need_save == "YES" or need_save == "y" or need_save == "Yes":
    name = input("What is your name?")
    with open("results.txt", "a") as f:
        f.write(f"{name}: {score}/5 in level {level} ({description}).")
print('The results are saved in "results.txt".')
