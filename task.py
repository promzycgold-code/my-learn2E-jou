raw_input = "forty-two"

try:
    number = int(raw_input)
    print(f"Parsed: {number}")
except ValueError:
    number = 0
    print("Could not parse input. Defaulting to 0.")

print(f"The number is {number}")

