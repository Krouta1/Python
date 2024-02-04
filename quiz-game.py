#-------------#
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("----------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#-------------#
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
#-------------#
def display_score(correct_guesses, guesses):
    print("----------------")
    print("Results")
    print("----------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
#-------------#
def play_again():
    response = input("Do you want to play again? (yes or no): ").lower()
    if response == "yes":
        return True
    else:
        return False
#-------------#
questions = {
    "What is the capital of France?": "A",
    "What is 2+2?": "B",
    "What is 10*10?": "C",
    "What is 100/10?": "A",
}
options = [ ["A. Paris", "B. London", "C. New York","D. Moscow"],[ "A. 2", "B. 4", "C. 3", "D. 5"], ["A. 100", "B. 1000", "C. 10000", "D. 100000"], ["A. 10", "B. 20", "C. 30", "D. 40"]] 

new_game()
while play_again():
    new_game()
print("Thanks for playing")