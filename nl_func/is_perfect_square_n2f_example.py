import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_is_perfect_square_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##is_perfect_square({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Check if {a} is a perfect square",
        f"IS_PERFECT_SQUARE({a})",
        f"Determine if {a} is a perfect square",
        f"The result of is perfect square({a})",
        f"Verify whether {a} is a perfect square",
        f"Checking is perfect square for {a}",
        f"Decide if {a} is a perfect square",
        f"is perfect square calculation: {a}",
        f"Is {a} a perfect square?",
        f"Is {a} a perfect square? What does it give?",
        f"Let's check if {a} is a perfect square",
        f"Check is perfect square for {a}",
        f"Is {a} a perfect square? The result is",
        f"Determining if {a} is a perfect square",
        f"Verifying whether {a} is a perfect square",
        f"Is {a} a perfect square? What is its value?",
        f"Let's decide if {a} is a perfect square",
        f"Check if {a} is a perfect square, find the answer",
        f"Is {a} a perfect square? Result: ",
        f"Checking the perfect square property of {a}",
        f"Is {a} a perfect square? What is its status?",
        f"Check if {a} is a perfect square and provide the result",
        f"IS_PERFECT_SQUARE({a}), what does it yield?",
        f"Is {a} a perfect square? Ignoring order",
        f"Is {a} a perfect square? The decision is",
        f"Determine whether {a} is a perfect square, find the answer",
        f"Check if {a} is a perfect square. What is the result?",
        f"Is {a} a perfect square? Let's find out",
        f"is perfect square status for {a}, is it a perfect square or not?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_perfect_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
