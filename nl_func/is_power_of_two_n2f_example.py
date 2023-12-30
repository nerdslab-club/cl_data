import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_power_of_two_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_power_of_two({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Determine if the integer {x} is a power of two",
        f"IS_POWER_OF_TWO({x})",
        f"Check if {x} is a power of two",
        f"Is {x} a power of two?",
        f"Verify whether {x} is a power of two",
        f"Checking if {x} is a power of two",
        f"IS_POWER_OF_TWO calculation: {x}",
        f"Is {x} a power of two?",
        f"Check if {x} is a power of two integer",
        f"Let's determine if {x} is a power of two",
        f"Is {x} a power of two or not?",
        f"Determine if {x} is a power of two",
        f"Checking the power of two property of {x}",
        f"Is {x} a power of two?",
        f"Check if {x} is a power of two, result is",
        f"Determine whether {x} is a power of two",
        f"Verify if {x} is a power of two",
        f"Check if {x} is a power of two integer",
        f"IS_POWER_OF_TWO({x}), what does it yield?",
        f"Checking if {x} is a power of two without remainder",
        f"Is {x} a power of two or not?",
        f"Determine if {x} is a power of two, result is",
        f"Check if {x} is a power of two or not, result is",
        f"Let's find out if {x} is a power of two",
        f"Is {x} a power of two without remainder?",
        f"Check if {x} is a power of two integer or not",
        f"Verify the power of two property of {x}",
        f"IS_POWER_OF_TWO({x}), is it true or false?",
        f"Determine if {x} is a power of two without remainder",
        f"Is {x} a power of two or not, what is the answer?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_power_of_two_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
