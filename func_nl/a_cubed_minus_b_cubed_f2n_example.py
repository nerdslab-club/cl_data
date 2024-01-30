import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_a_cubed_minus_b_cubed_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##a_cubed_minus_b_cubed({a}, {b})",
                "outputStr": __random_explanation_a_cubed_minus_b_cubed(a, b, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_a_cubed_minus_b_cubed(a, b, identifier: int | None) -> str:
    explanations = [
        f"Calculating the value of {a}^3 - {b}^3",
        f"a_cubed_minus_b_cubed({a}, {b})",
        f"The result of evaluating {a}^3 - {b}^3",
        f"Calculation: a_cubed_minus_b_cubed({a}, {b})",
        f"The expression {a}^3 - {b}^3",
        f"The outcome of evaluating a_cubed_minus_b_cubed({a}, {b})",
        f"The result obtained by calculating {a}^3 - {b}^3",
        f"The value of {a} cubed minus {b} cubed",
        f"The computed result of evaluating {a}^3 - {b}^3",
        f"The difference between {a} cubed and {b} cubed",
        f"The outcome of determining {a}^3 - {b}^3",
        f"The numerical value of {a} cubed minus {b} cubed",
        f"The result of evaluating a_cubed_minus_b_cubed({a}, {b})",
        f"The value of {a}^3 - {b}^3 is",
        f"The result derived from evaluating a_cubed_minus_b_cubed({a}, {b})",
        f"The calculated result of {a} cubed minus {b} cubed",
        f"The value of {a} cubed minus {b} cubed is",
        f"The value of {a}^3 minus {b}^3 equals",
        f"The value of {a}^3 minus {b}^3 is",
        f"The computed value of {a}^3 - {b}^3",
        f"The calculated outcome of {a} cubed minus {b} cubed",
        f"The outcome of evaluating a_cubed_minus_b_cubed({a}, {b})",
        f"The outcome of determining the difference between {a} cubed and {b} cubed",
        f"The outcome of evaluating a_cubed_minus_b_cubed({a}, {b})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_cubed_minus_b_cubed_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
