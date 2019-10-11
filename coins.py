import os
import random
import argparse
import time

parser = argparse.ArgumentParser(description='Practice coin summation.')
parser.add_argument('--order',
                    dest='order',
                    default='decreasing',
                    help='style (increasing, decreasing, mixed)')
parser.add_argument('--num',
                    dest='ncoins',
                    default=3,
                    type=int,
                    help="number of coins")
parser.add_argument('--rate',
                    dest='rate',
                    default=175,
                    type=int,
                    help="voice speed (175 is normal)")
parser.add_argument('--pause',
                    dest='pause',
                    default=0.5,
                    type=float,
                    help="pause between coins")

args = parser.parse_args()


class Coins:
    max = 6

    def __init__(self):
        self.amt = random.randint(1, self.max)

    def __str__(self):
        if self.amt == 1:
            return self.name
        else:
            return self.name + "s"


class Pennies(Coins):
    max = 9
    name = "penny"
    val = 1


class Nickles(Coins):
    name = "nickle"
    val = 5


class Dimes(Coins):
    name = "dime"
    val = 10


class Quarters(Coins):
    name = "quarter"
    val = 25


class HalfDollars(Coins):
    name = "half dollar"
    val = 50
    max = 3


COINS = [Pennies, Nickles, Dimes, Quarters, HalfDollars]


def say(msg):
    os.system(f"say --rate {args.rate} '{msg}'")
    time.sleep(args.pause)
    # print(msg)


while True:
    coin_pos = random.sample(range(len(COINS)), args.ncoins)
    if args.order == "increasing":
        coin_pos.sort()
    elif args.order == "decreasing":
        coin_pos.sort(reverse=True)
    coins = [COINS[coin]() for coin in coin_pos]
    total = sum([coin.amt * coin.val for coin in coins])

    while True:
        for coin in coins:
            say(f"{coin.amt} {coin}")

        guess = input("total> ")
        try:
            guess = int(guess)
            if guess == total:
                break
            else:
                say("try again")

        except ValueError:
            pass

    say("correct")
