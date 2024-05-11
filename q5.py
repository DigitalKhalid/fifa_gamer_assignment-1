def main():
    # Initialize lists to store positive, zero, and negative numbers
    positive_nums = []
    zeros = []
    negative_nums = []

    # Continuously prompt the user for input until they enter a blank line
    while True:
        user_input = input("Enter an integer (blank to quit): ")
        if user_input == "":
            break
        num = int(user_input)
        # Categorize the number into positive, zero, or negative list
        if num > 0:
            positive_nums.append(num)
        elif num == 0:
            zeros.append(num)
        else:
            negative_nums.append(num)

    # Print the entered numbers
    print("The numbers were:")
    # Combine all three lists into one
    all_nums = positive_nums + zeros + negative_nums
    
    # Convert all numbers in the list to strings
    str_nums = [str(num) for num in all_nums]

    # Join the strings together with a space between each number
    result = " ".join(str_nums)

    # Print the result
    print(result)


# Usage
if __name__ == "__main__":
    main()