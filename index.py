from time import *
import random as r


def mistakecalculator(para,user):
    error = 0
    for i in range(len(para)):
        try:
            if para[i] !=user[i]:
                error = error + 1
        except :
            error = error + 1
    return error


def  timing(s_time, e_time, userinput):
    time_delay = e_time - s_time
    time_r = round(time_delay,2)
    speed = len(userinput)/time_r
    return round(speed)          
        
while True:
    ck = input("Are you ready : yes/no :")
    if ck == "yes":
        test = ["Now that you have a feeling for the keyboard and typing easy words, you will move on to full sentences with capitalization.",
        "One of the secrets to fast typing is maintaining a rhythm as you type.","This typing test is based on a randomly selected words taken",
        "You can practice your typing skills here. Typing speed practice tests with the most common English words.",
        "This online typing test tracks your errors, your mistakes and even lets you correct your mistakes as you go.",
        "Improve your typing speed and accuracy online with the words that you type every day. "]
        string1 = r.choice(test)
        print("                Test your typing speed              ")
        print(string1)

        print()
        print()
        time_1 = time()
        stringinput = input("Type here : ")
        time_2 = time()
        print("Your speed : ", timing(time_1, time_2, stringinput),"w/sec")
        print("Error : ", mistakecalculator(string1,stringinput))
    elif ck == "no":
        print("Thank You")
        break

    else:
        print("Wrong Input")

    



