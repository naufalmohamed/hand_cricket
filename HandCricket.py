import random

def toss():
    toss_options = ["H", "T"]
    toss_result = random.choice(toss_options)
    return toss_result

def select_bat_or_chase(toss_result, head_or_tail):
    if toss_result == head_or_tail:
        print("""
You've Won the Toss
""")
        incorrect = True
        while incorrect:
            input_bat_or_chase = input("Batting or Chasing (B/C): ")
            if input_bat_or_chase == "B" or input_bat_or_chase == "C":
                incorrect = False
            else:
                print("Invalid Input! Try again!")

        user_won_toss = True
    elif toss_result != head_or_tail:
        print("""
You've Lost the Toss
""")
        b_or_c = ["B","C"]
        input_bat_or_chase = random.choice(b_or_c)
        if input_bat_or_chase == "B":
            print("""
Computer Chose Batting
""")
        elif input_bat_or_chase == "C":
            print("""
Computer Chose Chasing
""")
        user_won_toss = False
    return input_bat_or_chase, user_won_toss


def first_batting(input_bat_or_chase, user_won_toss):
    if user_won_toss == True:
        if input_bat_or_chase == "B":
            one_batting = "User"
        elif input_bat_or_chase == "C":
            one_batting = "Comp"
    elif user_won_toss == False:
        if input_bat_or_chase == "B":
            one_batting = "Comp"
        elif input_bat_or_chase == "C":
            one_batting = "User"

    return one_batting


def first_innings(one_batting, wickets):

    first_innings_user = []
    first_innings_comp = []
    numb = [1, 2, 3, 4, 5, 6]
    one_wickets_lost = 0

    one_loop = True
    while one_loop == True:

        one_incorrect = True
        while one_incorrect:
            user_input = input("Type your number: ")
            if user_input.isnumeric():
                if int(user_input) in numb:
                    one_incorrect = False
                else:
                    print("Number should be in between 1 and 6! Try again!")
            else:
                print("Invalid Input! Try again!")

        comp_input = random.choice(numb)

        if int(user_input) == comp_input:
            one_wickets_lost += 1
            print(f"""
{one_wickets_lost} wickets down
""")
            input("Press any Key to Continue: ")
            if one_wickets_lost == int(wickets):
                one_loop = False
        elif user_input != comp_input:
            first_innings_user.append(int(user_input))
            first_innings_comp.append(comp_input)

        if one_batting == "User":
            one_score = sum(first_innings_user)
        elif one_batting == "Comp":
            one_score = sum(first_innings_comp)

        print(f"""
UserInput: {user_input}                   ComputerInput: {comp_input}
BattingScore: {one_score}/{one_wickets_lost}

""")

        if one_loop == False:
            print("""
First Innings Over
            """)
    return one_score


def second_innings(one_batting, one_score, wickets):
    second_innings_user = []
    second_innings_comp = []
    numb = [1, 2, 3, 4, 5, 6]
    two_wickets_lost = 0
    two_loop = True
    while two_loop == True:

        two_incorrect = True
        while two_incorrect:
            user_input = input("Type your number: ")
            if user_input.isnumeric():
                if int(user_input) in numb:
                    two_incorrect = False
                else:
                    print("Number should be in between 1 and 6! Try again!")
            else:
                print("Invalid Input! Try again!")

        comp_input = random.choice(numb)

        if int(user_input) == int(comp_input):
            two_wickets_lost += 1
            print(f"""
{two_wickets_lost} wickets down
""")
            input("Press any Key to Continue: ")
            if two_wickets_lost == int(wickets):
                two_loop = False
                if one_batting == "User":
                    winner = "User"
                elif one_batting == "Comp":
                    winner = "Computer"
        elif user_input != comp_input:
            second_innings_user.append(int(user_input))
            second_innings_comp.append(comp_input)

        if one_batting == "User":
            two_score = sum(second_innings_comp)
        elif one_batting == "Comp":
            two_score = sum(second_innings_user)

        print(f"""
UserInput: {user_input}                   ComputerInput: {comp_input}
BattingScore: {two_score}/{two_wickets_lost}
""")

        if one_batting == "Comp" and two_score > one_score:
            # print("User Won")
            winner = "User"
            break
        elif one_batting == "User" and two_score > one_score:
            # print("Computer Won")
            winner = "Computer"
            break
    return two_score, winner

input("Press any key to Begin: ")

print("""
-------------------
The Game Begins Now
-------------------
""")

incorrect = True
while incorrect:
    wickets = input("Select Number of Wickets: ")
    if wickets.isnumeric():
        if int(wickets) in range(1, 11):
            incorrect = False
        else:
            print("Select Wickets between 1 and 10")
    else:
        print("Please Enter a Numeric Value")

toss_incorrect = True
while toss_incorrect:
    head_or_tail = input("Select Head or Tail (H/T): ")
    if head_or_tail == "H" or head_or_tail == "T":
        toss_incorrect = False
    else:
        print("Invalid Input! Try Again")


toss_result = toss()
input_bat_or_chase, user_won_toss = select_bat_or_chase(toss_result, head_or_tail)
one_batting = first_batting(input_bat_or_chase, user_won_toss)
print("""
--------------------
First Innings Begins
--------------------
""")

one_score = first_innings(one_batting, wickets)

print(f"""
---------------------
Second Innings Begins
---------------------

Score To Chase: {one_score}
""")

two_score, winner = second_innings(one_batting, one_score, wickets)

print(f"""
{winner} Wins!!!
""")





