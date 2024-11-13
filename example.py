# example.py

def dangerous_function(user_input):
    # Avoid using eval in production code
    user_command = eval(user_input)  # This is dangerous!
    return user_command

def main():
    user_input = input("Enter your command: ")
    result = dangerous_function(user_input)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
