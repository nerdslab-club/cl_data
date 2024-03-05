import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_a_squared_minus_2ab_plus_b_squared_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##a_squared_minus_2ab_plus_b_squared({a}, {b})",
                "outputStr": __random_explanation_a_squared_minus_2ab_plus_b_squared(
                    a, b, (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_a_squared_minus_2ab_plus_b_squared(a, b, identifier: int | None) -> str:
    explanations = [
        f"The outcome of evaluating a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"Calculating the value of {a}^2 - 2*{a}*{b} + {b}^2",
        f"a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"The result of evaluating {a}^2 - 2*{a}*{b} + {b}^2",
        f"Calculation: a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"The expression {a}^2 - 2*{a}*{b} + {b}^2",
        f"The result obtained by calculating {a}^2 - 2*{a}*{b} + {b}^2",
        f"The value of {a} squared minus 2 times {a} times {b} plus {b} squared",
        f"The computed result of evaluating {a}^2 - 2*{a}*{b} + {b}^2",
        f"The sum of {a} squared, -2 times {a} times {b}, and {b} squared",
        f"The outcome of determining {a}^2 - 2*{a}*{b} + {b}^2",
        f"The numerical value of {a} squared minus 2 times {a} times {b} plus {b} squared",
        f"The result of evaluating a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"The value of {a}^2 - 2*{a}*{b} + {b}^2 is",
        f"The result derived from evaluating a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"The calculated result of {a} squared minus 2 times {a} times {b} plus {b} squared",
        f"The calculated sum of {a} squared, -2 times {a} times {b}, and {b} squared",
        f"The value of {a}^2 - 2*{a}*{b} + {b}^2 equals",
        f"The value of {a}^2 minus 2 times {a} times {b} plus {b}^2 is",
        f"The value of {a} squared minus 2 times {a} times {b} plus {b} squared is",
        f"The computed value of {a}^2 - 2*{a}*{b} + {b}^2",
        f"The calculated outcome of {a} squared minus 2 times {a} times {b} plus {b} squared",
        f"The outcome of evaluating a_squared_minus_2ab_plus_b_squared({a}, {b})",
        f"The outcome of determining the sum of {a} squared, -2 times {a} times {b}, and {b} squared",
        f"The outcome of evaluating a_squared_minus_2ab_plus_b_squared({a}, {b})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_squared_minus_2ab_plus_b_squared_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
