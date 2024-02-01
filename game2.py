import random
import time

topics = ["Countries", "Animals", "Movies"] # Possible topics
questions = {
    "Countries": {
        "question1": "What is the capital of France?",
        "answers": {"Paris": "correct", "Lyon": "wrong"}
    },
    "Animals": {
        "question2": "What is the fastest land animal?",
        "answers": {"Cheetah": "correct", "Tiger": "wrong", "Elephant": "wrong"}
    },
    "Movies": {
        "question3": "Who directed the movie 'The Dark Knight'?",
        "answers": {"Christopher Nolan": "correct", "George Lucas": "wrong", "Steven Spielberg": "wrong"}
    }
}

score = 0

def timer(sec):
    start = time.time()
    while (time.time() - start) < sec:
        print(f"Time remaining: {round(sec - (time.time() - start), 2)} seconds")
        time.sleep(0.2)
    print("Time's up!")

while True:
    try:
        # Ask the user for the topic of their choice
        topic_choice = input("Choose a topic (Countries, Animals, Movies): ")

        # Check if the input is valid
        while topic_choice not in topics:
            topic_choice = input("Invalid input. Choose a topic (Countries, Animals, Movies): ")

        question = questions[topic_choice]

        timer(5) # Set a timer for 5 seconds
        print(question["question1"])

        answer = question["answers"]

        # Convert dictionary to list of tuples (for use in the random.choice method)
        # The list will look like this: ['Paris', 'wrong], ...]
        answers_list = [(item, answer[item]) for item in answer.keys()]

        user_ans = input("Your answer: ")
        while user_ans not in [item for item, result in answers_list]:
            print("Invalid answer. Please enter one of the provided options.")
            user_ans = input("Your answer: ")

        # Check if the user's answer is correct
        correct = None
        for answer_tuple in answers_list:
            if answer_tuple[0] == user_ans:
                answer_correct = answer_tuple[1] == "correct"
                correct = answer_correct
                break

        if correct:
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
        print("\nBye-Bye!")
        break
    except Exception as error:
        print("\nError:", error)
        break
