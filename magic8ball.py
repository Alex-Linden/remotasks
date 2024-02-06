
import random

# # List of responses a magic 8-ball might give
# responses = [
#     "Signs point to yes.",
#     "Reply hazy, try again.",
#     "Don't count on it.",
#     "Outlook not so good.",
#     "It is decidedly so.",
#     "My sources say no.",
#     "Most likely.",
#     "Ask again later.",
#     "Cannot predict now.",
#     "Better not tell you now.",
#     "Concentrate and ask again.",
#     "Very doubtful.",
#     "Yes - definitely.",
#     "You may rely on it.",
#     "Prepare to be surprised!,",
# ]

# def ask_question():
#     question = input("Ask a question to the magic 8-ball: ")
#     if question == "":
#         return "\n\nYou didn't ask a question! Try again."

#     random_index = random.randint(0, len(responses))
#     answer = responses[random_index]

#     return f"\n\n{question.title()}, the magic 8-ball responds: '{answer}'."

# # Main loop
# while True:
#     print(ask_question())


def main():
    # Define the possible answers
    answers = ["Yes", "No", "\nBetter not tell you now.", "\nOutlook not so good.", "Yes, definitely.", "No way, Jose.",
               "Definitely not.", "Incredibly lucky,", "You may rely on it", "Hell yes, definitely.", "Hell no, definitely not!"]

    # Prompt the user to enter their question
    question = input("Enter your question: \n")

    # Randomly select an answer from the possible answers
    answer = random.choice(answers)

    # Display the answer to the user
    print("\nThe magic 8-ball says: {}".format(answer))

if __name__ == "__main__":
    main()
