import random


pres_list = ["Reagan's", "Obama's", "Putin's"]
word_list = ["Fury", "Bunghole", "Eyebrows"]

def type_choice():
    choice = random.random()*10
    print(choice)

    if choice < 3:
        type_one()

    elif choice < 6:
        type_two()

    else:
        type_three()


def type_one():
    print(str(random.choice(pres_list) + " " + random.choice(word_list)))


def type_two():
    print(str(random.choice(pres_list) + " " + random.choice(word_list)))


def type_three():
    print(str(random.choice(pres_list) + " " + random.choice(word_list)))

type_choice()
