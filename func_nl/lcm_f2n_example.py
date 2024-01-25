import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_lcm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        examples.append(
            {
                "inputStr": f"##lcm({x}, {y})",
                "outputStr": __random_explanation_lcm(x, y, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_lcm(x: int, y: int, identifier: int | None) -> str:
    explanations = [
        f"The least common multiple of {x} and {y}",
        f"lcm({x}, {y})",
        f"The smallest multiple that is divisible by both {x} and {y}",
        f"Calculation: lcm({x}, {y})",
        f"The lowest common multiple of {x} and {y}",
        f"The smallest positive integer divisible by both {x} and {y}",
        f"The least common multiple for the numbers {x} and {y}",
        f"The result of calculating the least common multiple for {x} and {y}",
        f"The smallest multiple of {x} and {y}",
        f"The common multiple of {x} and {y} with the smallest value",
        f"The smallest positive integer that is a multiple of both {x} and {y}",
        f"The least common multiple of the integers {x} and {y}",
        f"The minimum multiple that is divisible by both {x} and {y}",
        f"The least multiple that divides both {x} and {y}",
        f"The smallest number that can be divided evenly by both {x} and {y}",
        f"The common multiple of {x} and {y} with the least value",
        f"The least shared multiple of {x} and {y}",
        f"The smallest number that can evenly divide both {x} and {y}",
        f"The smallest value that is a multiple of both {x} and {y}",
        f"The common factor of {x} and {y} with the smallest value",
        f"The least common multiple for {x} and {y} is",
        f"The result of calculating lcm({x}, {y}) is",
        f"The minimum common multiple of {x} and {y} is",
        f"The least common multiple for the integers {x} and {y} is",
        f"The smallest multiple that is divisible by both {x} and {y} is",
        f"The least shared multiple of {x} and {y} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_lcm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
