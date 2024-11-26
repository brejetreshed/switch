def menu():
    print("\nPlease enter the number of the operation you choose:")
    print("1. Palindrome: Check if the input is palindrome")
    print("2. Lower: Check if all characters in the input are lowercase")
    print("3. Digit: Check if all characters in the input are digits")
    print("4. Long: Check if the input length is longer than 15")
    print("5. Empty: Check if the input is empty")
    print("6. Exit: Exit successfully from the application")

def is_palindrome(s):
    if len(s)<=1:
        return True
    elif (s[0]==s[-1]):
        return is_palindrome(s[1:-1])
    else: 
        return False
    
def is_lowercase(s):
    return s.islower()

def is_digit(s):
    return s.isdigit()

def is_length_exceed(s, threshold=15):
    return len(s) > threshold

def is_empty(s):
    return s == ""

def main():
    while True:
        menu()
        try:
            choice = int(input("Please enter the number of the operation you choose: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice not in range(1, 7):
                print("Invalid choice. Please select a valid option from 1 to 6.")
                continue

        if choice == 6:
            print("Exit successfully")
            break

        user_input = input("Enter an input: ")

        if choice == 1:
            result = "is a palindrome" if is_palindrome(user_input) else "is not a palindrome"
        elif choice == 2:
            result = "is all lowercase" if is_lowercase(user_input) else "is not all lowercase"
        elif choice == 3:
            result = "contains only digits" if is_digit(user_input) else "does not contain only digits"
        elif choice == 4:
            result = "long" if is_length_exceed(user_input) else "is not long, does not exceed length threshold"
        elif choice == 5:
            result = "is empty" if is_empty(user_input) else "is not empty"
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        print(f"The input '{user_input}' {result}.")

if __name__ == "__main__":
    main()