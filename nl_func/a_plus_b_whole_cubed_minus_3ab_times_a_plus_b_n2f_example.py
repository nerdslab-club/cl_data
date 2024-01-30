import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Determine the result of ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Find the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result of calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Performing the a_plus_b_whole_cubed_minus_3ab_times_a_plus_b operation for {a} and {b}",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result after calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is it",
        f"Determine ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Let's calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result of ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), is it true",
        f"Calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result after calculating a_plus_b_whole_cubed_minus_3ab_times_a_plus_b for {a} and {b}",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is its value",
        f"Let's determine the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is the result",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), ignoring order",
        f"The result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), find the answer",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what does it give",
        f"Let's find the result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is the output",
        f"The result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
