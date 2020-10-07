import random
import time


def main():

    print(f"Hi there!\n"
          f"I've generated a random 4 digit number for you.\n"
          f"Let's play a bulls and cows game")

    play = 'g'
    while play == 'g':
        print(f"\nNew game\nEnter number or press 'q' to quit game")
        time_r = timer()
        print(f"You played this game {time_r} seconds .")
        play = input("\nIf you can play new game, press 'g'!")

    else:
        exit()


def timer():
    start_time = time.time()
    game()
    total_time = round(time.time() - start_time)
    return total_time


def game():
    guess_num = num()
    guess = 0
    round_g = True
    while round_g is True:
        guess += 1
        tip = tip_player()
        control = tip_correct(tip)
        if control:
            bulls, cows = game_assess(tip, guess_num)
            round_g = result_r(bulls, cows, guess, tip)
        else:
            print("\nIt's not correct number. GAME OVER ")
            round_g = False


def num():
    seq = [*range(10)]
    num1 = random.choice([*range(1, 10)])
    seq.remove(num1)
    num2 = random.choice(seq)
    seq.remove(num2)
    num3 = random.choice(seq)
    seq.remove(num3)
    num4 = random.choice(seq)

    return num1, num2, num3, num4


def tip_player():
    a = input(">>> ")
    if a == 'q':
        exit()
    return a


def tip_correct(tip):
    try:
        a = tip.count(tip[0])
        b = tip.count(tip[1])
        c = tip.count(tip[2])
    except IndexError:
        return False
    if len(tip) != 4 or a != 1 or b != 1 or c != 1:
        return False
    elif tip.isdigit() is False:
        return False
    else:
        return True


def game_assess(tip, guess_num):
    cows = 0
    bulls = 0
    for i, num in enumerate(tip):
        if int(num) == guess_num[i]:
            bulls += 1
        elif int(num) in guess_num:
            cows += 1

    return bulls, cows


def result_r(bulls, cows, guess, tip):
    if bulls == 4:
        print(f"Correct, you've guessed the right number \"{tip}\" in {guess} guesses!")
        return False

    else:
        print(f"bulls: {bulls}, cows: {cows}")
        return True


main()
