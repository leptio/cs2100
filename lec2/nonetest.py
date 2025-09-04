from typing import Optional
def get_number_or_None(hopefully_a_number: str) -> Optional[int]:
    try:
        return(int(hopefully_a_number))
    except ValueError:
        return None
    
print(get_number_or_None("4"))
print(get_number_or_None("n"))