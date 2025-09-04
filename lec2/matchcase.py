name: str = input ("Please enter your name: ")
match name:
    case 'SpongeBob':
        print("You are SpongeBob")
    case 'patrick':
        print("You are Patrick")
    case _:
        print("I don't know you")