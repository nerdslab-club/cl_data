import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_geometric_mean_example(count: int):
    examples = []
    for _ in range(count):
        lst = [random.uniform(0.1, 1000.0) for _ in range(random.randint(2, 10))]
        examples.append(
            {
                "inputStr": f"##geometric_mean({lst})",
                "outputStr": __random_explanation_geometric_mean(lst),
            }
        )
    return examples


def __random_explanation_geometric_mean(lst_one: list[float]) -> str:
    lst = ", ".join(str(num) for num in lst_one)
    explanations = [
        f"The geometric mean of the numbers in the list {lst}",
        f"geometric_mean({lst})",
        f"The result of calculating the geometric mean of {lst}",
        f"Calculation: geometric_mean({lst})",
        f"The mean value obtained by using the geometric mean formula for the numbers {lst}",
        f"The outcome of finding the geometric mean of the provided numbers {lst}",
        f"The geometric mean value of the numbers in the list {lst}",
        f"The mean value calculated using the geometric mean approach for the numbers {lst}",
        f"The computed result of determining the geometric mean of the values {lst}",
        f"The mean value derived using the geometric mean formula for the numbers {lst}",
        f"The average value obtained by using the geometric mean method for the numbers {lst}",
        f"The outcome of evaluating geometric_mean({lst})",
        f"The value calculated by finding the geometric mean of the numbers {lst}",
        f"The result of evaluating geometric_mean({lst})",
        f"The value obtained by applying the geometric mean formula to the numbers {lst}",
        f"The computed geometric mean value of the numbers {lst}",
        f"The mean value obtained through the geometric mean formula for the numbers {lst}",
        f"The result derived from calculating the geometric mean of the numbers {lst}",
        f"The calculated outcome of evaluating geometric_mean({lst})",
        f"The average value of the numbers calculated using geometric_mean for the numbers {lst}",
        f"The computed value of the geometric mean of the numbers {lst}",
        f"The calculated result of determining the geometric mean of the provided values {lst}",
        f"The mean value derived from the geometric mean of the numbers {lst}",
        f"The value obtained through the geometric mean calculation for the numbers {lst}",
        f"The result obtained by finding the geometric mean of the provided numbers {lst}",
        f"The computed mean value of the numbers using the geometric mean formula for the numbers {lst}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_geometric_mean_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
