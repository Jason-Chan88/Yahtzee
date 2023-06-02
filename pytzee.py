"""
File: pytzee.py
Author: Jason Chan
Description: It's a game of Yahtzee but single player instead of two
"""
import random

TOTAL_DICE = 5
DICE_FACEs = 6  # these are the constants aka dice


def roll_dice():
    """"
    It gets the 5 dice number that we need for the game
    :param: none
    :return: a list containing 5 integers representing dice rolls between 1 and 6
    """""

    roll_list = []
    for i in range(TOTAL_DICE):  # this gets 5 random number for your dice for each round
        roll_list.append(random.randint(1, 6))
    return roll_list  # returns the roll list


def scoring():
    """"
        Scores everything that you want to be scored
        :param: 
        :return: score which contains all these score in it
        """""

    ones_count = 0
    twos_count = 0
    threes_count = 0  # all these counts are for the dice that show up in your roll, and it allows me to score
    # everything
    fours_count = 0
    fives_count = 0
    sixes_count = 0

    small_straight_amount = 0
    large_straight_amount = 0
    full_house_amount = 0  # all these amount relate to a fixed increase of the score
    yahtzee_amount = 0
    bonus_amount = 0

    bonus_on = False

    print("    Your score is:", sum(final_score))  # this is showing u your score before everything starts so 0

    x = roll_dice()  # made roll dice into a variable so we can use a for loop to go through it
    print(*x)  # prints your 5 dice

    for i in x:
        if i == 1:
            ones_count += 1
        elif i == 2:
            twos_count += 1
        elif i == 3:
            threes_count += 1  # this counts the amount of a number in the roll dice
        elif i == 4:
            fours_count += 1
        elif i == 5:
            fives_count += 1
        elif i == 6:
            sixes_count += 1

    run = False
    while not run:  # while loop to ask what you want to do
        num_count = input("How would you like to count this dice roll? ")

        if num_count not in your_choice:  # if your option hasn't been chosen yet than you are allowed to run the
            # code for it or you get a message to choose another
            run = True

            while num_count == "" or num_count != "skip" and num_count != "count 1" and num_count != "count 2"\
                    and num_count != "count 3" and num_count != "count 4" and num_count != "count 5" \
                    and num_count != "count 6" and num_count != "three of a kind" and num_count != "3 of a kind"\
                    and num_count != "four of a kind" and num_count != "4 of a kind" and num_count != "full house" \
                    and num_count != "small straight" and num_count != "large straight" and num_count != "chance"\
                    and num_count != "yahtzee":
                # People can't just press enter
                print("Say skip if you want to skip")
                num_count = input("How would you like to count this dice roll? ")

            if num_count == "three of a kind" or num_count == "3 of a kind":
                if ones_count >= 3 or twos_count >= 3 or threes_count >= 3 or fours_count >= 3 or fives_count >= 3 or \
                        sixes_count == 3:

                    three_of_a_kind_score_card.remove(0)
                    choice(num_count)  # this code allow you to check three of a kind, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after
                    # getting the sum of the list
                    three_of_a_kind_score.append(sum(x))
                    three_of_a_kind_score_card.append(sum(x))
                    score.append(sum(three_of_a_kind_score))
                    your_choice.append(num_count)

            elif num_count == "four of a kind" or num_count == "4 of a kind":
                if ones_count >= 4 or twos_count >= 4 or threes_count >= 4 or fours_count >= 4 or fives_count >= 4 or \
                        sixes_count >= 4:

                    four_of_a_kind_score_card.remove(0)
                    choice(num_count)  # this code allow you to check four of a kind, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after
                    # getting the sum of the list
                    four_of_a_kind_score.append(sum(x))
                    four_of_a_kind_score_card.append(sum(x))
                    score.append(sum(four_of_a_kind_score))
                    your_choice.append(num_count)

            elif num_count == "count 1":

                if ones_count == 0:
                    print("It's not in dice roll")

                else:
                    ones_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 1, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    ones_score.append(1 * ones_count)
                    ones_score_card.append(1 * ones_count)
                    score.append(sum(ones_score))
                    bonus_counter.append(sum(ones_score))
                    your_choice.append(num_count)

            elif num_count == "count 2":

                if twos_count == 0:
                    print("It's not in dice roll")

                else:
                    twos_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 2, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    twos_score.append(2 * twos_count)
                    twos_score_card.append(2 * twos_count)
                    score.append(sum(twos_score))
                    bonus_counter.append(sum(twos_score))
                    your_choice.append(num_count)

            elif num_count == "count 3":

                if threes_count == 0:
                    print("It's not in dice roll")

                else:
                    threes_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 3, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    threes_score.append(3 * threes_count)
                    threes_score_card.append(3 * threes_count)
                    score.append(sum(threes_score))
                    bonus_counter.append(sum(threes_score))
                    your_choice.append(num_count)

            elif num_count == "count 4":

                if fours_count == 0:
                    print("It's not in dice roll")

                else:
                    fours_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 4, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    fours_score.append(4 * fours_count)
                    fours_score_card.append(4 * fours_count)
                    score.append(sum(fours_score))
                    bonus_counter.append(sum(fours_score))
                    your_choice.append(num_count)

            elif num_count == "count 5":

                if fives_count == 0:
                    print("It's not in dice roll")

                else:
                    fives_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 5, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    fives_score.append(5 * fives_count)
                    fives_score_card.append(5 * fives_count)
                    score.append(sum(fives_score))
                    bonus_counter.append(sum(fives_score))
                    your_choice.append(num_count)

            elif num_count == "count 6":

                if sixes_count == 0:
                    print("It's not in dice roll")

                else:
                    sixes_score_card.remove(0)
                    choice(num_count)
                    # this code allow you to check count 1, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after doing
                    # the equation also put in a part if it's not in dice roll it prints not in dice roll
                    sixes_score.append(6 * sixes_count)
                    sixes_score_card.append(6 * sixes_count)
                    score.append(sum(sixes_score))
                    bonus_counter.append(sum(sixes_score))
                    your_choice.append(num_count)

            elif num_count == "small straight":

                if ones_count >= 1 and twos_count >= 1 and threes_count >= 1 and fours_count >= 1 \
                        or twos_count >= 1 and threes_count >= 1 and fours_count >= 1 and fives_count >= 1 \
                        or threes_count >= 1 and fours_count >= 1 and fives_count >= 1 and sixes_count >= 1:

                    small_straight_score_card.remove(0)
                    choice(num_count)
                    small_straight_amount += 30
                    # this code allow you to check small straight, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after
                    # putting in the amount
                    small_straight_score.append(small_straight_amount)
                    small_straight_score_card.append(small_straight_amount)
                    score.append(sum(small_straight_score))
                    your_choice.append(num_count)

            elif num_count == "large straight":

                if ones_count >= 1 and twos_count >= 1 and threes_count >= 1 and fours_count >= 1 and fives_count >= 1 \
                        or twos_count >= 1 and threes_count >= 1 and fours_count >= 1 and fives_count >= 1 and \
                        sixes_count >= 1:

                    large_straight_score_card.remove(0)
                    choice(num_count)
                    large_straight_amount += 40
                    # this code allow you to check large straight, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after
                    # putting in the amount
                    large_straight_score.append(large_straight_amount)
                    large_straight_score_card.append(large_straight_amount)
                    score.append(sum(large_straight_score))
                    your_choice.append(num_count)

            elif num_count == "full house":

                if (ones_count >= 3 and twos_count >= 2 or threes_count >= 2 or fours_count >= 2 or fives_count >= 2
                    or sixes_count >= 2) or \
                        (
                        twos_count >= 3 and ones_count >= 2 or threes_count >= 2 or fours_count >= 2 or fives_count >= 2
                        or sixes_count >= 2) or \
                        (
                        threes_count >= 3 and twos_count >= 2 or ones_count >= 2 or fours_count >= 2 or fives_count >= 2
                        or sixes_count >= 2) or \
                        (
                        fours_count >= 3 and twos_count >= 2 or threes_count >= 2 or ones_count >= 2 or fives_count >= 2
                        or sixes_count >= 2) or \
                        (
                        fives_count >= 3 and twos_count >= 2 or threes_count >= 2 or fours_count >= 2 or ones_count >= 2
                        or sixes_count >= 2) or \
                        (
                        sixes_count >= 3 and twos_count >= 2 or threes_count >= 2 or fours_count >= 2 or
                        fives_count >= 2 or ones_count >= 2):
                    full_house_score_card.remove(0)
                    choice(num_count)
                    full_house_amount += 25
                    # this code allow you to check full house, put it on your
                    # scoreboard, takes it away as one of your choices,also put it towards your final score after
                    # putting in the amount
                    full_house_score.append(full_house_amount)
                    full_house_score_card.append(full_house_amount)
                    score.append(sum(full_house_score))
                    your_choice.append(num_count)

            elif num_count == "chance":

                chance_score_card.remove(0)
                choice(num_count)  # this code allow you to check chance, put it on your
                # scoreboard, takes it away as one of your choices,also put it towards your final score after
                # putting in the amount
                chance_score.append(sum(x))
                chance_score_card.append(sum(x))
                score.append(sum(chance_score))
                your_choice.append(num_count)

            elif num_count == "yahtzee":

                if ones_count >= 5 or twos_count >= 5 or threes_count >= 5 or fours_count >= 5 or fives_count >= 5 or \
                        sixes_count >= 5:
                    del yahtzee_score_card[0]
                    choice(num_count)
                    yahtzee_amount += 50  # this code allow you to check yahtzee when you get it the first time,
                    # put it on your scoreboard, also put it towards your final score with adding 50 the first time,
                    # also you can do yahtzee as many times as you want
                    yahtzee_score.append(yahtzee_amount)
                    yahtzee_count.append(yahtzee_amount)
                    yahtzee_score_card.append(sum(yahtzee_count))
                    score.append(sum(yahtzee_count))

                    if 2 <= len(yahtzee_count):
                        del yahtzee_score_card[0]
                        yahtzee_amount = 50  # this code allow you to check yahtzee when you get it the more than one
                        # time, puts it on your scoreboard, also put it towards your final score with adding 100
                        # everytime after the first one
                        yahtzee_score.append(yahtzee_amount)
                        yahtzee_count.append(yahtzee_amount)
                        yahtzee_score_card.append(sum(yahtzee_score))

            if sum(bonus_counter) >= 63 and bonus_on == False:
                choice(num_count)
                bonus_amount += 35  # this tracks bonus which happen after 1's, 2's, 3's, 4's, 5's, and 6's
                # equal 63 after you get a one time + 35 to your overall score
                bonus_score.append(bonus_amount)
                score.append(sum(bonus_score))

                bonus_on = True

        else:
            print("This command has been already used")  # this happens when it's already in your choice

    return score  # returns the score


