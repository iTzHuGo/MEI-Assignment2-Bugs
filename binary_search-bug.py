def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        # Bug 1: Missing else keyword
        # Bug 2: Missing update for high when arr[mid] is greater than target
        # else:
        #     high = mid - 1

    # Bug 3: Incorrect return statement
    return 1

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    size = len(numbers)

    index = binary_search(numbers, target, 0, size - 1)

    if index != -1:
        print(f"Index of {target}: {index}")
    else:
        print(f"{target} not found in the array.")

if __name__ == "__main__":
    main()
