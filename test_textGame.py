import time #Imports a module to add a pause
import sys #imports a module for various system functions
import random #imports a module to produce randomized output

#variables to be used in the game:

#input variables:

A = ["A", "a"]
B = ["B", "b"]
C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]

#character variables:

name = input("What's your name? ") #Stores the users name as the main character
mayor = ["Mayor Syn Tacks, the resident Python Master of Tin Town"]
knights = ["Lady Sally", "Sir Notalance", "Lady Braketts"]

#item variables:

sword = ["sword", "Sword", "the sword", "The sword"]
staff = ["staff", "Staff", "the staff", "The staff"]
drum = ["drum", "Drum", "the drum", "The drum"]

#instructing user on which keys to use:

quizRequired = ("\nUse only t, T, true, True, f, F, false, or False.")
storyRequired = ("\nUse only a, b, or c\n") 
contRequired = ("\nUse only Y or N")
itemRequired = ("\nUs only Sword, Staff, or Drum")

###The following generates a random meal:

def meal():
    menuItem = random.randint(1,8)
    if menuItem == 1:
        print("duck con fit")
    if menuItem == 2:
        print("peanut butter & jelly sandwiches")
    if menuItem == 3:
        print("venison stew")
    if menuItem == 4:
        print("rabbit haunch and salad")
    if menuItem == 5:
        print("chicken noodle soup")
    if menuItem == 6:
        print("seal tartare")
    if menuItem == 7:
        print("cabbage rolls")
    if menuItem == 8:
        print("macaroni salad")



###Below are the Quiz functions, which are called after in the Story section###
def quiz1():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n1. Python is an object-oriented programming language.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 2.\n
-----------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
-----------------------------------------""")
        quiz1()
    else:
        print(quizRequired)
        quiz1()
    time.sleep(1)

def quiz2():
    print ("\n2. Python was named after the non-venomous snake.")
    choice = input(">")
    if choice in false:
        print("""Correct! It was named after the British comedy group, Monty Python. You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is True! It was named after the British comedy group, Monty Python. Please try again.\n
++++++++++++++++++++++++++++++++++++++++++""")
        quiz2()
    else:
        print(quizRequired)
        quiz2()
    time.sleep(1)

def quiz3():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n3. Boolean values are True and False, which equal 1 and 0 respectively.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to question 4.\n
------------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
------------------------------------------""")
        quiz3()
    else:
        print (quizRequired)
        quiz3()
    time.sleep(1)

def quiz4():
    print ("\n4. You can store the same variable globally and locally.")
    choice = input(">")
    if choice in false:
        print("""Correct! You may continue with the story.\n
+++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is False! Please try again.\n
+++++++++++++++++++++++++++++++++++++++++""")
        quiz4()
    else:
        print (quizRequired)
        quiz4()
    time.sleep(1)

def quiz5():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n5. The statement: Spam = ['ham', 'eggs', 'bacon', 'marble cake'] is an example of a list.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 6.\n
-----------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
-----------------------------------------""")
        quiz5()
    else:
        print (quizRequired)
        quiz5()
    time.sleep(1)

def quiz6():
    print ("\n6. In question 5, you can insert the item 'hamster' by using the script: Spam.append('hamster')")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue with the story.\n
+++++++++++++++++++++++++++++++++++++++++++++++++ """)
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
+++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz6()
    else:
        print (quizRequired)
        quiz6()
    time.sleep(1)

def quiz7():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n7. Let's say you want your hamster before your eggs.")
    time.sleep(2)
    print("You can do this using the code:")
    time.sleep(2)
    print("Spam.append(1, 'hamster')")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 8.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. You use Spam.insert('1, hamster'). Please try again.\n
------------------------------------------------""")
        quiz7()
    else:
        print(quizRequired)
        quiz7()
    time.sleep(1)

def quiz8():
    print ("\n8. You are given the following list:")
    time.sleep(2)
    print ("list = ([1, 2, 3, 4], ['one', 'two', 'three', 'four']")
    time.sleep(2)
    print ("The code 'print(list[1, 0])' returns the output '2, 'one'.")
    choice = input(">")
    if choice in false:
        print("""Correct! Please continue with the story.\n
