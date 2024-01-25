import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_geometric_mean_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        lst = [random.uniform(0.1, 1000.0) for _ in range(random.randint(2, 10))]
        examples.append(
            {##geometric_mean({vector1_list})
                "inputStr": f"##geometric_mean({lst})",
                "outputStr": __random_explanation_geometric_mean(lst, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_geometric_mean(lst_one: list[float], identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in lst_one)
    explanations = [
        f"The geometric mean of the numbers in the list {lst_str}",
        f"geometric_mean({lst_str})",
        f"The result of calculating the geometric mean of {lst_str}",
        f"Calculation: geometric_mean({lst_str})",
        f"The mean value obtained by using the geometric mean formula for the numbers {lst_str}",
        f"The outcome of finding the geometric mean of the provided numbers {lst_str}",
        f"The geometric mean value of the numbers in the list {lst_str}",
        f"The mean value calculated using the geometric mean approach for the numbers {lst_str}",
        f"The computed result of determining the geometric mean of the values {lst_str}",
        f"The mean value derived using the geometric mean formula for the numbers {lst_str}",
        f"The average value obtained by using the geometric mean method for the numbers {lst_str}",
        f"The outcome of evaluating geometric_mean({lst_str})",
        f"The value calculated by finding the geometric mean of the numbers {lst_str}",
        f"The result of evaluating geometric_mean({lst_str})",
        f"The value obtained by applying the geometric mean formula to the numbers {lst_str}",
        f"The computed geometric mean value of the numbers {lst_str}",
        f"The mean value obtained through the geometric mean formula for the numbers {lst_str}",
        f"The result derived from calculating the geometric mean of the numbers {lst_str}",
        f"The calculated outcome of evaluating geometric_mean({lst_str})",
        f"The average value of the numbers calculated using geometric_mean for the numbers {lst_str}",
        f"The computed value of the geometric mean of the numbers {lst_str}",
        f"The calculated result of determining the geometric mean of the provided values {lst_str}",
        f"The mean value derived from the geometric mean of the numbers {lst_str}",
        f"The value obtained through the geometric mean calculation for the numbers {lst_str}",
        f"The result obtained by finding the geometric mean of the provided numbers {lst_str}",
        f"The computed mean value of the numbers using the geometric mean formula for the numbers {lst_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_geometric_mean_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
