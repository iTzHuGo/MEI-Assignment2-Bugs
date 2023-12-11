def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) - fibonacci(n - 2) # Bug 1: incorrect recursive calls

def main():
    n = 10 

    print("Fibonacci Series:")
        # Bug 2: The loop should start from 1 instead of 0 for correct output

    for i in range(n):
        print(fibonacci(i)) # Bug 3: Incorrect print output

if __name__ == "__main__":
    main()
