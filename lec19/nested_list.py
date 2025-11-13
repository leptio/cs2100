from typing import List, Any
def sum_list(inp: List[Any]) -> Any:
    if inp is None or not isinstance(inp, List):
        return 0
    elif len(inp) == 0:
        return 0
    else:
        print(inp)
        element = inp[0]
        if isinstance(element, List):
            sum_list_return = sum_list(element)
            sum_list_other_inputs = sum_list(inp[1:])

            print(sum_list_return, sum_list_other_inputs)

            return sum_list_return + sum_list_other_inputs
        else:
            sum_list_other_inputs = sum_list(inp[1:])

            print(element, sum_list_other_inputs)

            return element + sum_list_other_inputs

print(sum_list([1, 2, [3, 4], 5]))