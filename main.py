import turtle
import os
word = input("Choose a secret word: ")
clear = "\n" * 100
print (clear)
progress = []
count = 0
halt = False

bool_1 = bool_2 = bool_3 = bool_4 = bool_5 = bool_6 = bool_7 = bool_8 = True

wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.forward(100)
t.forward(-50)
t.left(90)
t.forward(250)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)

for i in word:
    progress.append('_')

def check_answer():
    global count
    global word
    if  str(letter) not in word:
        print("Sorry, that is not a letter in this word")
        count += 1
    else:
        index = word.index(str(letter))
        progress[int(index)] = str(letter)
        word = word.replace(str(letter), " ", 1)


def draw():
    global bool_1
    global bool_2
    global bool_3
    global bool_4
    global bool_5
    global bool_6
    global bool_7
    global bool_8
    if count == 1 and bool_1 == True:
        t.penup()
        t.forward(50)
        t.right(90)
        t.pendown()
        t.circle(-25)
        bool_1 = False
    elif count == 2 and bool_2 == True:
        t.left(90)
        t.forward(80)
        bool_2 = False
    elif count == 3 and bool_3 == True:
        t.forward(-55)
        t.left(50)
        t.forward(35)
        bool_3 = False
    elif count == 4 and bool_4 == True:
        t.forward(-35)
        t.right(100)
        t.forward(35)
        bool_4 = False
    elif count == 5 and bool_5 == True:
        t.forward(-35)
        t.left(50)
        t.forward(55)
        t.right(30)
        t.forward(50)
        bool_5 = False
    elif count == 6 and bool_6 == True:
        t.forward(-50)
        t.left(70)
        t.forward(55)
        bool_6 = False
    elif count == 7 and bool_7 == True:
        t.left(35)
        t.forward(10)
        bool_7 = False
    elif count == 8 and bool_8 == True:
        t.forward(-10)
        t.right(35)
        t.forward(-55)
        t.right(70)
        t.forward(55)
        t.right(35)
        t.forward(10)
        bool_8 = False

def check_win():
    global word
    if "_" not in progress:
        print("Congratulations! You won with " + str(count) + " incorrect guesses.")
        halt = True


while "_" in progress:
    letter = input("Choose a letter to see if it is in the word: ")

    check_answer()
    for i in progress:
        print(i)
    draw()
    check_win()
    if halt == True:
        break
    if count == 8:
        print("Sorry, you've lost. The word was " + word)
        break














