import random
import sys
from time import sleep

# Possible topics
topics = ["countries", "animals", "movies"]

# Questions and answers for each topic
questions = {
    "countries": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "animals": {
        "question": "What is the fastest land animal?",
        "answer": "Cheetah"
    },
    "movies": {
        "question": "Who directed the movie 'The Dark Knight'?",
        "answer": "Christopher Nolan"
    }
}

# Initialize score and timer
score = 0
timer = 10  # 10 seconds per question

while True:
    try:
        # Ask the user for the topic of their choice
        topic_choice = input("Choose a topic (countries, animals, movies): ")

        # Check if the input is valid
        while topic_choice not in topics:
            topic_choice = input("Invalid input. Choose a topic (countries, animals, movies): ")

        question = questions[topic_choice]
        answer = questions[topic_choice][question]["answer"]

        # Display the question and start the timer
        print(question)
        start = time.time()
        while time.time() - start < timer:
            print(f"Time remaining: {timer - (time.time() - start)} sec")
            sleep(1)

        user_ans = input("\nEnter your answer: ")

        # Check if the user's answer is correct
        if user_ans.lower() == answer.lower():
            print("Congratulations! You are right.")
            score += 1
        else:
            print("Sorry, that's not correct. Try again.")

        print(f"Your current score is: {score}")

        # Ask the user if they want to continue playing
        again = input("Do you want to continue playing? (y/n): ")

        # If the user doesn't want to continue, break the loop
        if again.lower() == 'n':
            break

    except KeyboardInterrupt:
        print("\nQuitting...")
        sys.exit()
    except Exception as e:
        print("\nError:", e)
        print("Please try again.")
