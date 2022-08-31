# logical operation: and/or/not
# used to check if two or more conditional statements is true/false

temperature = int(input("what is the temperature outside?: "))

if temperature >= 0 and temperature <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temperature < 0 or temperature > 30:
    print("the temperature is bad today!")
    print("stay inside!")

if not(temperature >= 0 and temperature <= 30):
    print("the temperature is good today!")
    print("go outside!")
elif not(temperature < 0 or temperature > 30):
    print("the temperature is bad today!")
    print("stay inside!")