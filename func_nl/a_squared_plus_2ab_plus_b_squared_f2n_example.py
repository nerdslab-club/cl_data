import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_a_squared_plus_2ab_plus_b_squared_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##a_squared_plus_2ab_plus_b_squared({a}, {b})",
                "outputStr": __random_explanation_a_squared_plus_2ab_plus_b_squared(
                    a, b
                ),
            }
        )
    return examples


def __random_explanation_a_squared_plus_2ab_plus_b_squared(a, b) -> str:
    explanations = [
        f"Calculating the value of {a}^2 + 2*{a}*{b} + {b}^2",
        f"a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The result of evaluating {a}^2 + 2*{a}*{b} + {b}^2",
        f"Calculation: a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The expression {a}^2 + 2*{a}*{b} + {b}^2",
        f"The outcome of evaluating a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The result obtained by calculating {a}^2 + 2*{a}*{b} + {b}^2",
        f"The value of {a} squared plus 2 times {a} times {b} plus {b} squared",
        f"The computed result of evaluating {a}^2 + 2*{a}*{b} + {b}^2",
        f"The sum of {a} squared, 2 times {a} times {b}, and {b} squared",
        f"The outcome of determining {a}^2 + 2*{a}*{b} + {b}^2",
        f"The numerical value of {a} squared plus 2 times {a} times {b} plus {b} squared",
        f"The result of evaluating a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The value of {a}^2 + 2*{a}*{b} + {b}^2 is",
        f"The result derived from evaluating a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The calculated result of {a} squared plus 2 times {a} times {b} plus {b} squared",
        f"The calculated sum of {a} squared, 2 times {a} times {b}, and {b} squared",
        f"The value of {a}^2 + 2*{a}*{b} + {b}^2 equals",
        f"The value of {a}^2 plus 2 times {a} times {b} plus {b}^2 is",
        f"The value of {a} squared plus 2 times {a} times {b} plus {b} squared is",
        f"The computed value of {a}^2 + 2*{a}*{b} + {b}^2",
        f"The calculated outcome of {a} squared plus 2 times {a} times {b} plus {b} squared",
        f"The outcome of evaluating a_squared_plus_2ab_plus_b_squared({a}, {b})",
        f"The outcome of calculating the sum of {a} squared, 2 times {a} times {b}, and {b} squared",
        f"The outcome of evaluating a_squared_plus_2ab_plus_b_squared({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_squared_plus_2ab_plus_b_squared_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
