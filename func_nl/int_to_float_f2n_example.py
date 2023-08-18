import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_int_to_float_example(count: int):
    examples = []
    for _ in range(count):
        value = random.randint(-100, 100)
        examples.append(
            {
                "inputStr": f"##int_to_float({value})",
                "outputStr": __random_explanation_int_to_float(value),
            }
        )
    return examples


def __random_explanation_int_to_float(value: int) -> str:
    explanations = [
        f"The floating-point representation of the integer {value}",
        f"int_to_float({value})",
        f"The result of converting the integer value {value} to a floating-point value",
        f"Calculation: int_to_float({value})",
        f"The decimal representation of the integer {value}",
        f"The outcome of converting the integer {value} to a floating-point number",
        f"The floating-point number that corresponds to the integer {value}",
        f"The result of converting the integer value {value} to a float",
        f"The computed result of converting the integer {value} to a floating-point value",
        f"The floating-point equivalent of the integer {value}",
        f"The outcome of evaluating int_to_float({value})",
        f"The floating-point number obtained by representing the integer {value}",
        f"The result of evaluating int_to_float({value})",
        f"The decimal value that corresponds to the integer {value}",
        f"The computed floating-point representation of the integer {value}",
        f"The floating-point value obtained by converting the integer {value}",
        f"The calculated result of converting the integer {value} to a float",
        f"The floating-point value for the given integer {value} is",
        f"The result derived from converting the integer {value} to a floating-point value",
        f"The computed floating-point equivalent of the integer {value}",
        f"The floating-point value obtained by representing the integer {value}",
        f"The floating-point value that corresponds to the integer {value}",
        f"The calculated outcome of evaluating int_to_float({value})",
        f"The decimal number that represents the integer {value}",
        f"The calculated floating-point representation of the integer {value}",
        f"The calculated floating-point value obtained by converting the integer {value}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_int_to_float_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
