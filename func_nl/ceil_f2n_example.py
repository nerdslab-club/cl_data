import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_ceil_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##ceil({x})",
                "outputStr": __random_explanation_ceil(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_ceil(x: float, identifier: int | None) -> str:
    explanations = [
        f"The integer just above {x}",
        f"The ceil value of {x} is",
        f"The smallest integer greater than or equal to {x}",
        f"The smallest whole number that is not less than {x}",
        f"The integer immediately above {x}",
        f"The smallest integer that is equal to or larger than {x}",
        f"The smallest integer that is not smaller than {x}",
        f"The smallest integer greater than {x}",
        f"The smallest integer larger than or equal to {x}",
        f"The smallest integer that is not less than {x} is",
        f"The next higher integer after {x}",
        f"The smallest integer equal to or greater than {x}",
        f"The smallest integer larger than {x} is",
        f"The smallest integer greater than or equal to the input value {x}",
        f"The smallest whole number greater than or equal to {x}",
        f"The smallest integer not less than {x}",
        f"The smallest integer larger than or equal to the value {x}",
        f"The next integer greater than or equal to {x}",
        f"The integer that is equal to or larger than {x}",
        f"The smallest integer that is not smaller than {x} is",
        f"The smallest integer immediately above {x}",
        f"The smallest integer greater than {x} is",
        f"The smallest integer that is greater than or equal to {x}",
        f"The smallest integer that is at least {x}",
        f"The result of calculating ceil({x}) is",
        f"The next integer above {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_ceil_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
