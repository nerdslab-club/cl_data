import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_perfect_square_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_perfect_square({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Check if {x} is a perfect square",
        f"IS_PERFECT_SQUARE({x})",
        f"Determine if {x} is a perfect square",
        f"The result of is perfect square({x})",
        f"Verify whether {x} is a perfect square",
        f"Checking is perfect square for {x}",
        f"Decide if {x} is a perfect square",
        f"is perfect square calculation: {x}",
        f"Is {x} a perfect square?",
        f"Is {x} a perfect square? What does it give?",
        f"Let's check if {x} is a perfect square",
        f"Check is perfect square for {x}",
        f"Is {x} a perfect square? The result is",
        f"Determining if {x} is a perfect square",
        f"Verifying whether {x} is a perfect square",
        f"Is {x} a perfect square? What is its value?",
        f"Let's decide if {x} is a perfect square",
        f"Check if {x} is a perfect square, find the answer",
        f"Is {x} a perfect square? Result: ",
        f"Checking the perfect square property of {x}",
        f"Is {x} a perfect square? What is its status?",
        f"Check if {x} is a perfect square and provide the result",
        f"IS_PERFECT_SQUARE({x}), what does it yield?",
        f"Is {x} a perfect square? Ignoring order",
        f"Is {x} a perfect square? The decision is",
        f"Determine whether {x} is a perfect square, find the answer",
        f"Check if {x} is a perfect square. What is the result?",
        f"Is {x} a perfect square? Let's find out",
        f"is perfect square status for {x}, is it a perfect square or not?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_perfect_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
