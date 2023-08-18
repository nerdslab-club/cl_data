import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_hypotenuse_example(count: int):
    examples = []
    for _ in range(count):
        a = random.uniform(1.0, 100.0)
        b = random.uniform(1.0, 100.0)
        examples.append(
            {
                "inputStr": f"##hypotenuse({a}, {b})",
                "outputStr": __random_explanation_hypotenuse(a, b),
            }
        )
    return examples


def __random_explanation_hypotenuse(a: float, b: float) -> str:
    explanations = [
        f"The length of the hypotenuse in a right triangle with perpendicular sides of lengths {a} and {b}",
        f"hypotenuse({a}, {b})",
        f"The result of calculating the length of the hypotenuse for a right triangle with sides {a} and {b}",
        f"Calculation: hypotenuse({a}, {b})",
        f"The length of the diagonal side in a right triangle with sides {a} and {b}",
        f"The outcome of finding the hypotenuse length for a right triangle with sides {a} and {b}",
        f"The length of the longest side in a right triangle with legs {a} and {b}",
        f"The result of determining the hypotenuse length for a right triangle with legs {a} and {b}",
        f"The computed result of calculating the hypotenuse length for a right triangle with sides {a} and {b}",
        f"The length of the slanted side in a right triangle with legs {a} and {b}",
        f"The outcome of evaluating hypotenuse({a}, {b})",
        f"The value obtained by finding the length of the hypotenuse for a right triangle with legs {a} and {b}",
        f"The result of evaluating hypotenuse({a}, {b})",
        f"The length of the inclined side in a right triangle with legs {a} and {b}",
        f"The computed length of the hypotenuse for a right triangle with sides {a} and {b}",
        f"The length of the diagonal side obtained from a right triangle with legs {a} and {b}",
        f"The calculated result of determining the hypotenuse length for a right triangle with sides {a} and {b}",
        f"The length of the slanted side derived from a right triangle with sides {a} and {b}",
        f"The result obtained from calculating the hypotenuse length for a right triangle with legs {a} and {b}",
        f"The computed hypotenuse length for a right triangle with sides {a} and {b}",
        f"The length of the inclined side calculated from a right triangle with legs {a} and {b}",
        f"The calculated outcome of evaluating hypotenuse({a}, {b})",
        f"The length of the diagonal side of a right triangle with sides {a} and {b}",
        f"The computed hypotenuse value for a right triangle with legs {a} and {b}",
        f"The calculated length of the hypotenuse for a right triangle with sides {a} and {b}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_hypotenuse_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
