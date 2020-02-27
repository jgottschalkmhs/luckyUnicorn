# Lucky Unicorn

import random

# Check that number is valid

def intcheck(question, low, high):
    valid = False
    while not valid:
            error = "Please enter an integer between {} and {}".format(low, high)

            try:
                response = int(input("Enter an integer between {} and {}: ".format(low, high)))

                if low <= response <= high:
                    return response
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)


# main routine goes here

total = intcheck("Enter a number between 1 and 15:", 1, 20)

how_much = total
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]

unicorn_count = 0
donkey_count = 0
zebhor_count = 0

keep_going = ""
while keep_going == "":

    chosen = random.choice(tokens)

    # Adjust total correctly for a given token
    if chosen == "unicorn":
        unicorn_count += 1
        total += 5
        feedback = "Congratulations, you won $5.00"
    elif chosen == "donkey":
        donkey_count += 1
        total -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        zebhor_count += 1
        total -= 0.5
        feedback = "Congratulations, you won 50c"

    print()

    print(feedback)
    print("You have ${} to play with".format(total))

    if total < 1:
        print()
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

# End screen
winnings = total

print()
print("**** You Got a Total of: ****")
print("# Unicorns: {}".format(unicorn_count))
print("# Zebra / Horses: {}".format(zebhor_count))
print("# Donkeys: {}".format(donkey_count))

print()
print("You spent ${}".format(how_much))
print("You go home with ${:.2f}".format(winnings))
