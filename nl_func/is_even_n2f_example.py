import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_is_even_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##is_even({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Determine if the integer {a} is even",
        f"Check if {a} is an even number",
        f"Is {a} an even number",
        f"Verify whether {a} is an even number",
        f"Checking if {a} is even",
        f"Is {a} divisible by 2",
        f"Check if {a} is an even integer",
        f"Let's determine if {a} is an even number",
        f"Is {a} even or odd",
        f"Determine the evenness of {a}",
        f"Checking the evenness of {a}",
        f"Is {a} divisible evenly by 2",
        f"Check if {a} is an even or odd number",
        f"Determine whether {a} is even",
        f"Verify if {a} is an even number",
        f"Check if {a} is an even or odd integer",
        f"Checking the divisibility of {a} by 2",
        f"Is {a} an even number or not",
        f"Determine if {a} is divisible by 2",
        f"Check if {a} is an even or odd number, result is",
        f"Let's find out if {a} is an even number",
        f"Is {a} divisible by 2 without remainder",
        f"Check if {a} is an even integer or not",
        f"Verify the evenness of {a}",
        f"Determine if {a} is divisible evenly by 2",
        f"Is {a} an even or odd integer",
        f"Check if {a} is divisible by 2, what is the answer",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_even_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
