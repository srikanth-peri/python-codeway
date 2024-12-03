def add(a, b):
    return a + b

def sub(x, y):
    return x - y

def mul(a, b):
    return a * b

def div(x, y):
    if y == 0:
        return "Division by zero not possible"
    else:
        return x / y

while True:
        print("1 Addition \n2 Subtraction \n3 Multiplication \n4 Division \n5 Exit")
        
        choice = input("Enter your choice: ")
        
        if choice in ('1', '2', '3', '4'):
            n1 = float(input("Enter 1 st number: "))
            n2 = float(input("Enter 2 nd number: "))
            
            if choice == '1':
                print("Sum :", add(n1, n2))
            elif choice == '2':
                print("Subtrat :", sub(n1, n2))
            elif choice == '3':
                print("Multiplication :", mul(n1, n2))
            elif choice == '4':
                print("Division :", div(n1, n2))
        elif choice == '5':
            print("Exiting")
            break
        else:
             print("Invalid choice ")