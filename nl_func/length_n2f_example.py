import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_length_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##length({numbers})",
        })
    return examples


def __random_explanation(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"Calculate the length of the list {lst_str}",
        f"Determine the result of the length for the list {lst_str}",
        f"Find the length of the list {lst_str}",
        f"The result of calculating the length of the list {lst_str}",
        f"Performing the length calculation for the list {lst_str}",
        f"The length of the list {lst_str}",
        f"Let's calculate the length of the list {lst_str}",
        f"The length of the list {lst_str} result is",
        f"Calculating the length of the list {lst_str}",
        f"The length result after calculating length for the list {lst_str}",
        f"Let's determine the length of the list {lst_str}",
        f"The result after calculating the length of the list {lst_str}",
        f"Calculate the length of the list {lst_str} find the answer",
        f"Let's find the result after calculating the length of the list {lst_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_length_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
