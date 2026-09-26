def calculate_rectangle_area(length, width):
    """
    Generalized custom function to calculate the area of a rectangle.
    Takes 2 parameters: length and width.
    """
    return length * width


def main():
    # Prompt the user for input and convert the strings to floating-point numbers
        user_length = float(input("Enter the length of the rectangle: "))
        user_width = float(input("Enter the width of the rectangle: "))

        # Call the custom function with the 2 parameters
        area = calculate_rectangle_area(user_length, user_width)

        # Display the area using an F-String
        print(f"\nThe area of the rectangle with length {user_length} and width {user_width} is: {area:.2f}")



if __name__ == "__main__":
    main()
