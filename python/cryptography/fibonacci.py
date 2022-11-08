def menu():
    choice = input("Choose a method of generating a sequence (1: if statements, 2: for loop, 0 to end program): ")
    if choice == "1":
        fibonacci()
    if choice == "2":
        fibonacci_forloop()
    if choice == "0":
        print("Goodbye")

def fibonacci(number):
    number = print(int(input("Choose a number, would you kindly: ")))
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number-2) + fibonacci(number-1)
    #print(fibonacci(number))

def fibonacci_forloop():
    num = print(int(input("Choose a number, would you kindly: ")))
    sequence = []
    if num == 1:
        sequence = [0]
    else:
        sequence = [0,1]
        for i in range(1, num-1):
            sequence.append(sequence[i-1] + sequence[i])
    return sequence
    #print(fibonacci_forloop)

menu()
