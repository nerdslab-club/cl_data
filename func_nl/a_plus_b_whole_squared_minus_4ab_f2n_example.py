import random

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_f2n_a_plus_b_whole_squared_minus_4ab_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##a_plus_b_whole_squared_minus_4ab({a}, {b})",
                "outputStr": __random_explanation_a_plus_b_whole_squared_minus_4ab(a, b),
            }
        )
    return examples


def __random_explanation_a_plus_b_whole_squared_minus_4ab(a, b) -> str:
    explanations = [
        f"Calculating the value of ({a} + {b})^2 - 4*{a}*{b}",
        f"a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The result of evaluating ({a} + {b})^2 - 4*{a}*{b}",
        f"Calculation: a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The expression ({a} + {b})^2 - 4*{a}*{b}",
        f"The outcome of evaluating a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The result obtained by calculating ({a} + {b})^2 - 4*{a}*{b}",
        f"The value of ({a} + {b}) squared minus 4 times {a} times {b}",
        f"The computed result of evaluating ({a} + {b})^2 - 4*{a}*{b}",
        f"The sum of ({a} + {b}) squared and -4 times {a} times {b}",
        f"The outcome of determining ({a} + {b})^2 - 4*{a}*{b}",
        f"The numerical value of ({a} + {b}) squared minus 4 times {a} times {b}",
        f"The result of evaluating a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The value of ({a} + {b})^2 - 4*{a}*{b} is",
        f"The result derived from evaluating a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The calculated result of ({a} + {b}) squared minus 4 times {a} times {b}",
        f"The calculated sum of ({a} + {b}) squared and -4 times {a} times {b}",
        f"The value of ({a} + {b})^2 - 4*{a}*{b} equals",
        f"The value of ({a} + {b})^2 minus 4 times {a} times {b} is",
        f"The value of ({a} + {b}) squared minus 4 times {a} times {b} is",
        f"The computed value of ({a} + {b})^2 - 4*{a}*{b}",
        f"The calculated outcome of ({a} + {b}) squared minus 4 times {a} times {b}",
        f"The outcome of evaluating a_plus_b_whole_squared_minus_4ab({a}, {b})",
        f"The outcome of determining the sum of ({a} + {b}) squared and -4 times {a} times {b}",
        f"The outcome of evaluating a_plus_b_whole_squared_minus_4ab({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_plus_b_whole_squared_minus_4ab_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
