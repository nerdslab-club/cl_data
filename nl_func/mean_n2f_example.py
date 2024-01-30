import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_mean_example(count: int, identifier: int | None, max_list_length: int = 5):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##mean({numbers})",
        })
    return examples


def __random_explanation(list_str: list, identifier: int | None) -> str:
    list_str = " , ".join(str(num) for num in list_str)

    explanations = [
        f"Calculate the mean of the numbers {list_str}",
        f"Find the average of the numbers {list_str}",
        f"Determine the mean value for the list {list_str}",
        f"Calculating the mean for the numbers {list_str}",
        f"The average value of the numbers {list_str}",
        f"The mean of the list {list_str}, what is it",
        f"The mean of the numbers {list_str}, what does it give",
        f"Let's find the mean of the numbers {list_str}",
        f"Find the MEAN for the list {list_str}",
        f"The mean of the list {list_str}, result is",
        f"Calculating the average of the numbers {list_str}",
        f"The result of averaging the numbers {list_str}",
        f"The mean of the list {list_str}, what is its value",
        f"Let's determine the mean of the numbers {list_str}",
        f"The average value of the numbers in the list: {list_str}",
        f"{list_str}, what is their mean",
        f"Finding the mean of the numbers {list_str}",
        f"The mean of the list {list_str}, what is its value",
        f"Find the average of the numbers {list_str} and provide the result",
        f"The mean of the numbers {list_str}, ignoring order",
        f"The result of averaging the elements in the list {list_str}",
        f"The average value of the numbers {list_str}, what is it",
        f"Calculate the mean of the list {list_str}, find the answer",
        f"The mean of the numbers {list_str}, what does it give",
        f"Let's find the result of averaging the numbers {list_str}",
        f"{list_str}, their mean, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_mean_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
