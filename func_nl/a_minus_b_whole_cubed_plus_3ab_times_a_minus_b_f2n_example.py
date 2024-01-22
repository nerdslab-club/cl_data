import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(-10, 1000)
        b = RandomValueGenerator.generate_random_integer(-10, 1000)
        examples.append(
            {
                "inputStr": f"##a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
                "outputStr": __random_explanation_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b(
                    a, b
                ),
            }
        )
    return examples


def __random_explanation_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b(a, b) -> str:
    explanations = [
        f"Calculating the value of ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The result of evaluating ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"Calculation: a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The expression ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"The outcome of evaluating a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The result obtained by calculating ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"The value of ({a} - {b}) cubed plus 3 times {a} times {b} times ({a} - {b})",
        f"The computed result of evaluating ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"The sum of ({a} - {b}) cubed and 3 times {a} times {b} times ({a} - {b})",
        f"The outcome of determining ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"The numerical value of ({a} - {b}) cubed plus 3 times {a} times {b} times ({a} - {b})",
        f"The result of evaluating a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The value of ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b}) is",
        f"The result derived from evaluating a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The calculated result of ({a} - {b}) cubed plus 3 times {a} times {b} times ({a} - {b})",
        f"The value of ({a} - {b}) cubed plus 3 times {a} times {b} times ({a} - {b}) is",
        f"The value of ({a} - {b})^3 plus 3 times {a} times {b} times ({a} - {b}) equals",
        f"The value of ({a} - {b})^3 plus 3 times {a} times {b} times ({a} - {b}) is",
        f"The computed value of ({a} - {b})^3 + 3 * {a} * {b} * ({a} - {b})",
        f"The calculated outcome of ({a} - {b}) cubed plus 3 times {a} times {b} times ({a} - {b})",
        f"The outcome of evaluating a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
        f"The outcome of determining the sum of ({a} - {b}) cubed and 3 times {a} times {b} times ({a} - {b})",
        f"The outcome of evaluating a_minus_b_whole_cubed_plus_3ab_times_a_minus_b({a}, {b})",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
