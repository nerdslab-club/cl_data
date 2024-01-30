import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_min_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##min_value({numbers})",
        })
    return examples


def __random_explanation(list_str: list[int], identifier: int | None) -> str:
    list_str = " , ".join(str(num) for num in list_str)

    explanations = [
        f"Find the minimum value in the list {list_str}",
        f"Determine the smallest value in the list {list_str}",
        f"Find the minimum element in the list {list_str}",
        f"Locate the lowest value in the list {list_str}",
        f"Searching for the minimum value in the list {list_str}",
        f"The result after finding the minimum value in the list {list_str}, what is it",
        f"The minimum value in the list {list_str}, what does it give",
        f"Let's find the minimum value in the list {list_str}",
        f"The minimum value in the list {list_str}, result is",
        f"Searching for the smallest value in the list {list_str}",
        f"The minimum element after finding the minimum value in the list {list_str}",
        f"The smallest value in the list {list_str}, what is its value",
        f"Let's determine the minimum value in the list {list_str}",
        f"The minimum value in the list {list_str}, what is the result",
        f"The result after finding the minimum value in the list {list_str}",
        f"The minimum value in the list {list_str}, what is it",
        f"Calculate the minimum value in the list {list_str}, find the answer",
        f"The minimum value in the list {list_str}, what does it give",
        f"Let's find the result after finding the minimum value in the list {list_str}",
        f"The minimum value in the list {list_str}, what is the output",
        f"The result after finding the minimum value in the list {list_str}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_min_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
