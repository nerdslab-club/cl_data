import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_a_plus_b_whole_squared_minus_4ab_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##a_plus_b_whole_squared_minus_4ab({a}, {b})",
                "outputStr": __random_explanation_a_plus_b_whole_squared_minus_4ab(
                    a, b, (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_a_plus_b_whole_squared_minus_4ab(a, b, identifier: int | None) -> str:
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_plus_b_whole_squared_minus_4ab_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
