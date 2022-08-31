# nested loop
# the "inner loop" will finish all of it's iterations before
# finishing one iteration of the "outer loop"

rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("Enter a symbol to use: ")

# outer loop
for i in range(rows):
    # inner loop
    for j in range(columns):
        print(symbol, end="") # prevent cursor moving down to the next line
    print()