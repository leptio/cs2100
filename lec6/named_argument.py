"""Defines a function to display text"""
##default argument values
def display_text(text: str, size:int = 18, 
                 is_bold:bool = False, 
                 is_italic:bool = False, 
                 is_underlined:bool = False) -> None:
    """Displays text"""
    print(text, size, is_bold, is_italic, is_underlined)

##named arguments
display_text(text='hello',
             is_underlined=False,
             is_bold=False,
             is_italic=False,
             size=18)

display_text("Hello again!")
