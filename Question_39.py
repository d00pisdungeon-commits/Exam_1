def area_rectangle(length, width): #function header for calculating area
    return length * width #function for calculating area

def rectangle(): #function header for defining the rectangle
    try: #function that allows program to output specific message instead of crashing if improper entry made by user
        user_length = float(input('Enter the length of the rectangle: ')) #prompts user for length of rectangle and converts to float
        user_width = float(input('Enter the width of the rectangle: ')) #prompts user for width of rectangle and converts to float

        area = area_rectangle(user_length, user_width) #calls the first function and uses defined parameters
        print(f'\nThe area of the rectangle with length {user_length} and width {user_width} is {area}') #F-string displays results

    except ValueError: #refers to the try function, if the user enters a value that creates a ValueError then this
        print('\nINVALID ENTRY: Please enter a number') #output for a ValueError allowing the program to complete instead of error

rectangle()




