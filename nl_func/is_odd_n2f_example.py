import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_odd_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_odd({num})",
        })
    return examples


def __random_explanation(a: int) -> str:
    explanations = [
        f"Determine if the integer {a} is odd",
        f"IS_ODD({a})",
        f"Check if {a} is an odd number",
        f"Is {a} an odd number?",
        f"Verify whether {a} is an odd number",
        f"Checking if {a} is odd",
        f"IS_ODD calculation: {a}",
        f"Is {a} not divisible by 2?",
        f"Check if {a} is an odd integer",
        f"Let's determine if {a} is an odd number",
        f"Is {a} even or odd?",
        f"Determine the oddness of {a}",
        f"Checking the oddness of {a}",
        f"Is {a} not divisible evenly by 2?",
        f"Check if {a} is an even or odd number",
        f"Determine whether {a} is odd",
        f"Verify if {a} is an odd number",
        f"Check if {a} is an even or odd integer",
        f"IS_ODD({a}), what does it yield?",
        f"Checking the non-divisibility of {a} by 2",
        f"Is {a} an odd number or not?",
        f"Determine if {a} is not divisible by 2",
        f"Check if {a} is an even or odd number, result is",
        f"Let's find out if {a} is an odd number",
        f"Is {a} not divisible by 2 without remainder?",
        f"Check if {a} is an odd integer or not",
        f"Verify the oddness of {a}",
        f"IS_ODD({a}), is it true or false?",
        f"Determine if {a} is not divisible evenly by 2",
        f"Is {a} an even or odd integer?",
        f"Check if {a} is not divisible by 2, what is the answer?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_odd_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