+++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The output is 'one'! Please try again.\n
+++++++++++++++++++++++++++++++++++++++++++++++++""")
    else:
        print(quizRequired)
        quiz8()
    time.sleep(1)

def quiz9():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n9. The following is an example of a tuple:")
    time.sleep(2)
    print("myTuple = (1, 2.0, 'three', 4.12)")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 10.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
------------------------------------------------""")
        quiz9()
    else:
        print(quizRequired)
        quiz9()
    time.sleep(1)

def quiz10():
    print ("\n10. To insert a new item, '5ive', into the tuple from Question 9, use the code:") #this is a trick question >:)
    time.sleep(2)
    print("myTuple.append('5ive')")
    choice = input(">")
    if choice in false:
        print("""Correct! You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. Tuples are immutable, and can't be changed. Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz10()
    else:
        print(quizRequired)
        quiz10()
    time.sleep(1)

def quiz11():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n11. A dictionary is a data type similar to lists and tuples, except that they use keys rather than integers as a data type.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 12.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
------------------------------------------------""")
        quiz11()
    else:
        print (quizRequired)
        quiz11()
    time.sleep(1)

def quiz12():
    print ("\n12. The following is an example of proper structure and syntax for a dictionary:")
    time.sleep(2)
    print("myDict = {'Hair Length': 'medium', 'Hair Colour': 'red', 'Hair Texture': 'curly'}")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz12()
    else:
        print (quizRequired)
        quiz12()
    time.sleep(1)

def quiz13():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n13. Dictionaries, like lists, have a strict order of items:")
    time.sleep(2)
    print("myDict = {'Hair Length': 'medium', 'Hair Colour': 'red', 'Hair Texture': 'curly') is NOT the same as:")
    time.sleep(2)
    print("myDict = {'Hair Texture': 'curly', 'Hair Length': 'medium', 'Hair Colour': 'red'")
    choice = input(">")
    if choice in false:
        print("""Correct! You may continue to Question 14.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. Dictionary items can be written in any order and still be the same dictionary. Please try again.\n
------------------------------------------------""")
        quiz13()
    else:
        print (quizRequired)
        quiz13()
    time.sleep(1)
                   
