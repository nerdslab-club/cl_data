import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_is_perfect_cube_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##is_perfect_cube({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Check if {a} is a perfect cube",
        f"IS_PERFECT_CUBE({a})",
        f"Determine if {a} is a perfect cube",
        f"The result of is perfect cube({a})",
        f"Verify whether {a} is a perfect cube",
        f"Checking is perfect cube for {a}",
        f"Decide if {a} is a perfect cube",
        f"is perfect cube calculation: {a}",
        f"Is {a} a perfect cube?",
        f"Is {a} a perfect cube? What does it give?",
        f"Let's check if {a} is a perfect cube",
        f"Check is perfect cube for {a}",
        f"Is {a} a perfect cube? The result is",
        f"Determining if {a} is a perfect cube",
        f"Verifying whether {a} is a perfect cube",
        f"Is {a} a perfect cube? What is its value?",
        f"Let's decide if {a} is a perfect cube",
        f"Check if {a} is a perfect cube, find the answer",
        f"Is {a} a perfect cube? Result: ",
        f"Checking the perfect cube property of {a}",
        f"Is {a} a perfect cube? What is its status?",
        f"Check if {a} is a perfect cube and provide the result",
        f"IS_PERFECT_CUBE({a}), what does it yield?",
        f"Is {a} a perfect cube? Ignoring order",
        f"Is {a} a perfect cube? The decision is",
        f"Determine whether {a} is a perfect cube, find the answer",
        f"Check if {a} is a perfect cube. What is the result?",
        f"Is {a} a perfect cube? Let's find out",
        f"Is perfect cube status for {a}, is it a perfect cube or not?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_perfect_cube_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
