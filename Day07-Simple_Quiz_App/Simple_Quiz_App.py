simple_quiz = {
    "q1": {
        "question": "1. In which year was Python released?",
        "options": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"],
        "answer": "B"
    },
    "q2": {
        "question": "2. Which symbol is used for single-line comments in Python?",
        "options": ["A) //", "B) /*", "C) #", "D) <!--"],
        "answer": "C"
    },
    "q3": {
        "question": "3. What was the main focus while designing Python?",
        "options": ["A) Speed", "B) Code Readability", "C) Complex Syntax", "D) Memory Management"],
        "answer": "B"
    }
}

medium_quiz = {
    "q1": {
        "question": "1. Which function is used to find the length of a list in Python?",
        "options": ["A) length()", "B) len()", "C) count()", "D) size()"],
        "answer": "B"
    },
    "q2": {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) function", "C) def", "D) define"],
        "answer": "C"
    },
    "q3": {
        "question": "3. Which function is used to convert a string into an integer in Python?",
        "options": ["A) str()", "B) int()", "C) float()", "D) cast()"],
        "answer": "B"
    },
    "q4": {
        "question": "4. Which method is used to add an element at the end of a list?",
        "options": ["A) add()", "B) insert()", "C) append()", "D) push()"],
        "answer": "C"
    },
    "q5": {
        "question": "5. Which of the following is NOT a valid variable name?",
        "options": ["A) my_var", "B) _myvar", "C) 2myvar", "D) myVar"],
        "answer": "C"
    },
    "q6": {
        "question": "6. Which statement is used to stop a loop immediately?",
        "options": ["A) stop", "B) exit", "C) break", "D) skip"],
        "answer": "C"
    }
}

hard_quiz = {
    "q1": {
        "question": "1. What type of programming language is Python?",
        "options": ["A) Interpreted", "B) Compiled", "C) Assembly", "D) None of these"],
        "answer": "A"
    },
    "q2": {
        "question": "2. Which of the following is a mutable data type?",
        "options": ["A) List", "B) Tuple", "C) String", "D) Int"],
        "answer": "A"
    },
    "q3": {
        "question": "3. Which data type does NOT allow duplicate values?",
        "options": ["A) List", "B) Tuple", "C) Set", "D) Dictionary Keys"],
        "answer": "C"
    },
    "q4": {
        "question": "4. Which keyword is used to create an anonymous function in Python?",
        "options": ["A) anonymous", "B) inline", "C) lambda", "D) undef"],
        "answer": "C"
    },
    "q5": {
        "question": "5. How are blocks of code defined in Python?",
        "options": ["A) Curly Braces {}", "B) Parentheses ()", "C) Indentation (Spaces)", "D) Semicolon ;"],
        "answer": "C"
    },
    "q6": {
        "question": "6. What is the '**' operator used for in Python?",
        "options": ["A) Multiplication", "B) Exponentiation (Power)", "C) Division", "D) Modulus"],
        "answer": "B"
    },
    "q7": {
        "question": "7. Which keyword is NOT used in exception handling?",
        "options": ["A) try", "B) except", "C) finally", "D) catch"],
        "answer": "D"
    },
    "q8": {
        "question": "8. Which method is used to get all keys from a dictionary?",
        "options": ["A) get_keys()", "B) keys()", "C) all_keys()", "D) show_keys()"],
        "answer": "B"
    },
    "q9": {
        "question": "9. Which of the following is a Python web development framework?",
        "options": ["A) Django", "B) React", "C) Laravel", "D) Angular"],
        "answer": "A"
    },
    "q10": {
        "question": "10. Which block can execute if a loop completes without a break statement?",
        "options": ["A) else", "B) finally", "C) except", "D) then"],
        "answer": "A"
    }
}


class Quiz:

    def __init__(self):
        self.selected_quiz = {}
        self.score = 0

    def load_simple_quiz(self):
        self.selected_quiz = simple_quiz

    def load_medium_quiz(self):
        self.selected_quiz = medium_quiz

    def load_hard_quiz(self):
        self.selected_quiz = hard_quiz

    def start_quiz(self):

        if not self.selected_quiz:
            print("No quiz selected.")
            return

        self.score = 0
        total_questions = len(self.selected_quiz)

        print("\n" + "=" * 40)
        print("Quiz Started")
        print("=" * 40)

        for question_data in self.selected_quiz.values():

            try:
                print("\n" + question_data["question"])

                for option in question_data["options"]:
                    print(option)

                answer = input("\nEnter Answer (A/B/C/D): ").strip().upper()

                if answer not in ["A", "B", "C", "D"]:
                    print("Invalid Answer! Enter only A, B, C or D")
                    continue

                if answer == question_data["answer"]:
                    print("Correct")
                    self.score += 1

                else:
                    for option in question_data["options"]:
                        if option.startswith(question_data["answer"]):
                            print(f"Wrong! Correct Answer: {option}")
                            break

            except KeyError:
                print("Quiz Data Error!")

            except Exception as e:
                print("Error:", e)

        print("\n" + "=" * 40)
        print("Quiz Finished")
        print("=" * 40)

        print(f"Score: {self.score}/{total_questions}")

        percentage = (self.score / total_questions) * 100

        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 80:
            print("Excellent!")
        elif percentage >= 50:
            print("Good Job!")
        else:
            print("Keep Practicing!")

    
def main():

    app = Quiz()

    while True:

        try:

            print("""
1. Simple Quiz
2. Medium Quiz
3. Hard Quiz
4. Exit
""")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                app.load_simple_quiz()
                app.start_quiz()

            elif choice == "2":
                app.load_medium_quiz()
                app.start_quiz()

            elif choice == "3":
                app.load_hard_quiz()
                app.start_quiz()

            elif choice == "4":
                print("Thank You for Playing!")
                break

            else:
                print("Invalid Choice! Please enter 1, 2, 3 or 4")

        except KeyboardInterrupt:
            print("\nProgram Interrupted")
            break

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()