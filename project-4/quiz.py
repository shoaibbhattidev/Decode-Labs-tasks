import random
import time


# This function simply prints a nice header for the quiz
def show_header():
    print("=" * 50)
    print("       🎯 GENERAL KNOWLEDGE QUIZ 🎯")
    print("=" * 50)


# This function returns all quiz questions
# We are using a list of dictionaries to keep things structured and easy to manage
def get_questions():
    return [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean in the world?",
            "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            "answer": "D"
        },
        {
            "question": "Who invented the telephone?",
            "options": ["A. Newton", "B. Einstein", "C. Edison", "D. Alexander Graham Bell"],
            "answer": "D"
        },
        {
            "question": "How many continents are there?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "C"
        },
        {
            "question": "Which gas do plants absorb?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        },
        {
            "question": "Which is the largest animal?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Shark", "D. Giraffe"],
            "answer": "B"
        },
        {
            "question": "Which country is famous for the Eiffel Tower?",
            "options": ["A. Italy", "B. France", "C. UK", "D. Germany"],
            "answer": "B"
        },
        {
            "question": "What is the currency of the USA?",
            "options": ["A. Euro", "B. Pound", "C. Dollar", "D. Yen"],
            "answer": "C"
        },
        {
            "question": "Which is the fastest land animal?",
            "options": ["A. Lion", "B. Tiger", "C. Cheetah", "D. Horse"],
            "answer": "C"
        }
    ]


# This function handles asking a single question
# It also checks the answer and returns 1 (correct) or 0 (wrong)
def ask_question(q, number):
    print(f"\nQ{number}. {q['question']}")

    # Display all options
    for option in q["options"]:
        print(option)

    # Start timer to track how long user takes
    start_time = time.time()

    # Take input and convert to uppercase for consistency
    answer = input("Your answer (A/B/C/D): ").upper()

    # Input validation loop (keeps asking until valid input is given)
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C or D.")
        answer = input("Your answer: ").upper()

    # End timer
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Check if answer is correct
    if answer == q["answer"]:
        print(f"✅ Correct! (Time: {time_taken}s)")
        return 1  # Return 1 for correct answer
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")
        return 0  # Return 0 for wrong answer


# This function shows the final result after quiz ends
def show_result(score, total):
    percentage = (score / total) * 100

    print("\n" + "=" * 50)
    print("📊 QUIZ RESULT")
    print("=" * 50)

    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    # Performance feedback based on score
    if percentage >= 90:
        print("🏆 Excellent!")
    elif percentage >= 70:
        print("👍 Very Good!")
    elif percentage >= 50:
        print("🙂 Good!")
    else:
        print("📚 Keep Practicing!")


# This function controls the quiz flow
def start_quiz():
    questions = get_questions()

    # Shuffle questions so each run feels different
    random.shuffle(questions)

    score = 0  # Initialize score

    # Loop through all questions
    for i, q in enumerate(questions, start=1):
        score += ask_question(q, i)

    # Show final result
    show_result(score, len(questions))


# Main function (entry point of program)
def main():
    while True:
        show_header()

        # Ask user name (just for personalization)
        name = input("Enter your name: ")
        print(f"\nWelcome {name}! Let's start the quiz 🚀")

        # Start quiz
        start_quiz()

        # Ask if user wants to play again
        again = input("\nDo you want to play again? (y/n): ").lower()

        if again != 'y':
            print("Thanks for playing! 👋")
            break  # Exit loop and end program


# This ensures the program only runs when file is executed directly
if __name__ == "__main__":
    main()

