# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.
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

    # NEW FOR-LOOP ADDED HERE
    for topic in topics:
        print("\nLet's try a joke about:", topic)
        tell_joke(topic)

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
