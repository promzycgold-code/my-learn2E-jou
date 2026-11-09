'''def tithe_calculator(tithe):
    try:
        income = tithe
        payable= income / 100
        fina = payable * 10
        print(fina)
    except ZeroDivisionError:
        return ( "can't pay tithe for zero income ")

tithe_calculator()'''




def tithe_calculator(tithe):
    try:
        income = float(tithe)  # Convert the input string to a decimal number
        if income == 0:
            print("Can't pay tithe for zero income.")
            return
            
        payable = income / 100
        fina = payable * 10
        print(f"Your tithe is: {fina}")
    except ValueError:
        print("Please enter a valid numeric amount.")

# 1. Ask the user for their income amount
user_income = input("Enter your income: ")

# 2. Call the function and pass the user's input into it
tithe_calculator(user_income)
