import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_median_example(count: int, identifier: int | None, max_list_length: int = 5):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##median({numbers})",
        })
    return examples


def __random_explanation(list_str: list, identifier: int | None) -> str:
    list_str = " , ".join(str(num) for num in list_str)

    explanations = [
        f"Calculate the median of the numbers {list_str}",
        f"Find the median value for the list {list_str}",
        f"Determine the median for the numbers {list_str}",
        f"Calculating the median for the numbers {list_str}",
        f"The median value of the numbers {list_str}",
        f"MEDIAN calculation: {list_str}",
        f"Let's find the median of the numbers {list_str}",
        f"Find the MEDIAN for the list {list_str}",
        f"The median of the list {list_str}, result is",
        f"Calculating the median of the numbers {list_str}",
        f"The result of finding the median of the numbers {list_str}",
        f"Let's determine the median of the numbers {list_str}",
        f"The median value of the numbers in the list: {list_str}",
        f"Finding the median of the numbers {list_str}",
        f"Find the median of the numbers {list_str} and provide the result",
        f"The result of finding the median of the elements in the list {list_str}",
        f"Calculate the median of the list {list_str}, find the answer",
        f"Let's find the result of finding the median of the numbers {list_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_median_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