def play_game(num_rounds):
    """"
        Tells you the round you are on
        :param: num_rounds
        :return: none
    """""
    print("***** Beginning Round", num_rounds, "*****")  # the beginning of what round you on


def score_card():  # the score of everything you put in
    """"
        Prints all the score for you to see
        :param: none
        :return: none
    """""
    print("    Scorecard")
    print("1's", "2's", "3's", "4's", "5's", "6's")
    print(*ones_score_card, " ",
          *twos_score_card, " ",
          *threes_score_card, " ",
          *fours_score_card, " ",
          *fives_score_card, " ",
          *sixes_score_card)
    print("Three of a Kind", "Four of a Kind", "Full House", "Small Straight", "Large Straight", "Yahtzee", "Chance")
    print("            ", *three_of_a_kind_score_card, "           ",
          *four_of_a_kind_score_card, "       ",
          *full_house_score_card, "           ",
          *small_straight_score_card, "           ",
          *large_straight_score_card, "    ",
          *yahtzee_score_card, "   ",
          *chance_score_card)


def choice(num_count):
    """"
       Prints that your choice was accepted
        :param: num count so it can print the num count
        :return: none
    """""
    print("accepted", num_count)  # when you put in a num count that not in your choic than it says this


if __name__ == '__main__':

    num_rounds = 1  # the round you are on

    your_choice = []  # tracks all your choices with dice roll

    ones_score_card = [0]
    twos_score_card = [0]
    threes_score_card = [0]  # these are list for scoreboard
    fours_score_card = [0]
    fives_score_card = [0]
    sixes_score_card = [0]

    three_of_a_kind_score_card = [0]
    four_of_a_kind_score_card = [0]
    full_house_score_card = [0]
    small_straight_score_card = [0]
    large_straight_score_card = [0]  # these are list for scoreboard
    chance_score_card = [0]
    yahtzee_score_card = [0]

    bonus_counter = []  # tracks all the !'s, 2's, 3's, 4's, 5's, 6's for the bonus score

    yahtzee_count = []  # this is for counting the amount of times you use yahtzee

    final_score = []  # this is the score you have after every round

    number_rounds = int(input("What is the number of rounds that you want to play? "))  # number of rounds this goes for

    seed = int(input("Enter the seed or 0 to use a random seed: "))
    if seed:  # it's like minecraft gives you a bunch of options roll dice
        random.seed(seed)

    while num_rounds <= number_rounds:  # keeps the entire thing running for however many rounds you put

        ones_score = []
        twos_score = []
        threes_score = []
        fours_score = []  # these list track those score and puts them into final score to get your score
        fives_score = []
        sixes_score = []

        three_of_a_kind_score = []
        four_of_a_kind_score = []
        full_house_score = []
        small_straight_score = []  # these list track those score and puts them into final score to get your score
        large_straight_score = []
        chance_score = []
        yahtzee_score = []

        bonus_score = []  # this is hold that plus 35 score

        score = []  # all the score goes into this

        play_game(num_rounds)
        s = scoring()  # calling the function that we needed
        score_card()

        final_score.append(sum(s))  # gets all the score in the score list and sums them

        num_rounds += 1  # increase everytime we go through the while loop

    print("Your Final Score was", (sum(final_score)))  # get this at the end to show that final score
