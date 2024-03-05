import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_negative_2ab_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##negative_2ab({a}, {b})",
                "outputStr": __random_explanation_negative_2ab(a, b, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_negative_2ab(x, y, identifier: int | None) -> str:
    explanations = [
        f"The outcome of evaluating negative_2ab({x}, {y})",
        f"Calculating the value of -2 * {x} * {y}",
        f"The result of evaluating -2 * {x} * {y}",
        f"Calculation: negative_2ab({x}, {y})",
        f"The expression -2 * {x} * {y}",
        f"The outcome of evaluating negative_2ab({x}, {y})",
        f"The result obtained by calculating -2 * {x} * {y}",
        f"The value of negative 2 times {x} times {y}",
        f"The computed result of evaluating -2 * {x} * {y}",
        f"The product of -2 times {x} times {y}",
        f"The outcome of determining -2 * {x} * {y}",
        f"The numerical value of -2 * {x} times {y}",
        f"The result of evaluating negative_2ab({x}, {y})",
        f"The value of -2 * {x} * {y} is",
        f"The result derived from evaluating negative_2ab({x}, {y})",
        f"The calculated result of -2 * {x} times {y}",
        f"The value of negative 2 times {x} times {y} is",
        f"The value of -2 * {x} * {y} equals",
        f"The value of -2 * {x} times {y} is",
        f"The computed value of -2 * {x} * {y}",
        f"The calculated outcome of -2 * {x} times {y}",
        f"The outcome of determining the product of -2 times {x} times {y}",
        f"The outcome of evaluating negative_2ab({x}, {y})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_negative_2ab_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
