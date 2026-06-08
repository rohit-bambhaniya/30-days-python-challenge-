import random

class RockPaperScissorsGame:

    def __init__(self):

        self.options = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    
    def get_user_choice(self):

        user_input = input(f"Enter Your Choice:-{','.join(self.options)}:-").strip().lower()

        return user_input
    
    def get_computer_choice(self):

        return random.choice(self.options)
    
    
    def is_valid_choice(self, choice):
        
        return choice in self.options


    def decide_winner(self, user, computer):

        if user == computer:

            return "Draw"
        
        winning_cases = {

            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        
        if winning_cases[user] == computer:

            return "user"
        
        else:

            return "computer"
        

    def update_score(self, winner):

            if winner == 'user':

                self.user_score += 1

                print("You win this round 🎉")

            elif winner == 'computer':

                self.computer_score += 1

                print("Computer win this round 💻")

            else:

                print("It's a draw")

    
    def play(self):

        print("\n Welcome to Rock Paper Scissors Game!")
        print("Type 'quit' anytime to exit.\n")

        while True:

            user = self.get_user_choice()

            if user == "quit":

                print("\nGame Over!")
                break

            if not self.is_valid_choice(user):

                print("Invalid choice! Try again.\n")
                continue

            computer = self.get_computer_choice()

            print(f"Computer chose: {computer}")

            winner = self.decide_winner(user, computer)

            self.update_score(winner)

            print(f"Score → You: {self.user_score} | Computer: {self.computer_score}\n")

        self.show_final_score()

    def show_final_score(self):
        print("\n FINAL RESULT")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")

        if self.user_score > self.computer_score:

            print(" You are the overall winner!")

        elif self.user_score < self.computer_score:

            print(" Computer wins overall!")

        else:
            
            print(" Overall match is a draw!")

    

if __name__=='__main__':

    game = RockPaperScissorsGame()
    game.play()

        
        
       
                

        
   


  


        

        