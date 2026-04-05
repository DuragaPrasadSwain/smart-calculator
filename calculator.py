# ===== SMART CALCULATOR =====

# Select operation:
# +  → Addition
# -  → Subtraction
# *  → Multiplication
# /  → Division
# ^  → Power
# %  → Modulus
# h  → Show History
# q  → Quit

# Enter choice: +
# Enter first number: 10
# Enter second number: 5
# Result: 15

# Do you want to continue? (yes/no): yes

def user_input():
    while True:
        choice = input("Enter choice:")
        if choice not in ['+','-','*','/','^','%','h','q']:
            print("\nEnter valid choice.\nTry again.\n")
            continue
        if choice == 'h':
            print("\n==== HISTORY =====\n")
            if len(History) == 0:
                print("No History Available\n")
            for i,his in enumerate(History,start=1):
                
                print(f"{i}.{his}\n")
        elif choice == 'q':
            return 'q'
        try:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            return choice,num1,num2
        except Exception as e:
            print(f"Error:{e}\n\nEnter numbers only.\nTry again.\n")

def calculation(choice,num1,num2):
    direction ={
        '+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '/':lambda a,b:a/b if b != 0 else "Cannot divide by zero",
        '^':lambda a,b:a**b,
        '%':lambda a,b:a%b,
    }
    
    return direction.get(choice)(num1,num2)

def calculator():

    user_inputs = user_input()
    if user_inputs == 'q':
        return 'q','q'
    result = calculation(user_inputs[0],user_inputs[1],user_inputs[2])
    print(f"Result: {result}")

    return user_inputs,result
        

print("===== SMART CALCULATOR =====")

print(" Select operation:\n+  → Addition\n-  → Subtraction\n*  → Multiplication\n/  → Division\n^  → Power\n%  → Modulus\nh  → Show History\nq  → Quit\n")
History = []
while True:
    inputs,result = calculator()
    if inputs == 'q':
        print("Exiting calculator... Goodbye!")
        break
    History.append(f"{inputs[1]} {inputs[0]} {inputs[2]} = {result}")