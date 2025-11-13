def power(base: int, exp:int) -> int:
    """Returns the base raised to the power of the exponent"""
    if exp==0:
        return 1
    else:
        returned=power(base,exp-1)
        print(base, exp, returned, base*returned)
        return base*returned

print(power(2,9))
#base^exp=base*base^(exp-1)