def quiz14():
    print ("\n14. Among other popular apps and programs, YouTube was scripted in Python.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz14()
    else:
        print (quizRequired)
        quiz14()
    time.sleep(1)

def quiz15():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n15. IoT stands for Information of Technology.")
    choice = input(">")
    if choice in false:
        print("""Correct! You may continue to Question 16.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. IoT stands for Internet of Things! Please try again.\n
------------------------------------------------""")
        quiz15()
    else:
        print(quizRequired)
        quiz15()
    time.sleep(1)

def quiz16():
    print("\n16. Github is an excellent place to host your own programs and software, as well as their documentation.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz16()
    else:
        print (quizRequired)
        quiz16()
    time.sleep(1)

def quiz17():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n17. Java is another object-oriented programming language that can land you a solid job in computer science.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 18.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
------------------------------------------------""")
        quiz17()
    else:
        print (quizRequired)
        quiz17()
    time.sleep(1)

def quiz18():
    print ("\n18.  To create a class, use the script 'def class():'")
    choice = input(">")
    if choice in false:
        print("""Correct! You may continue with the story.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is False! To create a class, use 'class [className]:', and in the next indented line, define your objects or functions with 'def [object]. Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz18()
    else:
        print(quizRequired)
        quiz18()
    time.sleep(1)

def quiz19():
    print("Kill the virus by answering these two T/F python questions: (use t for true, f for false)")
    print ("\n19. Classes are a useful method to define objects and their functions for use in other Python programs.")
    choice = input(">")
    if choice in true:
        print("""Correct! You may continue to Question 20.\n
------------------------------------------------""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
------------------------------------------------""")
        quiz19()
    else:
        print(quizRequired)
        quiz19()
    time.sleep(1)

def quiz20():
    print ("\n20. PYTHONPATH is an environment variable that tells Python where to locate a module.")
    choice = input(">")
    if choice in true:
        print("""Correct! You are finished the quiz! Feel free to continue with the story!\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
    elif choice in false:
        print("""WRONG. The answer is True! Please try again.\n
++++++++++++++++++++++++++++++++++++++++++++++++""")
        quiz20()
    else:
        print(quizRequired)
        quiz20()
    time.sleep(1)

###Below is the code for the actual game functions####

def intro():
    time.sleep(2)
    print("_____________________________________________\n")
    print("""You are a highly trained hacker called to a town called Tin Town in the kingdom of Datum.
You arrive at the local inn and set your bags on the bed. You hear a knock on the door,
and answer it to find a short old man in a long robe.""")
    time.sleep(3)
    print("'Welcome, " + name + ", to Tin Town. Having just moved in, I'm sure you have many questions.")
    time.sleep(3)
    print("The first one being, who am I?")
    time.sleep(3)
    print("I am Mayor Syn Tacks, and also happen to be the resident Python Master of Tin Town.")
    time.sleep(3)
    print("""Tin Town is a mining town that mines data to update the King's libraries.
Tin Town was recently overrun with a horde of viruses.""")
    time.sleep(3)
    print("""I need you to help us kill each virus before it takes our kingdom's top secret,
highly confidential information and leaks it beyond our borders.""")
    time.sleep(3)
    print(name + ", are you up for this task?'")
    time.sleep(3)
    print("""(Y/N)""")
    choice = input(">")
    if choice in yes:
        print("""'Excellent! Tomorrow we will suit you up to go out and kill those awful viruses!' \n
Mayor Syn Tacks leaves the inn.""")
        time.sleep(3)
        print("zzZZzzZZ")
        time.sleep(3)
        optionProceed()
    elif choice in no:
        print("""'That's truly disappointing. With our nation's valuable information leaked all across the lands,
our enemies will surely destroy us. But I see you've made your choice.""")
        print("Goodbye, " + name + ".'")
    else:
        print(contRequired)
        intro()

def optionProceed():
    print("You awaken the next morning and head to the barracks. There you meet three knights: \n")
    time.sleep(3)
    print(knights[0], knights[1], knights[2])
    time.sleep(3)
    print(knights[0] + ": '" + name + ", these are the weapons and tools you will choose from to ward off the viruses.'")
    time.sleep(3)
    print(knights[1] + ": 'The first choice is a greatsword. Should you choose it, wield it well, as this sword belonged to the King's great-great-grandfather in the great war against the Trojans.'")
    time.sleep(3)
    print(knights[2] + ": 'The second choice is a staff, useful if you're skilled in magic. " + (str(mayor[0])) + " is a Mage, he will be very impressed if you choose this one.'")
    time.sleep(3)
    print(knights[0] + ": 'The third is a drum. We're not quite sure why it's in the armory. Perhaps viruses like music?'")
    time.sleep(3)
    print(knights[1] + ": " + name + ", choose wisely. The wrong choice could be fatal. And if you die, we all die.'")
    time.sleep(3)
    print(knights[0] + ": 'No pressure, though. Stress is a killer too.'\n")
    
    print("Which weapon will you choose?")
    time.sleep(3)
    choice = input(">")
    if choice in sword:
        print(knights[1] + ": 'Ooh, another swordsman. Excellent choice. I will meet you in the training yard.'")
        time.sleep(3)
        optionSword()
    if choice in staff:
        print(knights[2] + ": 'Hey " + (str(knights[0])) + ", I told ya we'd have another Mage!' She turns to you. '" + (str(mayor[0])) + " will meet you in the Mages' Manor this eveing.'")
        time.sleep(3)
        optionStaff()
    if choice in drum:
        print(knights[0] + ": 'I don't know about this, are you sure? ... Well, it's your funeral.'")
        print(knights[2] + ": '" + (str(knights[0])) + ", try having a little faith before you scare " + name + " off, will ya?' She turns to you.\n 'We'll meet you in the yard for a briefing before you leave.'")
        time.sleep(3)
        optionDrum()

def optionSword():
    weapon = ["sword"]
    print("You eat a quick lunch of")
    meal()
    print("in the kitchens and head to the training yard. " + (str(knights[1])) + " is already there waiting.")
    time.sleep(3)
    print(knights[1] + ": 'Good. You're here. Have you ever used a sword before?'")
    time.sleep(3)
    choice = input(">")
    if choice in yes:
        print(knights[1] + ": 'Then let's skip the basics shall we? These viruses don't respond well to physical attacks. Or any attacks, for that matter.'")
        time.sleep(3)
        print(knight[1] + ": 'For some reason after you attack them they'll ask you a question about the programming language, Python, and if you answer correctly, they die.'")
        time.sleep(3)
        print(knight[1] + ": 'Let's practice.'")
        quiz1()
        quiz2()
        time.sleep(3)
        print(knight[1] + ": 'For some reason after you attack the viruses, they'll ask you a question about the programming language, Python, and if you answer correctly, they die.'")
        time.sleep(3)
        print(knight[1] + ": 'Let's practice with this dummy virus.'")
        time.sleep(3)
        print("A creature of indescribable horror runs up to you and " + (str(knight[1])) + " and you leap out with your staff, casting a fire spell and wrapping the virus in a blanket of scorching flame.")
        time.sleep(3)
        print("The horrid creature prints out a string statement. You pick up the sheet of paper and read it: ")
        quiz1()
        quiz2()
        print(knight[1] + " gives you a hard punch in the shoulder. 'Nice work. I'd say you're ready for a real fight. Now, go to the north end of town where you will see an archway leading into the Dank Forest.'")
        print("'There, you will encounter many different viruses and you must defeat them all to restore our town to normal!'")
        time.sleep(3)
    if choice in no:
        print(knights[1] + ": 'Great. Now I have to teach you how to swing a sword, too. Altight. Let's do this.'")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(2)
        print(".")
        time.sleep(3)
        print(knight[1] + ", looking a little tired: 'Alright, not bad for a beginner. Now, the real thing is a lot more interesting.'")
        time.sleep(3)
        print(knight[1] + ": 'For some reason after you attack the viruses, they'll ask you a question about the programming language, Python, and if you answer correctly, they die.'")
        time.sleep(3)
        print(knight[1] + ": 'Let's practice with this dummy virus.'")
        time.sleep(3)
        print("A creature of indescribable horror runs up to you and " + (str(knight[1])) + " and you leap out with your sword, slicing it right down the middle with a powerful swing.")
        time.sleep(3)
        print("The horrid creature prints out a string statement. You pick up the sheet of paper and read it: ")
        quiz1()
        quiz2()
        print(knight[1] + " leaps up and down ecstatically. 'YOU DID IT!! You're ready for the real thing!! Now, go to the north end of town where you will see an archway leading into the Dank Forest.'")
        print("'There, you will encounter many different viruses and you must defeat them all to restore our town to normal!'")
        time.sleep(3)
    optionBegin()
        
            

def optionStaff():
    weapon = ["staff"]
    print("You eat a quick dinner of")
    meal()
    print("in the kitchens and head to the Mages' Manor. " + (str(mayor[0])) + " is already there waiting.")
    time.sleep(3)
    print(mayor[0] + ": 'Good. You're here. Have you ever used a staff before?'")
    time.sleep(3)
    choice = input(">")
    if choice in yes:
        print(mayor[0] + ": 'Then let's skip the basics shall we? These viruses don't respond well to magic attacks. Or any attacks, for that matter.'")
        time.sleep(3)
        print(mayor[0] + ": 'For some reason after you attack them they'll ask you a question about the programming language, Python, and if you answer correctly, they die.'")
        time.sleep(3)
        print("Let's practice with this dummy virus.'")
        time.sleep(2)
        print("A creature of indescribable horror runs up to you and " + (str(mayor[0])) + " and you leap out with your staff, casting a fire spell and wrapping the virus in a blanket of scorching flame.")
        time.sleep(3)
        print("The horrid creature prints out a string statement. You pick up the sheet of paper and read it: ")
        quiz1()
        quiz2()
        print(mayor[0] + " leaps up and down ecstatically. 'YOU DID IT!! You're ready for the real thing!! Now, go to the north end of town where you will see an archway leading into the Dank Forest.'")
        print("'There, you will encounter many different viruses and you must defeat them all to restore our town to normal!'")
        time.sleep(3)
    if choice in no:
        print(mayor[0] + ": 'GADZEUS! Never used a staff before? And you're choosing NOW to try? Well, let's get learning. And FAST.'")
        time.sleep(3)
        print(".")
        time.sleep(3)
        print(".")
        time.sleep(3)
        print(".")
        time.sleep(3)
        print(".")
        time.sleep(3)
        print(".")
        time.sleep(3)
        print(mayor[0] + " wipes sweat off his brow with a handkerchief. 'You're not too shabby for a first timer. Now let's practice as if we're attacking real viruses.'")
        time.sleep(3)
        print(mayor[0] + ": 'In the forest by the mines, those viruses only receive damage if you answer a quiz question correctly. The quiz is about the Python programming language.")
        time.sleep(3)
        print("Weird, innit? Hohoho! Now, they will attack you and try to suck your brains out! So you have to hit them with a well-timed spell, and then answer their question correctly.")
        time.sleep(3)
        print("Let's practice with this dummy virus.'")
        time.sleep(3)
        print("A creature of indescribable horror runs up to you and " + (str(mayor[0])) + " and you leap out with your staff, casting a fire spell and wrapping the virus in a blanket of scorching flame.")
        time.sleep(3)
        print("The horrid creature prints out a string statement. You pick up the sheet of paper and read it: ")
        quiz1()
        quiz2()
        print(mayor[0] + " leaps up and down ecstatically. 'YOU DID IT!! You're ready for the real thing!! Now, go to the north end of town where you will see an archway leading into the Dank Forest.'")
        print("'There, you will encounter many different viruses and you must defeat them all to restore our town to normal!'")
        time.sleep(3)
    optionBegin()


def optionDrum():
    print("You eat a quick dinner of")
    meal()
    
    print("in the kitchens and head to the yard. " + (str(knights[0])) + " is already there waiting.")
    time.sleep(3)
    print(knights[0] + ": 'Good. You're here. Let's get this over with.'")
    time.sleep(3)
    print(knights[0] + ": 'Then let's skip the basics shall we? These viruses don't respond well to magic attacks. Or any attacks, for that matter.'")
    time.sleep(3)
    print(knight[0] + ": 'For some reason after you attack them they'll ask you a question about the programming language, Python, and if you answer correctly, they die.'")
    time.sleep(3)
    print(knight[0] + ": 'Let's practice.'")
    time.sleep(3)
    print("A creature of indescribable horror runs up to you and " + (str(knights[0])) + " and you leap out with your drum and start beating it furiously.")
    time.sleep(3)
    print("The creature doesn't even seem to notice your incredible percussion and flies straight for your face. It attaches itself to your head and begins sucking all of the information stored in your brain.")
    time.sleep(3)
    print(knights[0] + " pulls out a sword and slashes the virus. It then prints out a string statement and she answers the questions, successfully killing the monster.")
    time.sleep(3)
    print(knight[0] + ": 'WOW! THAT was an amazing fail. Let's go get you an actual weapon.'")
    print("Which weapon will you choose?")
    time.sleep(3)
    choice = input(">")
    if choice in sword:
        print(knights[0] + ": 'Much better. " + (str(knights[1])) + " will meet you in the training yard.'")
        time.sleep(3)
        optionSword()
    elif choice in staff:
        print(knights[0] + ": 'Hey, good choice. " + (str(mayor[0])) + " will meet you in the Mages' Manor this eveing.'")
        time.sleep(3)
        optionStaff()
    else:
        print("Please choose the sword or the staff.")
        time.sleep(3)
        choice = input(">")
        if choice in sword:
            print(knights[0] + ": 'Much better. " + (str(knights[1])) + " will meet you in the training yard.'")
            time.sleep(3)
            optionSword()
        elif choice in staff:
            print(knights[0] + ": 'Hey, good choice. " + (str(mayor[0])) + " will meet you in the Mages' Manor this eveing.'")
            time.sleep(3)
            optionStaff()
        

def optionBegin():
    print("You enter the Dank Forext and darkness surrounds you. Birds and strange frogs make their noises all around you. You can hardly see.")
    time.sleep(3)
    print("Suddenly, to the north east, you hear a piercing scream. Heroically, you dash deeper into the forest towards the sound.")
    time.sleep(3)
    print("You pull out your " + (str(weapon)) + " find three viruses surrounding a younf boy. The viruses see you and the closest one attacks.")
    
        
    
intro()
    
