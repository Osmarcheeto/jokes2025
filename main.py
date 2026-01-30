# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
topics = ["robbers", "tanks", "pencils"]

# Function to tell a joke (abstraction)
def tell_joke(topic):
    if topic == "robbers":
        setup = "Calder"
        punchline = "Calder police — I've been robbed!"
    elif topic == "tanks":
        setup = "Tank"
        punchline = "You're welcome!"
    else:
        setup = "Broken pencil"
        punchline = "Nevermind, it's pointless!"

    input("Knock knock... ")
    input(setup + "... ")
    print(punchline)

# Function to get a valid answer
def choose(prompt, options):
    answer = input(prompt).lower()
    while answer not in options:
        answer = input(prompt).lower()
    return answer

# Start
play = choose("Do you want to hear a joke? (yes/no) ", ["yes", "no"])

if play == "yes":
    again = "yes"
    while again == "yes":
        topic = choose("Pick a topic (robbers/tanks/pencils): ", topics)
        tell_joke(topic)
        again = choose("Another joke? (yes/finito) ", ["yes", "finito"])

    rating = int(input("Rate the game 1–10: "))
    print("Satisfaction:", rating * 10, "%")

    recommend = choose("Recommend to a friend? (yes/maybe/no) ",
                       ["yes", "maybe", "no"])

    if recommend in ["yes", "maybe"]:
        print("Thank you!")
    else:
        print("Sorry you didn’t like it.")
else:
    print("Okay, maybe next time!")
