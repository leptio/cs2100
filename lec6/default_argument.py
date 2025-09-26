"""Prints a number with a default value of 5."""
number_save: int = 5

def print_number(number:int=number_save) -> None:
    """Prints a number with a default value of 5."""
    print(number)

number_save: int = 6      #Does nothing, defualt stuck at 5

print_number(8) #8
print_number()  #5
print(number_save)   #6
