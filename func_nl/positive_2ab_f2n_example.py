import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_positive_2ab_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##positive_2ab({a}, {b})",
                "outputStr": __random_explanation_positive_2ab(a, b, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_positive_2ab(a, b, identifier: int | None) -> str:
    explanations = [
        f"The outcome of evaluating positive_2ab({a}, {b})",
        f"Calculating the value of 2 * {a} * {b}",
        f"The result of evaluating 2 * {a} * {b}",
        f"Calculation: positive_2ab({a}, {b})",
        f"The expression 2 * {a} * {b}",
        f"The outcome of evaluating positive_2ab({a}, {b})",
        f"The result obtained by calculating 2 * {a} * {b}",
        f"The value of 2 times {a} times {b}",
        f"The computed result of evaluating 2 * {a} * {b}",
        f"The product of 2 times {a} times {b}",
        f"The outcome of determining 2 * {a} * {b}",
        f"The numerical value of 2 * {a} times {b}",
        f"The result of evaluating positive_2ab({a}, {b})",
        f"The value of 2 * {a} * {b} is",
        f"The result derived from evaluating positive_2ab({a}, {b})",
        f"The calculated result of 2 * {a} times {b}",
        f"The value of 2 times {a} times {b} is",
        f"The value of 2 * {a} * {b} equals",
        f"The value of 2 * {a} times {b} is",
        f"The computed value of 2 * {a} * {b}",
        f"The calculated outcome of 2 * {a} times {b}",
        f"The outcome of determining the product of 2 times {a} times {b}",
        f"The outcome of evaluating positive_2ab({a}, {b})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_positive_2ab_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
