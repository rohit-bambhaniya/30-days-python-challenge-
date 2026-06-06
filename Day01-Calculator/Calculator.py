class Calculator:

    def __init__(self, num1:float, num2:float):

        self.num1 = num1
        self.num2 = num2

    def add(self):

        return self.num1 + self.num2
    
    
    def subtract(self):

        return self.num1 - self.num2
    
    
    def multiply(self):

        return self.num1 * self.num2
    
    
    def divide(self):
        
        if self.num2 == 0:

            return "Cannot divide by zero"

        return self.num1 / self.num2
        
def main():

    while True:

        MENU = """
            1. Addition (+)
            2. Subtract (-)
            3. Multiply (*)
            4. Divide (/)
        """

        print(MENU)

        choice = input("Enter Your choice:-")

        if choice not in ['1', '2', '3', '4']:

            print("invalid choice! ")

            continue

        try:

            num1 = float(input("Enter Number1:- "))
            num2 = float(input("Enter Number2:- "))

            calc = Calculator(num1, num2)

            operations = {
                "1":calc.add,
                "2":calc.subtract,
                "3":calc.multiply,
                "4":calc.divide
            }

            print(f"Result: {operations[choice]()}")

            again = input("Do another calculation? (y/n):").lower()

            if again == 'n':

                break

            elif again == 'y':

                continue
            
            else:

                print("Please enter only y or n")



        except ValueError:
            print("Enter valid number")

    
        except Exception as e:
            print(f"unexpected error {e}")


if __name__ == "__main__":    
    
    main()
        
   
        





