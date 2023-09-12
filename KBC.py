q = ["What is the approximate amount of people currently living on earth?", """What is the name of the layer of earth on
 which we are living?""", "What is another name for the Antarctic Ocean?", "What is the name of our galaxy?", """Are 
Cartoons and Anime the same thing?""", "Who presented the 'Two-Nation Theory'?", "What is Pakistan's national animal?"]
ans_choice = ["A. 9 billion, B. 8 billion, C. 7 billion", "A. Core, B. Mantle C. Crust", """A. Eastern Ocean,
 B. Southern Ocean, C. Northern Ocean""", "A. Andromeda, B. Milky Way, C. Solar Star", "A. Yes, B. No", """A. Sir Syed
 Ahmed Khan, B. Quaid e Azam, C. Allama Iqbal""", "A. Parrot, B. Markhor, C. Bull "]

print("This is the game of \"Kaun Banega Crorepati\"\n\n")


# Q.1
print(q[0], "\n", ans_choice[0])
interaction1 = input("Answer: ")
money_won = "0rs"
if interaction1 == "b" or interaction1 == "B" or interaction1 == "8 billion":
    print("Correct!")
    print("You have won 10,000rs with this question.")
    print(f"If you get the next question wrong, you will leave with {money_won}!\n")
else:
    print("Incorrect!")
    print("You did not win any money.")
    print("Come prepared next time!")
    quit()

# Q.2
print(q[1], "\n", ans_choice[1])
interaction2 = input("Answer: ")
money_won = "60,000rs"
if interaction2 == "c" or interaction2 == "C" or interaction2 == "Crust":
    print("Correct!")
    print("!! Checkpoint Reached !!")
    print(f"You have won {money_won} with this question.")
    print(f"If you get the next question wrong, you will leave with {money_won}!\n")
else:
    print("Incorrect!")
    print(f"You won 0rs.")
    quit()
# Q.3
print(q[2], "\n", ans_choice[2])
interaction3 = input("Answer: ")
if interaction3 == "b" or interaction3 == "B" or interaction3 == "Southern Ocean":
    print("Correct!")
    print(f"You have won 100,000rs with this question.")
    print(f"If you get the next question wrong, you will leave with {money_won} \n")
else:
    print("Incorrect!")
    print("You won 60,000rs.")
    quit()

# Q.4
print(q[3], "\n", ans_choice[3])
interaction4 = input("Answer: ")
money_won = "180,000rs"
if interaction4 == "b" or interaction4 == "B" or interaction4 == "Milky Way":
    print("Correct!")
    print("!! Checkpoint Reached !!")
    print("You have won 180,000rs with this question.")
    print(f"If you get the next question wrong, you will leave {money_won}\n")
else:
    print("Incorrect!")
    print("You won 60,000rs.")
    quit()

# Q.5
print(q[4], "\n", ans_choice[4])
interaction5 = input("Answer: ")
if interaction5 == "b" or interaction5 == "B" or interaction5 == "No":
    print("Correct!")
    print("You have won 250,000rs with this question.")
    print(f"If you get the next question wrong, you will leave with {money_won}!\n")
else:
    print("Incorrect!")
    print(f"You won {money_won}.")
    quit()

# Q.6
print(q[5], "\n", ans_choice[5])
interaction6 = input("Answer: ")
money_won = "300,000rs"
if interaction6 == "c" or interaction6 == "C" or interaction6 == "Allama Iqbal":
    print("Correct!")
    print("!! Checkpoint Reached !!")
    print("You have won 300,000rs with this question.")
    print(f"If you get the next question wrong, you will leave with {money_won}!\n")
else:
    print("Incorrect!")
    print("You won 250,000rs.")
    quit()

# Q.7
print(q[6], "\n", ans_choice[6])
interaction7 = input("Answer: ")
money_won = "500,000rs"
if interaction7 == "b" or interaction7 == "B" or interaction7 == "Markhor":
    print("Correct!")
    print("You have won 500,000rs with this question.")
else:
    print("Incorrect!")
    print(f"You won {money_won}.")
    quit()

print("You are now A CROREPATI")
