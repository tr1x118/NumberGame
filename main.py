import random #importing functon for random number

def main(): 

    ran = random.randint(1, 100)
    #setting the varible for random number

    while True:

        guess = int(input("Guess the number from 1 to 100: \n"))
        #asking for user input

        if guess == ran:
            print("Congatulations!!!")
            break
        elif guess < ran:
            print("Too low,try again")
        else:
            print("Too big,try again")
    #loop that checking is user input correct

main() 
