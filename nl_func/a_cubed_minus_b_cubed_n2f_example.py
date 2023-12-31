import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_a_cubed_minus_b_cubed_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b),
            "outputStr": f"##a_cubed_minus_b_cubed({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Calculate {a}^3 - {b}^3",
        f"A_CUBED_MINUS_B_CUBED({a}, {b})",
        f"Determine the result of {a}^3 - {b}^3",
        f"Find the expression {a}^3 - {b}^3",
        f"The result of calculating {a}^3 - {b}^3",
        f"Performing the a_cubed_minus_b_cubed operation for {a} and {b}",
        f"The expression {a}^3 - {b}^3",
        f"A_CUBED_MINUS_B_CUBED operation: ({a}, {b})",
        f"The result after calculating {a}^3 - {b}^3, what is it?",
        f"Determine {a}^3 - {b}^3",
        f"Let's calculate {a}^3 - {b}^3",
        f"The result of {a}^3 - {b}^3, is it true?",
        f"Calculating {a}^3 - {b}^3",
        f"The result after calculating a_cubed_minus_b_cubed for {a} and {b}",
        f"The expression {a}^3 - {b}^3, what is its value?",
        f"Let's determine the expression {a}^3 - {b}^3",
        f"The expression {a}^3 - {b}^3",
        f"The expression {a}^3 - {b}^3, what is the result?",
        f"The expression {a}^3 - {b}^3, what does it give?",
        f"The expression {a}^3 - {b}^3 and provide the result",
        f"A_CUBED_MINUS_B_CUBED({a}, {b}), what does it yield?",
        f"The expression {a}^3 - {b}^3, ignoring order",
        f"The result after calculating the expression {a}^3 - {b}^3",
        f"Calculate {a}^3 - {b}^3, find the answer",
        f"The expression {a}^3 - {b}^3, what does it give?",
        f"Let's find the result after calculating the expression {a}^3 - {b}^3",
        f"The expression {a}^3 - {b}^3, what is the output?",
        f"The result after calculating the expression {a}^3 - {b}^3, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_cubed_minus_b_cubed_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
