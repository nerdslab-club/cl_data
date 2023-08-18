import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_median_example(count: int):
    examples = []
    for _ in range(count):
        num_count = random.randint(3, 6)  # Generate 3 to 6 numbers
        numbers = [random.uniform(-100.0, 100.0) for _ in range(num_count)]
        examples.append(
            {
                "inputStr": f"##median({numbers})",
                "outputStr": __random_explanation_median(numbers),
            }
        )
    return examples


def __random_explanation_median(numbers: list) -> str:
    num_str = ", ".join(str(num) for num in numbers)
    explanations = [
        f"The median of the numbers {num_str}",
        f"median({num_str})",
        f"The middle value of the numbers {num_str}",
        f"Calculation: median({num_str})",
        f"The value at the center of the sorted numbers {num_str}",
        f"The value that separates the data set {num_str} into two halves",
        f"The result of calculating the median of the elements {num_str}",
        f"The middle value of the dataset {num_str}",
        f"The median value of the numbers {num_str}",
        f"The value that lies in the middle of the ordered numbers {num_str}",
        f"The value obtained by sorting the numbers {num_str} and taking the middle",
        f"The computed result of finding the median of {num_str}",
        f"The result of evaluating median({num_str})",
        f"The outcome of determining the median of {num_str}",
        f"The median of the set {num_str}",
        f"The outcome of finding the middle value of {num_str}",
        f"The value at the center of the sorted set {num_str} is",
        f"The value that divides the data set {num_str} into two halves is",
        f"The calculated result of median({num_str}) is",
        f"The middle value of the numbers {num_str} is",
        f"The value of the median of {num_str} is",
        f"The median of the elements {num_str} is",
        f"The result of calculating median({num_str}) is",
        f"The outcome of finding the median value of {num_str} is",
        f"The value in the middle of the sorted list {num_str} is",
        f"The value that separates the numbers {num_str} into two halves is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_median_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
