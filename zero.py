Age = int(input(f'Age: '))
day = input("Day type (weekday/weekend): ")

if Age < 5:
    price = 0
elif 5 <= Age <=12:
    if day == "weekday":
        price = 1500
    else:
        price = 2000
elif 13 <= Age <=59:
    if day == "weekday":
        price = 2500
    else:
        price = 3500
elif Age >= 60:
    if day == "weekday":
        price = 1200
    else:
        price = 1800

print(f"Price: {price}")    

#
# Prompts must be exactly: "Age: " and "Day type (weekday/weekend): "
# Final output must be exactly: "Price: {price}"