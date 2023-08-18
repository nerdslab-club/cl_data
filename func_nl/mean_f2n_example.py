import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_mean_example(count: int):
    examples = []
    for _ in range(count):
        num_count = random.randint(2, 10)  # Generate 2 to 5 numbers
        numbers = [random.uniform(-100.0, 1000.0) for _ in range(num_count)]
        examples.append(
            {
                "inputStr": f"##mean({numbers})",
                "outputStr": __random_explanation_mean(numbers),
            }
        )
    return examples


def __random_explanation_mean(numbers: list) -> str:
    num_str = ", ".join(str(num) for num in numbers)
    explanations = [
        f"The mean of the numbers {num_str}",
        f"mean({num_str})",
        f"The average value of the numbers {num_str}",
        f"Calculation: mean({num_str})",
        f"The value obtained by averaging the numbers {num_str}",
        f"The outcome of finding the average of the elements {num_str}",
        f"The result of calculating the mean of the numbers {num_str}",
        f"The average value of the data set {num_str}",
        f"The arithmetic mean of the numbers {num_str}",
        f"The result of summing the numbers and dividing by the count",
        f"The average obtained by summing and dividing the numbers {num_str}",
        f"The computed result of finding the mean of {num_str}",
        f"The result of averaging the values {num_str}",
        f"The value calculated by adding and dividing the numbers {num_str}",
        f"The average value of the list {num_str}",
        f"The outcome of calculating the average of {num_str}",
        f"The mean of the elements {num_str} is",
        f"The average value of the set {num_str}",
        f"The calculated result of mean({num_str}) is",
        f"The average of the numbers {num_str} is",
        f"The value of the mean of {num_str} is",
        f"The result of evaluating mean({num_str}) is",
        f"The outcome of finding the average of the numbers {num_str} is",
        f"The average value calculated from {num_str} is",
        f"The value of the average of the numbers {num_str} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_mean_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
