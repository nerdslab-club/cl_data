import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_float_to_int_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##float_to_int({value})",
                "outputStr": __random_explanation_float_to_int(value, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_float_to_int(value: float, identifier: int | None) -> str:
    explanations = [
        f"The integer part of the float {value}",
        f"The result of converting the floating-point value {value} to an integer",
        f"Calculation: float_to_int({value})",
        f"The whole number portion of the float {value}",
        f"The outcome of truncating the decimal part of the floating-point number {value}",
        f"The integer that represents the floor value of the float {value}",
        f"The result of rounding down the floating-point number {value} to an integer",
        f"The computed result of converting the float {value} to an integer",
        f"The integer obtained by discarding the decimal part of the float {value}",
        f"The outcome of evaluating float_to_int({value})",
        f"The integer value obtained by truncating the decimal part of the float {value}",
        f"The result of evaluating float_to_int({value})",
        f"The integer that represents the largest integer less than or equal to the float {value}",
        f"The computed integer value of the float {value}",
        f"The integer obtained by removing the decimal part of the floating-point value {value}",
        f"The calculated result of converting the float {value} to an integer",
        f"The integer part of the number {value} is",
        f"The result derived from truncating the decimal part of the float {value}",
        f"The computed integer part of the floating-point number {value}",
        f"The integer obtained by rounding down the float {value}",
        f"The integer obtained from truncating the decimal part of the float {value}",
        f"The calculated outcome of evaluating float_to_int({value})",
        f"The integer value that corresponds to the floor value of the float {value}",
        f"The calculated integer part of the floating-point number {value}",
        f"The calculated integer obtained by truncating the decimal part of the float {value}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_float_to_int_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
