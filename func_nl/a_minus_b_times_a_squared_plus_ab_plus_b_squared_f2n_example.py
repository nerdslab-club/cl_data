import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
                "outputStr": __random_explanation_a_minus_b_times_a_squared_plus_ab_plus_b_squared(a, b),
            }
        )
    return examples


def __random_explanation_a_minus_b_times_a_squared_plus_ab_plus_b_squared(a, b) -> str:
    explanations = [
        f"Calculating the value of ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The result of evaluating ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"Calculation: a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The expression ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"The outcome of evaluating a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The result obtained by calculating ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"The value of ({a} - {b}) times ({a}^2 + {a} * {b} + {b}^2)",
        f"The computed result of evaluating ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"The product of ({a} - {b}) and ({a}^2 + {a} * {b} + {b}^2)",
        f"The outcome of determining ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"The numerical value of ({a} - {b}) times ({a}^2 + {a} * {b} + {b}^2)",
        f"The result of evaluating a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The value of ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2) is",
        f"The result derived from evaluating a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The calculated result of ({a} - {b}) times ({a}^2 + {a} * {b} + {b}^2)",
        f"The value of ({a} - {b}) times ({a}^2 + {a} * {b} + {b}^2) is",
        f"The value of ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2) equals",
        f"The value of ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2) is",
        f"The computed value of ({a} - {b}) * ({a}^2 + {a} * {b} + {b}^2)",
        f"The calculated outcome of ({a} - {b}) times ({a}^2 + {a} * {b} + {b}^2)",
        f"The outcome of evaluating a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
        f"The outcome of determining the product of ({a} - {b}) and ({a}^2 + {a} * {b} + {b}^2)",
        f"The outcome of evaluating a_minus_b_times_a_squared_plus_ab_plus_b_squared({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
