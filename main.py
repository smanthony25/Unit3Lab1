# Sean A
# While vs Recursion
# Make a while loop to do the same thing that the recursion does

def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num - 1)
    print(f"Returning; num = {num}")
    return


def while_substitute(num):
    max = num
    while num > 0:
        print(f"Looping; num = {num}")
        num -= 1
    print("\nBASE CASE REACHED\n")
    while num < max:
        num += 1
        print(f"Looping; num = {num}")


def main():
    sample(5)
    print("\n\n")
    while_substitute(5)


if __name__ == "__main__":
    main()
