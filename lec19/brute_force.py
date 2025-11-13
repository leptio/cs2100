def unlock(passcode: str) -> None:
    """Unlocks the vault if the passcode is correct"""
    if passcode == '9299934':
        print("Unlocked!") 

def try_all(num_digits: int, passcode_so_far: str = '') -> None:
    if len(passcode_so_far) == num_digits:
        unlock(passcode_so_far)
    else:
        for digit in range(10):
            try_all(num_digits, f'{passcode_so_far}{digit}')

try_all(7)