import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_x_plus_a_times_x_plus_b_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_integer()
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append(
            {
                "inputStr": f"##x_plus_a_times_x_plus_b({x}, {a}, {b})",
                "outputStr": __random_explanation_x_plus_a_times_x_plus_b(x, a, b, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_x_plus_a_times_x_plus_b(n, a, b, identifier: int | None) -> str:
    explanations = [
        f"The outcome of evaluating x_plus_a_times_x_plus_b({n}, {a}, {b})",
        f"Calculating the value of ({n} + {a}) * ({n} + {b})",
        f"The result of evaluating ({n} + {a}) * ({n} + {b})",
        f"Calculation: x_plus_a_times_x_plus_b({n}, {a}, {b})",
        f"The expression ({n} + {a}) * ({n} + {b})",
        f"The outcome of evaluating x_plus_a_times_x_plus_b({n}, {a}, {b})",
        f"The result obtained by calculating ({n} + {a}) * ({n} + {b})",
        f"The value of ({n} + {a}) multiplied by ({n} + {b})",
        f"The computed result of evaluating ({n} + {a}) * ({n} + {b})",
        f"The product of ({n} + {a}) and ({n} + {b})",
        f"The outcome of determining ({n} + {a}) * ({n} + {b})",
        f"The numerical value of ({n} + {a}) times ({n} + {b})",
        f"The result of evaluating x_plus_a_times_x_plus_b({n}, {a}, {b})",
        f"The value of ({n} + {a}) * ({n} + {b}) is",
        f"The result derived from evaluating x_plus_a_times_x_plus_b({n}, {a}, {b})",
        f"The calculated result of ({n} + {a}) * ({n} + {b})",
        f"The value of ({n} + {a}) multiplied by ({n} + {b}) is",
        f"The value of ({n} + {a}) * ({n} + {b}) equals",
        f"The value of ({n} + {a}) times ({n} + {b}) is",
        f"The computed value of ({n} + {a}) * ({n} + {b})",
        f"The calculated outcome of ({n} + {a}) * ({n} + {b})",
        f"The outcome of determining the product of ({n} + {a}) and ({n} + {b})",
        f"The outcome of evaluating x_plus_a_times_x_plus_b({n}, {a}, {b})",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_x_plus_a_times_x_plus_b_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
