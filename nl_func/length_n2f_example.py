import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_length_example(count: int):
    examples = []
    for _ in range(count):
        numbers = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##length({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"Calculate the length of the list {numbers}",
        f"LENGTH({numbers})",
        f"Determine the result of the length for the list {numbers}",
        f"Find the length of the list {numbers}",
        f"The result of calculating the length of the list {numbers}",
        f"Performing the length calculation for the list {numbers}",
        f"The length of the list {numbers}",
        f"LENGTH calculation: {numbers}",
        f"The result after calculating the length of the list {numbers}, what is it?",
        f"The length of the list {numbers}, what does it give?",
        f"Let's calculate the length of the list {numbers}",
        f"The length of the list {numbers}, result is",
        f"Calculating the length of the list {numbers}",
        f"The length result after calculating length for the list {numbers}",
        f"The length of the list {numbers}, what is its value?",
        f"Let's determine the length of the list {numbers}",
        f"The length of the list {numbers}",
        f"The length of the list {numbers}, what is the result?",
        f"The length of the list {numbers}, what does it give?",
        f"The length of the list {numbers} and provide the result",
        f"LENGTH({numbers}), what does it yield?",
        f"The length of the list {numbers}, ignoring order",
        f"The result after calculating the length of the list {numbers}",
        f"The length of the list {numbers}, what is it?",
        f"Calculate the length of the list {numbers}, find the answer",
        f"The length of the list {numbers}, what does it give?",
        f"Let's find the result after calculating the length of the list {numbers}",
        f"The length of the list {numbers}, what is the output?",
        f"The result after calculating the length of the list {numbers}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_length_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
