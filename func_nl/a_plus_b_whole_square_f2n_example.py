import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility
from cl_data.src.random_value_generator import RandomValueGenerator


def create_f2n_a_plus_b_whole_square_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##a_plus_b_whole_square({a}, {b})",
                "outputStr": __random_explanation_a_plus_b_whole_square(a, b, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_a_plus_b_whole_square(a, b, identifier: int | None) -> str:
    explanations = [
        f"Calculating the square of the sum of {a} and {b}",
        f"a_plus_b_whole_square({a}, {b})",
        f"The result of squaring the sum of {a} and {b}",
        f"Calculation: a_plus_b_whole_square({a}, {b})",
        f"The square of the sum of {a} and {b}",
        f"The outcome of evaluating a_plus_b_whole_square({a}, {b})",
        f"The result obtained by squaring the sum of {a} and {b}",
        f"The square value of {a} plus {b}",
        f"The computed result of calculating the square of the sum of {a} and {b}",
        f"The square of the sum of the numbers {a} and {b}",
        f"The outcome of determining the square of the sum of {a} and {b}",
        f"The numerical value of squaring {a} plus {b}",
        f"The result of evaluating a_plus_b_whole_square({a}, {b})",
        f"The square of the sum of {a} and {b} equals",
        f"The result derived from evaluating a_plus_b_whole_square({a}, {b})",
        f"The squared value of {a} plus {b} is",
        f"The value of squaring {a} plus {b} is",
        f"The computed square of the sum of {a} and {b}",
        f"The calculated result of calculating the square of the sum of {a} and {b}",
        f"The square value of {a} added to {b}",
        f"The computed value of squaring the sum of {a} and {b}",
        f"The outcome of evaluating a_plus_b_whole_square({a}, {b})",
        f"The outcome of determining the squared value of {a} plus {b}",
        f"The outcome of evaluating a_plus_b_whole_square({a}, {b})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_plus_b_whole_square_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
