import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b),
            "outputStr": f"##a_plus_b_whole_cubed_minus_3ab_times_a_plus_b({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"A_PLUS_B_WHOLE_CUBED_MINUS_3AB_TIMES_A_PLUS_B({a}, {b})",
        f"Determine the result of ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Find the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result of calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Performing the a_plus_b_whole_cubed_minus_3ab_times_a_plus_b operation for {a} and {b}",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"A_PLUS_B_WHOLE_CUBED_MINUS_3AB_TIMES_A_PLUS_B operation: ({a}, {b})",
        f"The result after calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is it?",
        f"Determine ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Let's calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result of ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), is it true?",
        f"Calculating ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The result after calculating a_plus_b_whole_cubed_minus_3ab_times_a_plus_b for {a} and {b}",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is its value?",
        f"Let's determine the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is the result?",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what does it give?",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}) and provide the result",
        f"A_PLUS_B_WHOLE_CUBED_MINUS_3AB_TIMES_A_PLUS_B({a}, {b}), what does it yield?",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), ignoring order",
        f"The result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"Calculate ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), find the answer",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what does it give?",
        f"Let's find the result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b})",
        f"The expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is the output?",
        f"The result after calculating the expression ({a} + {b})^3 - 3({a} * {b}) * ({a} + {b}), what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
