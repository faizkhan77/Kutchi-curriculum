quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C",
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "B",
    },
    {
        "question": "Which language is primarily used for Android app development?",
        "options": ["A. Java", "B. Python", "C. Swift", "D. Kotlin"],
        "answer": "A",
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Process Unit",
            "B. Central Processing Unit",
            "C. Computer Personal Unit",
            "D. Central Processor Unit",
        ],
        "answer": "B",
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": [
            "A. William Wordsworth",
            "B. William Shakespeare",
            "C. Charles Dickens",
            "D. George Orwell",
        ],
        "answer": "B",
    },
]

score = 0

for index, q in enumerate(quiz_data):
    print(f"Q{index+1}: {q['question']}")
    for option in q["options"]:
        print(option)

    # Get the user's answer
    user_answer = input("Your answer (A/B/C/D): ")

    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

# Display the final score
print(f"Your final score is: {score}/{len(quiz_data)}")
