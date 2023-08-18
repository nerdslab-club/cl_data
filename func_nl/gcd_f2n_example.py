import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_gcd_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        examples.append(
            {
                "inputStr": f"##gcd({x}, {y})",
                "outputStr": __random_explanation_gcd(x, y),
            }
        )
    return examples


def __random_explanation_gcd(x: int, y: int) -> str:
    explanations = [
        f"The greatest common divisor of {x} and {y}",
        f"gcd({x}, {y})",
        f"The largest number that divides both {x} and {y}",
        f"Calculation: gcd({x}, {y})",
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
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_gcd_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
