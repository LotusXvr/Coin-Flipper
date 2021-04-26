# Imports

import random
from time import sleep


# Code

def coin_flipper_timer(flip_amount):

    # Prompting how much time to sleep in between coin tosses groups
    time_to_sleep = int(input("Time to sleep in between waves: \n> "))

    # Repeating the groups of coin tossing
    while True:
        print(" ")
        count = 0
        heads = 0
        tails = 0

        # Repeating the coin toss
        while count < flip_amount:
            coin_flip = random.choice(["Head", "Tails"])
            if coin_flip == "Head":
                heads += 1
            if coin_flip == "Tails":
                tails += 1
            print(coin_flip)
            count += 1

        # Waiting time_to_sleep time to repeat the coin toss
        print(f"\n\nThrows: {count} \nTails: {tails} \nHeads: {heads}")
        sleep(time_to_sleep)


def coin_flipper_prompt(flip_amount):

    # Repeating the groups of coin tossing
    while True:
        print(" ")
        count = 0
        heads = 0
        tails = 0

        # Repeating the coin toss
        while count < flip_amount:
            coin_flip = random.choice(["Head", "Tails"])
            if coin_flip == "Head":
                heads += 1
            if coin_flip == "Tails":
                tails += 1
            print(coin_flip)
            count += 1

        print(f"\n\nThrows: {count} \nTails: {tails} \nHeads: {heads}")

        # Prompt the user for continuation
        prompt = str(input("\n\nContinue? (s/n) \n> "))
        if prompt in "sSyY1":
            continue
        else:
            break


def coin_flipper_writer(flip_amount, amount_of_times):

    # Creating and opening the txt to write to
    flips_file = open("FlipCounter.txt", "a")
    flips_file.write(
        f"\n---\n\nThrows per wave: {flip_amount}\nWaves performed: {amount_of_times}\n")

    print("\nWriting...\n")

    # Repeat amount of times the process
    while amount_of_times > 0:
        count = 0
        heads = 0
        tails = 0

        # Repeat the flipping for as long as amount_of_times is over zero
        while count < flip_amount:
            coin_flip = random.choice(["Head", "Tails"])
            if coin_flip == "Head":
                heads += 1
            if coin_flip == "Tails":
                tails += 1

            count += 1

            # if the counter is still smalled then flip_amount, it will continue to throw the coin.
            if count < flip_amount:
                continue
            # if the counter is equal, it will write the result to the txt file
            if count == flip_amount:
                flips_file.write(f"\nTails: {tails} \nHeads: {heads}\n")

        amount_of_times -= 1

    # Closing the file
    flips_file.write(f"\n---\n\n\n\n")
    flips_file.close()
    print("\nDone. \nTxt saved in C:/Users/Lucas/Desktop/VSCode as FlipCounter.txt")


def prompt_answer():
    CoinMode = str(
        input("\n\nSelect coin flipping mode \n1. On timer \n2. On prompt \n3. Write to txt \n> "))

    # prompt the amount of coin flipping per group
    try:
        coin_flips = int(
            input("\n\nEnter the number of coin flips to execute per wave: \n> "))
        coin_flipper_timer(coin_flips)
    except ValueError:
        print("\nError: The input must be a number")

    # Selecting the function the user asked for
    if CoinMode == "1":
        coin_flipper_timer(coin_flips)
    elif CoinMode == "2":
        coin_flipper_prompt(coin_flips)
    elif CoinMode == "3":
        try:
            # Number of groups of coin tossing to write to the txt
            number_of_times = (
                int(input("Number of times waves performed: \n> ")))
        except ValueError:
            print("\nError: The input must be a number")
        coin_flipper_writer(coin_flips, number_of_times)
    else:
        print("\nInput must only be either 1, 2 or 3")


# Starting the program
prompt_answer()
