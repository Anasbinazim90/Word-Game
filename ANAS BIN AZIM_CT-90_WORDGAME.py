print("\t\t\tANAS'S WORD GUESSING GAME\t\t\t")
print("\t\t\t=========================\t\t\t")
print("\nHey Welcome !!\nThink of a word and Follow the Steps.\nI'll tell you what's going in your mind.\n")
english_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 3
print("COLOUMN #01  COLOUMN #02  COLOUMN #03  COLOUMN #04")
print("===========  ===========  ===========  ===========")
for i in range(0, len(english_alphabets)):
    print("     ", end="")
    print(english_alphabets[i],end="       ")
    if i==count:
        print()
        count=count+4
print()
coloumn1 = []
for a in range(0,26,4):
    coloumn1.append(english_alphabets[a])
coloumn2 = []
for b in range(1,26,4):
    coloumn2.append(english_alphabets[b])
coloumn3 = []
for c in range(2,26,4):
    coloumn3.append(english_alphabets[c])
coloumn4 = []
for d in range(3,26,4):
    coloumn4.append(english_alphabets[d])

user_1st_input = ""

while True:
    n = input("Enter Coloumn # in which your Guessing Word's letter is present one by one then type (next) when done: ")
    if n.lower()== "next":
            break
    if n>="1" and n<="4":
        user_1st_input+=n
    else :
        print("Invalid input\nThere are 4 coloumns, so you enter only four digits i.e 1-4")
        continue
print()
print("1    2    3    4    5    6    7")
for x in user_1st_input :
    if x == "1" :                           # where x are the coloumn numbers which we have entered in first half.
        for y in coloumn1 :         # where "y" are the letters which we have listed before in all
            print(y, end="    ")    # 4 coloumns
        print()
    elif x == "2" :
        for y in coloumn2 :
            print(y, end="    ")
        print()
    elif x == "3" :
        for y in coloumn3 :
            print(y, end="    ")
        print()
    else :
        for y in coloumn4 :
            print(y, end="    ")
        print()

our_guessing_word = ""
for digit in user_1st_input :
    n = int(input("Enter Coloumn # in which your Guessing Word's letter is present one by one : "))
    if n>=1 and n<=7 :
        if n==1 :
            if digit=="1":
                our_guessing_word+=coloumn1[0]
            elif digit=="2":
                our_guessing_word+=coloumn2[0]
            elif digit=="3":
                our_guessing_word+=coloumn3[0]
            else :
                our_guessing_word+=coloumn4[0]
        if n==2 :
            if digit=="1":
                our_guessing_word+=coloumn1[1]
            elif digit=="2":
                our_guessing_word+=coloumn2[1]
            elif digit=="3":
                our_guessing_word+=coloumn3[1]
            else :
                our_guessing_word+=coloumn4[1]
        if n==3 :
            if digit=="1":
                our_guessing_word+=coloumn1[2]
            elif digit=="2":
                our_guessing_word+=coloumn2[2]
            elif digit=="3":
                our_guessing_word+=coloumn3[2]
            else :
                our_guessing_word+=coloumn4[2]
        if n==4 :
            if digit=="1":
                our_guessing_word+=coloumn1[3]
            elif digit=="2":
                our_guessing_word+=coloumn2[3]
            elif digit=="3":
                our_guessing_word+=coloumn3[3]
            else :
                our_guessing_word+=coloumn4[3]
        if n==5 :
            if digit=="1":
                our_guessing_word+=coloumn1[4]
            elif digit=="2":
                our_guessing_word+=coloumn2[4]
            elif digit=="3":
                our_guessing_word+=coloumn3[4]
            else :
                our_guessing_word+=coloumn4[4]
        if n==6 :
            if digit=="1":
                our_guessing_word+=coloumn1[5]
            elif digit=="2":
                our_guessing_word+=coloumn2[5]
            elif digit=="3":
                our_guessing_word+=coloumn3[5]
            else :
                our_guessing_word+=coloumn4[5]
        if n==7 :
            if digit=="1":
                our_guessing_word+=coloumn1[6]
            elif digit=="2":
                our_guessing_word+=coloumn2[6]
            elif digit=="3":
                our_guessing_word+=coloumn3[6]
            else :
                our_guessing_word+=coloumn4[6]
    else:
        print("Invalid input")
        print("There are 7 coloumns, so you enter only seven digits i.e 1-7")
        continue

print("\nTHE WORD YOU HAVE GUESSED IS", our_guessing_word, "!!!")
print("\nSHOCKED ? xD HOPE YOU ENJOYED")
print("=============================")
