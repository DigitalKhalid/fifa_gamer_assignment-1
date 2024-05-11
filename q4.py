import random


def generate_random_list():
    # Create an empty list to store random numbers
    random_list = []

    # Loop 10 times to generate 10 random numbers
    for i in range(10):
        # Generate a random number between 1 and 50
        random_number = random.randint(1, 50)
        # Add the random number to the list
        random_list.append(random_number)

    # Return the list of random numbers
    return random_list


def substitute(lst):
    # Iterate through each element of the list
    for i in range(len(lst)):
        # Check if the element is a multiple of 5
        if lst[i] % 5 == 0:
            # If it is, replace the element with its square
            lst[i] = lst[i] ** 2


def main():
    # Generate a random list
    original_list = generate_random_list()

    # Display the original list
    print("Before substitution, the list is:", original_list)

    # Apply substitution to the original list
    substitute(original_list)

    # Display the modified list
    print("After substitution, the list is:", original_list)


# Usage
if __name__ == "__main__":
    main()