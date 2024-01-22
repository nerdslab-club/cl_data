import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


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
    lst_str = ", ".join(str(num) for num in numbers)
    explanations = [
        f"The median of the numbers {lst_str}",
        f"median({lst_str})",
        f"The middle value of the numbers {lst_str}",
        f"Calculation: median({lst_str})",
        f"The value at the center of the sorted numbers {lst_str}",
        f"The value that separates the data set {lst_str} into two halves",
        f"The result of calculating the median of the elements {lst_str}",
        f"The middle value of the dataset {lst_str}",
        f"The median value of the numbers {lst_str}",
        f"The value that lies in the middle of the ordered numbers {lst_str}",
        f"The value obtained by sorting the numbers {lst_str} and taking the middle",
        f"The computed result of finding the median of {lst_str}",
        f"The result of evaluating median({lst_str})",
        f"The outcome of determining the median of {lst_str}",
        f"The median of the set {lst_str}",
        f"The outcome of finding the middle value of {lst_str}",
        f"The value at the center of the sorted set {lst_str} is",
        f"The value that divides the data set {lst_str} into two halves is",
        f"The calculated result of median({lst_str}) is",
        f"The middle value of the numbers {lst_str} is",
        f"The value of the median of {lst_str} is",
        f"The median of the elements {lst_str} is",
        f"The result of calculating median({lst_str}) is",
        f"The outcome of finding the median value of {lst_str} is",
        f"The value in the middle of the sorted list {lst_str} is",
        f"The value that separates the numbers {lst_str} into two halves is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_median_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
