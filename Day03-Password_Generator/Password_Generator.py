import random
import string

class PasswordGenerator:

    def __init__(self):
        
        pass

    def generate_password(self, pool):

        

        try:
         
            my_password = ""

            user = int(input("Enter your password length:- "))
           

            if user <= 0:
                    print("Password length must be greater than 0")
                    return
            

            for i in range(user):
                
                my_password += random.choice(pool)

            print(my_password)

        except ValueError:

            print("Please Enter valid number!")
         

    def simple_pass(self):

        

        pool = string.ascii_letters

        self.generate_password(pool)

       

    def hard_pass(self):
        
        pool = string.ascii_letters + string.digits

        self.generate_password(pool)

            
    def strong_pass(self):
         
        pool = string.ascii_letters + string.digits + string.punctuation

        self.generate_password(pool)

            
def main():

    password = PasswordGenerator()

    print("welcome to Password Generator")

    choice_pass = """
    1.simple_password
    2.hart_password
    3.strong_password
    """
    while True:

        print(choice_pass)

        choice = input("Enter your choice:-")

        if choice == '1':
            password.simple_pass()

        elif choice == '2':
            password.hard_pass()

        elif choice == '3':
            password.strong_pass()

        else:
            print("Invalid Choice!")
            continue

        
        again = input("Generate Password Again? (y/n): ").lower()

        if again == 'n':
             
            print("Thanks for Generate Password ❤️")
            break

        elif again == 'y':
            continue

        else:
            print("Please enter only y or n")
             


   
     
if __name__ == "__main__":
    main()






