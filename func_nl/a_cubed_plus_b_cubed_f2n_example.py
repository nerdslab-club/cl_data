import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_a_cubed_plus_b_cubed_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##a_cubed_plus_b_cubed({a}, {b})",
                "outputStr": __random_explanation_a_cubed_plus_b_cubed(a, b),
            }
        )
    return examples


def __random_explanation_a_cubed_plus_b_cubed(a, b) -> str:
    explanations = [
        f"Calculating the value of {a}^3 + {b}^3",
        f"a_cubed_plus_b_cubed({a}, {b})",
        f"The result of evaluating {a}^3 + {b}^3",
        f"Calculation: a_cubed_plus_b_cubed({a}, {b})",
        f"The expression {a}^3 + {b}^3",
        f"The outcome of evaluating a_cubed_plus_b_cubed({a}, {b})",
        f"The result obtained by calculating {a}^3 + {b}^3",
        f"The value of {a} cubed plus {b} cubed",
        f"The computed result of evaluating {a}^3 + {b}^3",
        f"The sum of {a} cubed and {b} cubed",
        f"The outcome of determining {a}^3 + {b}^3",
        f"The numerical value of {a} cubed plus {b} cubed",
        f"The result of evaluating a_cubed_plus_b_cubed({a}, {b})",
        f"The value of {a}^3 + {b}^3 is",
        f"The result derived from evaluating a_cubed_plus_b_cubed({a}, {b})",
        f"The calculated result of {a} cubed plus {b} cubed",
        f"The value of {a} cubed plus {b} cubed is",
        f"The value of {a}^3 plus {b}^3 equals",
        f"The value of {a}^3 plus {b}^3 is",
        f"The computed value of {a}^3 + {b}^3",
        f"The calculated outcome of {a} cubed plus {b} cubed",
        f"The outcome of evaluating a_cubed_plus_b_cubed({a}, {b})",
        f"The outcome of determining the sum of {a} cubed and {b} cubed",
        f"The outcome of evaluating a_cubed_plus_b_cubed({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_cubed_plus_b_cubed_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
