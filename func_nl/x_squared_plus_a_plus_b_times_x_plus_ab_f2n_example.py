import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_x_squared_plus_a_plus_b_times_x_plus_ab_example(count: int):
    examples = []
    for _ in range(count):
        x = RandomValueGenerator.generate_random_integer(-10, 1000)
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        result = x**2 + (a + b) * (x + a * b)
        examples.append(
            {
                "inputStr": f"##x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
                "outputStr": __random_explanation_x_squared_plus_a_plus_b_times_x_plus_ab(
                    x, a, b
                ),
            }
        )
    return examples


def __random_explanation_x_squared_plus_a_plus_b_times_x_plus_ab(x, a, b) -> str:
    explanations = [
        f"Calculating the value of {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The result of evaluating {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"Calculation: x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The outcome of evaluating x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The result obtained by calculating {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The value of {x} squared plus the product of ({a} + {b}) and ({x} + {a} * {b})",
        f"The computed result of evaluating {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The sum of {x} squared and the product of ({a} + {b}) and ({x} + {a} * {b})",
        f"The outcome of determining {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The numerical value of {x} squared plus the product of ({a} + {b}) and ({x} + {a} * {b})",
        f"The result of evaluating x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The value of {x}^2 + ({a} + {b}) * ({x} + {a} * {b}) is",
        f"The result derived from evaluating x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The calculated result of {x} squared plus the product of ({a} + {b}) and ({x} + {a} * {b})",
        f"The value of {x} squared plus the product of ({a} + {b}) and ({x} + {a} * {b}) is",
        f"The value of {x}^2 plus the product of ({a} + {b}) and ({x} + {a} * {b}) equals",
        f"The value of {x}^2 plus the product of ({a} + {b}) and ({x} + {a} * {b}) is",
        f"The computed value of {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The calculated outcome of {x}^2 + ({a} + {b}) * ({x} + {a} * {b})",
        f"The outcome of evaluating x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        f"The outcome of determining the sum of {x} squared and the product of ({a} + {b}) and ({x} + {a} * {b})",
        f"The outcome of evaluating x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_x_squared_plus_a_plus_b_times_x_plus_ab_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
