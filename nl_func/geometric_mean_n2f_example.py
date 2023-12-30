import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_geometric_mean_example(count: int):
    examples = []
    for _ in range(count):
        numbers = RandomValueGenerator.generate_random_list(5, 1, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##geometric_mean({numbers})",
        })
    return examples


def __random_explanation(numbers: list[float]) -> str:
    explanations = [
        f"Calculate the geometric mean of the list {numbers}",
        f"GEOMETRIC_MEAN({numbers})",
        f"Determine the geometric mean of the elements in the list {numbers}",
        f"Find the geometric mean value for the list {numbers}",
        f"The result of calculating the geometric mean of {numbers}",
        f"Performing the geometric mean operation on the list {numbers}",
        f"The geometric mean of the list {numbers}",
        f"GEOMETRIC_MEAN calculation: {numbers}",
        f"The result after calculating the geometric mean of {numbers}, what is it?",
        f"The geometric mean value of {numbers}, what does it give?",
        f"Let's find the geometric mean value of the list {numbers}",
        f"Geometric mean of the list {numbers}, result is",
        f"Calculating the geometric mean for the list {numbers}",
        f"The geometric mean result after calculating the geometric mean of {numbers}",
        f"The geometric mean of the list {numbers}, what is its value?",
        f"Let's determine the geometric mean of the list {numbers}",
        f"The geometric mean value of the list {numbers}",
        f"The geometric mean of the list {numbers}, what is the result?",
        f"The geometric mean of the list {numbers}, what does it give?",
        f"The geometric mean of the list {numbers} and provide the result",
        f"GEOMETRIC_MEAN({numbers}), what does it yield?",
        f"The geometric mean value of the list {numbers}, ignoring order",
        f"The result after calculating the geometric mean of {numbers}",
        f"The geometric mean of the list {numbers}, what is it?",
        f"Calculate the geometric mean of the list {numbers}, find the answer",
        f"The geometric mean of the list {numbers}, what does it give?",
        f"Let's find the result after calculating the geometric mean of {numbers}",
        f"Geometric mean of the list {numbers}, what is the output?",
        f"The result after calculating the geometric mean of {numbers}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_geometric_mean_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
