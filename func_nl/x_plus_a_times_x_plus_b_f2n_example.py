import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_x_plus_a_times_x_plus_b_example(count: int):
    examples = []
    for _ in range(count):
        x = RandomValueGenerator.generate_random_integer(-10, 1000)
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##x_plus_a_times_x_plus_b({x}, {a}, {b})",
                "outputStr": __random_explanation_x_plus_a_times_x_plus_b(x, a, b),
            }
        )
    return examples


def __random_explanation_x_plus_a_times_x_plus_b(x, a, b) -> str:
    explanations = [
        f"Calculating the value of ({x} + {a}) * ({x} + {b})",
        f"x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The result of evaluating ({x} + {a}) * ({x} + {b})",
        f"Calculation: x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The expression ({x} + {a}) * ({x} + {b})",
        f"The outcome of evaluating x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The result obtained by calculating ({x} + {a}) * ({x} + {b})",
        f"The value of ({x} + {a}) multiplied by ({x} + {b})",
        f"The computed result of evaluating ({x} + {a}) * ({x} + {b})",
        f"The product of ({x} + {a}) and ({x} + {b})",
        f"The outcome of determining ({x} + {a}) * ({x} + {b})",
        f"The numerical value of ({x} + {a}) times ({x} + {b})",
        f"The result of evaluating x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The value of ({x} + {a}) * ({x} + {b}) is",
        f"The result derived from evaluating x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The calculated result of ({x} + {a}) * ({x} + {b})",
        f"The value of ({x} + {a}) multiplied by ({x} + {b}) is",
        f"The value of ({x} + {a}) * ({x} + {b}) equals",
        f"The value of ({x} + {a}) times ({x} + {b}) is",
        f"The computed value of ({x} + {a}) * ({x} + {b})",
        f"The calculated outcome of ({x} + {a}) * ({x} + {b})",
        f"The outcome of evaluating x_plus_a_times_x_plus_b({x}, {a}, {b})",
        f"The outcome of determining the product of ({x} + {a}) and ({x} + {b})",
        f"The outcome of evaluating x_plus_a_times_x_plus_b({x}, {a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_x_plus_a_times_x_plus_b_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
