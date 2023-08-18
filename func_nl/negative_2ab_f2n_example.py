import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_negative_2ab_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        result = -2 * a * b
        examples.append(
            {
                "inputStr": f"##negative_2ab({a}, {b})",
                "outputStr": __random_explanation_negative_2ab(a, b),
            }
        )
    return examples


def __random_explanation_negative_2ab(a, b) -> str:
    explanations = [
        f"Calculating the value of -2 * {a} * {b}",
        f"negative_2ab({a}, {b})",
        f"The result of evaluating -2 * {a} * {b}",
        f"Calculation: negative_2ab({a}, {b})",
        f"The expression -2 * {a} * {b}",
        f"The outcome of evaluating negative_2ab({a}, {b})",
        f"The result obtained by calculating -2 * {a} * {b}",
        f"The value of negative 2 times {a} times {b}",
        f"The computed result of evaluating -2 * {a} * {b}",
        f"The product of -2 times {a} times {b}",
        f"The outcome of determining -2 * {a} * {b}",
        f"The numerical value of -2 * {a} times {b}",
        f"The result of evaluating negative_2ab({a}, {b})",
        f"The value of -2 * {a} * {b} is",
        f"The result derived from evaluating negative_2ab({a}, {b})",
        f"The calculated result of -2 * {a} times {b}",
        f"The value of negative 2 times {a} times {b} is",
        f"The value of -2 * {a} * {b} equals",
        f"The value of -2 * {a} times {b} is",
        f"The computed value of -2 * {a} * {b}",
        f"The calculated outcome of -2 * {a} times {b}",
        f"The outcome of evaluating negative_2ab({a}, {b})",
        f"The outcome of determining the product of -2 times {a} times {b}",
        f"The outcome of evaluating negative_2ab({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_negative_2ab_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
