import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_int_to_float_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##int_to_float({value})",
                "outputStr": __random_explanation_int_to_float(value, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_int_to_float(n: int, identifier: int | None) -> str:
    explanations = [
        f"The floating-point representation of the integer {n}",
        f"The result of converting the integer value {n} to a floating-point value",
        f"Calculation: int_to_float({n})",
        f"The decimal representation of the integer {n}",
        f"The outcome of converting the integer {n} to a floating-point number",
        f"The floating-point number that corresponds to the integer {n}",
        f"The result of converting the integer value {n} to a float",
        f"The computed result of converting the integer {n} to a floating-point value",
        f"The floating-point equivalent of the integer {n}",
        f"The outcome of evaluating int_to_float({n})",
        f"The floating-point number obtained by representing the integer {n}",
        f"The result of evaluating int_to_float({n})",
        f"The decimal value that corresponds to the integer {n}",
        f"The computed floating-point representation of the integer {n}",
        f"The floating-point value obtained by converting the integer {n}",
        f"The calculated result of converting the integer {n} to a float",
        f"The floating-point value for the given integer {n} is",
        f"The result derived from converting the integer {n} to a floating-point value",
        f"The computed floating-point equivalent of the integer {n}",
        f"The floating-point value obtained by representing the integer {n}",
        f"The floating-point value that corresponds to the integer {n}",
        f"The calculated outcome of evaluating int_to_float({n})",
        f"The decimal number that represents the integer {n}",
        f"The calculated floating-point representation of the integer {n}",
        f"The calculated floating-point value obtained by converting the integer {n}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_int_to_float_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
