numbers = [1, 2, 3, 4, 5]

# Bug 1: Filter even numbers with an incorrect condition
even_numbers = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even_numbers)

# Bug 2: Square each number with an incorrect exponent
squared_numbers = [x**3 for x in numbers]
print("Squared numbers:", squared_numbers)

# Bug 3: Calculate the sum with a wrong variable
total = sum(even_numbers)  # Change to sum(numbers) for correct behavior
print("Sum:", total)

