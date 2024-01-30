import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility
from cl_data.src.random_value_generator import RandomValueGenerator


def create_f2n_average_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append(
            {
                "inputStr": f"##average({numbers})",
                "outputStr": __random_explanation_average(numbers, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_average(lst: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in lst)
    explanations = [
        f"Calculate the average of the numbers {lst_str}",
        f"Determine the result of the average for the numbers {lst_str}",
        f"Find the average of the numbers {lst_str}",
        f"The result of calculating the average of the numbers {lst_str}",
        f"Performing the average calculation for the numbers {lst_str}",
        f"The average of the numbers {lst_str}",
        f"The result after calculating the average of the numbers {lst_str}, what is it",
        f"The average of the numbers {lst_str}, what does it give",
        f"Let's calculate the average of the numbers {lst_str}",
        f"The average of the numbers {lst_str}, result is",
        f"Calculating the average of the numbers {lst_str}",
        f"The average result after calculating average for the numbers {lst_str}",
        f"The average of the numbers {lst_str}, what is its value",
        f"Let's determine the average of the numbers {lst_str}",
        f"The average of the numbers {lst_str}",
        f"The average of the numbers {lst_str}, what is the result",
        f"The average of the numbers {lst_str}, what does it give",
        f"The average of the numbers {lst_str} and provide the result",
        f"The average of the numbers {lst_str}, ignoring order",
        f"The result after calculating the average of the numbers {lst_str}",
        f"The average of the numbers {lst_str}, what is it",
        f"Calculate the average of the numbers {lst_str}, find the answer",
        f"The average of the numbers {lst_str}, what does it give",
        f"Let's find the result after calculating the average of the numbers {lst_str}",
        f"The average of the numbers {lst_str}, what is the output",
        f"The result after calculating the average of the numbers {lst_str}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_average_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
