# fun quiz
# -------------
# def start_game():
#     list_user_guess = []
#     score_correct_guess = 0
#     question_num = 1
#
#     for key in questions:
#         print(key)  # print out the questions
#         for i in options[1 - question_num]:  # value at i position in each list
#             print(i)
#         user_guess = input("choice: ").upper()  # make user input to upper case
#         list_user_guess.append(user_guess)
#         score_correct_guess += check_answer(questions.get(key), user_guess)       # get pair value in dictionary
#         question_num += 1              # move to next index of options in option
#
#     display_score(score_correct_guess, list_user_guess)
#
#
# # -------------
# def check_answer(correct_answer, user_guess):
#     if correct_answer == user_guess:
#         print("Correct!")
#         return 1
#     else:
#         print("Incorrect!")
#         return 0
#
#
# # -------------
# def display_score(correct_guess, list_user_guess):
#     print("\n---------------")
#     print("Result")
#     print("---------------")
#     print("Your answer: ", end=" ")  # list the answer to the right / no new line
#     for i in list_user_guess:
#         print(i, end=" ")
#     print("\nCorrect answer: ", end=" ")
#     for key in questions:
#         print(questions.get(key), end=" ")
#
#     score = int((correct_guess / len(questions)) * 100)
#     print(""
#           ""
#           "\nScore: " + str(score) + "%")
#
#
# # -------------
# def play_again():
#     response = input("\nWould you like to play again? (yes/no)").upper()
#     if response == "Yes":
#         return True
#     elif response == "NO":
#         return False
#     else:
#         print("[ Invalid response ]")
#         return False

def start_game():
    list_user_answer = []
    question_num = 1
    score_answer = 0
    for key in questions:
        print(key)
        for i in options[question_num - 1]:
            print(i)
        user_answer = input("choice: ").upper() # make user input in lower case
        score_answer += check_answer(questions.get(key), user_answer)
        list_user_answer.append(user_answer)
        question_num += 1

    display_score(score_answer, list_user_answer)


def check_answer(correct_answer, user_answer):
    if correct_answer == user_answer:
        print("[ Correct ]")
        return 1
    else:
        print("[ Incorrect ]")
        return 0


def display_score(score_answer, list_user_answer):
    print("\n=======")
    print("Result")
    print("=======")
    print("Your answer: ", end=" ")      # end=" " means you display on one line / no new line
    for i in list_user_answer:
        print(i, end=" ")
    print("\nCorrect answer:", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")

    score = int((score_answer / len(questions)) * 100)

    print("\nScore: " + str(score) + "%")


def play_again():
    response = input("\nWould you like to play again: (yes/no) ").upper()
    if response == "YES":
        return True
    elif response == "NO":
        return False
    else:
        print("\nInvalid input")


questions = {"\n1. How many colors are there in rainbow? ": "A",
             "\n2. What does a thermometer measure? ": "C",
             "\n3. What fruits do raisins come from? ": "B",
             "\n4. A portrait is a picture of what? ": "C",
             "\n5. How many cents are in a quarter? ": "A"
             }

options = [["A. 7", "B. 6", "C. 5"],
           ["A. Width", "B. Length", "C. Temperature"],
           ["A. Apple", "B. Grapes", "C. Pineapples"],
           ["A. A nation", "B. An island", "C. A person"],
           ["A. 25 cents", "B. 20 cents", "C. 15 cents"]
           ]


start_game()
#
while play_again():
    start_game()

print("\n== Good Game ==")
