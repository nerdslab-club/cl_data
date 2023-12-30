import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_even_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_even({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Determine if the integer {x} is even",
        f"IS_EVEN({x})",
        f"Check if {x} is an even number",
        f"Is {x} an even number?",
        f"Verify whether {x} is an even number",
        f"Checking if {x} is even",
        f"IS_EVEN calculation: {x}",
        f"Is {x} divisible by 2?",
        f"Check if {x} is an even integer",
        f"Let's determine if {x} is an even number",
        f"Is {x} even or odd?",
        f"Determine the evenness of {x}",
        f"Checking the evenness of {x}",
        f"Is {x} divisible evenly by 2?",
        f"Check if {x} is an even or odd number",
        f"Determine whether {x} is even",
        f"Verify if {x} is an even number",
        f"Check if {x} is an even or odd integer",
        f"IS_EVEN({x}), what does it yield?",
        f"Checking the divisibility of {x} by 2",
        f"Is {x} an even number or not?",
        f"Determine if {x} is divisible by 2",
        f"Check if {x} is an even or odd number, result is",
        f"Let's find out if {x} is an even number",
        f"Is {x} divisible by 2 without remainder?",
        f"Check if {x} is an even integer or not",
        f"Verify the evenness of {x}",
        f"IS_EVEN({x}), is it true or false?",
        f"Determine if {x} is divisible evenly by 2",
        f"Is {x} an even or odd integer?",
        f"Check if {x} is divisible by 2, what is the answer?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_even_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
