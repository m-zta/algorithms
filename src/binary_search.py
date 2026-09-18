import random as rnd

# TODO:
# Find out why the following example fails:
# List: [16, 35, 46, 48, 49, 51, 55, 56, 58, 59]
# Key: 37
# -> Results in invalid bounds error 


def get_key():
    key = 0
    while True:
        key = input("Enter a key to search: ")
        if key.isdigit():
            key = int(key)
            break
        else:
            print("Invalid input! Try again.")

    return key


def get_mode():
    mode = ""
    while True:
        mode = input(
            "Enter a mode (r: completely random, mr = manually random, m: manual) or 'q' to quit: ").lower()

        # check mode validity
        if mode == "q":
            print(
                "You're quitting? You're a quitter! You're a loser and nobody likes you!")
            quit()
        if mode != "r" and mode != "mr" and mode != "m":
            print("Invalid mode! Try again you son of a biatch!")
        else:
            break

    return mode


def get_random_list(size=10, min=0, max=100):
    result = []

    # check whether parameters are valid
    if size < 0 or max < min:
        print("invalid parameters! get_random_list(size, min, max)")
        return result

    for _ in range(size):
        result.append(rnd.randint(min, max))

    return result


def binary_search_iterative(mylist, key, first=None, last=None):
    """Perform an iterative binary search. Return index of the element in the array if found."""

    # Set default values for first and last
    if first is None:
        first = 0
    if last is None:
        last = len(mylist) - 1

    while first <= last:
        m = (first + last) / 2
        if mylist[m] == key:
            return m
        elif mylist[m] < key:
            first = m + 1
        else:
            last = m - 1

    return


def binary_search(mylist, key, first=None, last=None):
    """Perform a recursive binary search. Return index of the element in the array if found."""

    # Set default values for first and last
    if first is None:
        first = 0
    if last is None:
        last = len(mylist) - 1

    # Check if first and last are within valid bounds
    if not (0 <= first <= last < len(mylist)):
        raise ValueError("Invalid bounds!")

    # Base case: only one element in mylist
    if first == last:
        if mylist[first] == key:
            return first
        else:
            return -1

    # Recursive case: Divide and Conquer
    m = (first + last) // 2  # Use // for integer division
    mid = mylist[m]
    if mid == key:
        return m
    elif key < mid:
        return binary_search(mylist, key, first, m - 1)
    elif mid < key:
        return binary_search(mylist, key, m + 1, last)

    # If we've checked everything and haven't found the key, return -1
    return -1


def print_result(mylist, key):
    """Print the result of the binary search."""
    result = binary_search(mylist, key)
    if result > -1:
        print(f"Binary result: Element {key} is at index {result}")
    else:
        print(f"Binary result: Element {key} not found")


def random_mode():
    print("\nRANDOM MODE:")

    # generate bounds
    size = rnd.randint(1, 10)
    min = rnd.randint(-100, 99)
    max = rnd.randint(min, 100)

    # create list and key
    mylist = sorted(get_random_list(size, min, max))
    key = rnd.randint(min, max)

    # print current status
    print("Random list: ", mylist)
    print(f"Random key: {key}\n")

    # print result
    print_result(mylist, key)


def manual_random_mode():
    print("\nMANUALLY RANDOM MODE:")

    # get input
    size = int(input("Enter a list size: "))
    min = int(input("Enter a minimum value: "))
    max = int(input("Enter a maximum value: "))

    # create list
    mylist = sorted(get_random_list(size, min, max))
    key = rnd.randint(min, max)

    # print current status
    print("Random list: ", mylist)
    print(f"Random key: {key}\n")

    # print result
    print_result(mylist, key)


def build_list():
    result = []

    # get list
    print("Enter elements for the list ('-' when finished):")
    while True:
        print(result)
        element = input("New element: ")
        if element.isdigit() or (element[0] == "-" and element[1:].isdigit()):
            element = int(element)
            result.append(element)
            result = sorted(result)
        elif element == "-":
            break
        else:
            print("Invalid input! Try again.")

    return result


def wanna_continue():
    while True:
        decision = input("Continue? (y/n): ").lower()
        if decision == "y":
            return True
        elif decision == "n":
            return False
        else:
            print("Invalid input! Try again.")


def manual_mode():
    print("\nMANUAL MODE:")

    mylist = build_list()
    if len(mylist) == 0:
        print("Empty list! Exiting...")
        quit()

    # get keys and check
    while True:
        print("\nList: ", mylist)
        key = get_key()

        # print result
        print_result(mylist, key)

        # check whether to continue
        if not wanna_continue():
            break


def main():
    mode = get_mode()

    if mode == "r":
        random_mode()
    elif mode == "mr":
        manual_random_mode()
    elif mode == "m":
        manual_mode()


if __name__ == "__main__":
    main()
