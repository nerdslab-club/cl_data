import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_gcd_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        y = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##gcd({x}, {y})",
                "outputStr": __random_explanation_gcd(x, y, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_gcd(x: int, y: int, identifier: int | None) -> str:
    explanations = [
        f"The greatest common divisor of {x} and {y}",
        f"The largest number that divides both {x} and {y}",
        f"The highest common factor of {x} and {y}",
        f"The greatest common factor of {x} and {y}",
        f"The greatest common divisor for the numbers {x} and {y}",
        f"The result of calculating the greatest common divisor for {x} and {y}",
        f"The greatest number that divides {x} and {y}",
        f"The common divisor of {x} and {y} with the highest value",
        f"The largest divisor shared by {x} and {y}",
        f"The greatest common divisor of the integers {x} and {y}",
        f"The maximum factor that divides both {x} and {y}",
        f"The greatest divisor that divides both {x} and {y}",
        f"The greatest number that can divide both {x} and {y}",
        f"The highest value divisor that divides {x} and {y}",
        f"The largest number that can evenly divide both {x} and {y}",
        f"The common factor of {x} and {y} with the highest value",
        f"The greatest shared divisor of {x} and {y}",
        f"The highest factor that divides both {x} and {y}",
        f"The largest common factor for the numbers {x} and {y}",
        f"The highest number that divides both {x} and {y} evenly",
        f"The greatest common divisor for {x} and {y} is",
        f"The result of calculating gcd({x}, {y}) is",
        f"The maximum common divisor of {x} and {y} is",
        f"The greatest common divisor for the integers {x} and {y} is",
        f"The largest factor that divides both {x} and {y} evenly",
        f"The highest shared divisor of {x} and {y} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_gcd_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
