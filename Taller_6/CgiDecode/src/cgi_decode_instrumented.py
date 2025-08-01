from src.evaluate_condition import evaluate_condition

def cgi_decode_instrumented(s):
    # Mapping of hex digits to their integer values
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
#  evaluate_condition(condition_num: int, op: str, lhs: Union[str, Dict], rhs: Union[str, Dict]) -> bool:
    t = ""
    i = 0
    while evaluate_condition(1, "Gt", len(s), i):  # c1
        c = s[i]
        if evaluate_condition(2, "Eq", c, '+'):  # c2
            t += ' '
        elif evaluate_condition(3, "Eq", c, '%'):  # c3
            digit_high, digit_low = s[i + 1], s[i + 2]
            i += 2
            if evaluate_condition(4, "In", digit_high, hex_values):  # c4
                if evaluate_condition(5, "In", digit_low, hex_values):  # c5
                    v = hex_values[digit_high] * 16 + hex_values[digit_low]
                    t += chr(v)
                else:
                    raise ValueError("Invalid encoding: digit low is not a hex digit")
            else:
                raise ValueError("Invalid encoding: digit high is not a hex digit")
        else:
            t += c
        i += 1
    return t

