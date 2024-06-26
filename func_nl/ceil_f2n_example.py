import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_ceil_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-100.0, 100.0)
        examples.append(
            {
                "inputStr": f"##ceil({x})",
                "outputStr": __random_explanation_ceil(x),
            }
        )
    return examples


def __random_explanation_ceil(x: float) -> str:
    explanations = [
        f"The smallest integer greater than or equal to {x}",
        f"ceil({x})",
        f"The smallest whole number that is not less than {x}",
        f"Calculation: ceil({x})",
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
        f"The integer just above {x}",
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
        f"The ceil value of {x} is",
        f"The result of calculating ceil({x}) is",
        f"The next integer above {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_ceil_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
