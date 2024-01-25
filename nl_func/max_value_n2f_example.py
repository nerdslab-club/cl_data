import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_max_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list(5, 0, 100)
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##max_value({numbers})",
        })
    return examples


def __random_explanation(list_str: list[int], identifier: int | None) -> str:
    list_str = " , ".join(str(num) for num in list_str)

    explanations = [
        f"Find the maximum value in the list {list_str}",
        f"MAX_VALUE({list_str})",
        f"Determine the largest value in the list {list_str}",
        f"Find the maximum element in the list {list_str}",
        f"Locate the highest value in the list {list_str}",
        f"Searching for the maximum value in the list {list_str}",
        f"MAX_VALUE calculation: {list_str}",
        f"The result after finding the maximum value in the list {list_str}, what is it?",
        f"The maximum value in the list {list_str}, what does it give?",
        f"Let's find the maximum value in the list {list_str}",
        f"The maximum value in the list {list_str}, result is",
        f"Searching for the largest value in the list {list_str}",
        f"The maximum element after finding the maximum value in the list {list_str}",
        f"The highest value in the list {list_str}, what is its value?",
        f"Let's determine the maximum value in the list {list_str}",
        f"The maximum value in the list {list_str}",
        f"The maximum value in the list {list_str}, what is the result?",
        f"The maximum value in the list {list_str}, what does it give?",
        f"The maximum value in the list {list_str} and provide the result",
        f"MAX_VALUE({list_str}), what does it yield?",
        f"The maximum value in the list {list_str}, ignoring order",
        f"The result after finding the maximum value in the list {list_str}",
        f"The maximum value in the list {list_str}, what is it?",
        f"Calculate the maximum value in the list {list_str}, find the answer",
        f"The maximum value in the list {list_str}, what does it give?",
        f"Let's find the result after finding the maximum value in the list {list_str}",
        f"The maximum value in the list {list_str}, what is the output?",
        f"The result after finding the maximum value in the list {list_str}, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_max_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
