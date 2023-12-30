import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_perfect_cube_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_perfect_cube({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Check if {x} is a perfect cube",
        f"IS_PERFECT_CUBE({x})",
        f"Determine if {x} is a perfect cube",
        f"The result of is perfect cube({x})",
        f"Verify whether {x} is a perfect cube",
        f"Checking is perfect cube for {x}",
        f"Decide if {x} is a perfect cube",
        f"is perfect cube calculation: {x}",
        f"Is {x} a perfect cube?",
        f"Is {x} a perfect cube? What does it give?",
        f"Let's check if {x} is a perfect cube",
        f"Check is perfect cube for {x}",
        f"Is {x} a perfect cube? The result is",
        f"Determining if {x} is a perfect cube",
        f"Verifying whether {x} is a perfect cube",
        f"Is {x} a perfect cube? What is its value?",
        f"Let's decide if {x} is a perfect cube",
        f"Check if {x} is a perfect cube, find the answer",
        f"Is {x} a perfect cube? Result: ",
        f"Checking the perfect cube property of {x}",
        f"Is {x} a perfect cube? What is its status?",
        f"Check if {x} is a perfect cube and provide the result",
        f"IS_PERFECT_CUBE({x}), what does it yield?",
        f"Is {x} a perfect cube? Ignoring order",
        f"Is {x} a perfect cube? The decision is",
        f"Determine whether {x} is a perfect cube, find the answer",
        f"Check if {x} is a perfect cube. What is the result?",
        f"Is {x} a perfect cube? Let's find out",
        f"Is perfect cube status for {x}, is it a perfect cube or not?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_perfect_cube_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
