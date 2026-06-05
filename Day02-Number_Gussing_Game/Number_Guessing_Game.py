import random

class NumberGuessingGame:

    def __init__(self):

        self.secret_number = 0
        self.attempts = 0

    
    def play(self, min_num, max_num, max_attempt):

        self.secret_number = random.randint(min_num,max_num)
        self.attempts = 0

        print(f"Guess a number between {min_num} and {max_num}")

        while True:

            try:

                num = int(input("Enter Number:"))
                self.attempts += 1

                
                if num < self.secret_number:
                     print("Too low! Try agian")
            
                elif num > self.secret_number:
                    print("Too high! Try agian")
            
                else:
                    print(f"You won the game in {self.attempts} attempts!")
                    break

                if max_attempt is not None and self.attempts >= max_attempt:
                    print(f"Game over! The number was {self.secret_number}.")
                    
                    break
                
            except ValueError:

                print("Pls Enter valid number" ) 
        
    def easy_game(self):
        self.play(1, 50, None)

    def medium_game(self):
        self.play(1, 100, 10)

    def hard_game(self):
        self.play(1, 500, 5)

            
def main():

    game = NumberGuessingGame()

    print("Welcome to Number Guessing Game")

    while True:

        GAME_LEVEL = """
        1. Easy
        2. Medium
        3. Hard
        4.Exit
        """
        
        print(GAME_LEVEL)

        num = input("Enter number:-")

        if num == '1':
            game.easy_game()
            
        
        elif num == '2':
            game.medium_game()

        elif num == '3':
            game.hard_game()
        
        elif num == '4':
            print("Goodbye!")
            break

        else:

            print("Invalid Choice!")
            continue

           

        again = input("Play again? (y/n): ").lower()   

        if again == "n":

            print("Thanks for playing ❤️")
            break

        

      
if __name__ == "__main__":
    main()