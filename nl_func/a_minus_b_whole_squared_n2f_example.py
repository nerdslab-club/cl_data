import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_a_minus_b_whole_squared_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b),
            "outputStr": f"##a_minus_b_whole_squared({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Calculate ({a} - {b})^2",
        f"A_MINUS_B_WHOLE_SQUARED({a}, {b})",
        f"Determine the result of ({a} - {b})^2",
        f"Find the expression ({a} - {b})^2",
        f"The result of calculating ({a} - {b})^2",
        f"Performing the a_minus_b_whole_squared operation for {a} and {b}",
        f"The expression ({a} - {b})^2",
        f"A_MINUS_B_WHOLE_SQUARED operation: ({a}, {b})",
        f"The result after calculating ({a} - {b})^2, what is it?",
        f"Determine ({a} - {b})^2",
        f"Let's calculate ({a} - {b})^2",
        f"The result of ({a} - {b})^2, is it true?",
        f"Calculating ({a} - {b})^2",
        f"The result after calculating a_minus_b_whole_squared for {a} and {b}",
        f"The expression ({a} - {b})^2, what is its value?",
        f"Let's determine the expression ({a} - {b})^2",
        f"The expression ({a} - {b})^2",
        f"The expression ({a} - {b})^2, what is the result?",
        f"The expression ({a} - {b})^2, what does it give?",
        f"The expression ({a} - {b})^2 and provide the result",
        f"A_MINUS_B_WHOLE_SQUARED({a}, {b}), what does it yield?",
        f"The expression ({a} - {b})^2, ignoring order",
        f"The result after calculating the expression ({a} - {b})^2",
        f"Calculate ({a} - {b})^2, find the answer",
        f"The expression ({a} - {b})^2, what does it give?",
        f"Let's find the result after calculating the expression ({a} - {b})^2",
        f"The expression ({a} - {b})^2, what is the output?",
        f"The result after calculating the expression ({a} - {b})^2, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_minus_b_whole_squared_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
