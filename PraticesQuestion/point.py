from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

try:
    color = Color(input("Enter your choice of 'red', 'blue' or 'green': ").strip().lower())
    
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
except ValueError:
    print("Invalid color choice. Please enter 'red', 'blue', or 'green'.")