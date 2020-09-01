# Write a function is_even that will return true if the passed-in number is even.
# YOUR CODE HERE
def is_even(num):
    if int(num) % 2 == 0:
        print("This is an even number")
    else:
        print("This number is odd")
    return num

is_even(50)
is_even(51)
is_even(52)
is_even(53)
is_even(54)
is_even(55)
is_even(56)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

