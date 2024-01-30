import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_floor_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##floor({x})",
                "outputStr": __random_explanation_floor(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_floor(x: float, identifier: int | None) -> str:
    explanations = [
        f"The largest integer less than or equal to {x}",
        f"The greatest whole number that is not greater than {x}",
        f"Calculation: floor({x})",
        f"The integer immediately below {x}",
        f"The largest integer that is equal to or smaller than {x}",
        f"The largest integer that is not larger than {x}",
        f"The largest integer less than {x}",
        f"The largest integer smaller than or equal to {x}",
        f"The largest integer that is not greater than {x} is",
        f"The next lower integer before {x}",
        f"The largest integer equal to or smaller than {x}",
        f"The largest integer smaller than {x} is",
        f"The largest integer less than or equal to the input value {x}",
        f"The integer just below {x}",
        f"The greatest whole number less than or equal to {x}",
        f"The largest integer not greater than {x}",
        f"The largest integer smaller than or equal to the value {x}",
        f"The previous integer less than or equal to {x}",
        f"The integer that is equal to or smaller than {x}",
        f"The largest integer that is not larger than {x} is",
        f"The largest integer immediately below {x}",
        f"The largest integer less than {x} is",
        f"The largest integer that is less than or equal to {x}",
        f"The largest integer that is at most {x}",
        f"The floor value of {x} is",
        f"The result of calculating floor({x}) is",
        f"The previous integer below {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_floor_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
