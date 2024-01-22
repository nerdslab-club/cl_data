import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_median_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##median({numbers})",
        })
    return examples


def __random_explanation(list_str: list) -> str:
    list_str = ", ".join(str(num) for num in list_str)

    explanations = [
        f"Calculate the median of the numbers {list_str}",
        f"MEDIAN({list_str})",
        f"Find the median value for the list {list_str}",
        f"The result of MEDIAN({list_str})",
        f"Determine the median for the numbers {list_str}",
        f"Calculating the median for the numbers {list_str}",
        f"The median value of the numbers {list_str}",
        f"MEDIAN calculation: {list_str}",
        f"The median of the list {list_str}, what is it?",
        f"The median of the numbers {list_str}, what does it give?",
        f"Let's find the median of the numbers {list_str}",
        f"Find the MEDIAN for the list {list_str}",
        f"The median of the list {list_str}, result is",
        f"Calculating the median of the numbers {list_str}",
        f"The result of finding the median of the numbers {list_str}",
        f"The median of the list {list_str}, what is its value?",
        f"Let's determine the median of the numbers {list_str}",
        f"The median value of the numbers in the list: {list_str}",
        f"{list_str}, what is their median?",
        f"Finding the median of the numbers {list_str}",
        f"The median of the list {list_str}, what is its value?",
        f"Find the median of the numbers {list_str} and provide the result",
        f"MEDIAN({list_str}), what does it yield?",
        f"The median of the numbers {list_str}, ignoring order",
        f"The result of finding the median of the elements in the list {list_str}",
        f"The median value of the numbers {list_str}, what is it?",
        f"Calculate the median of the list {list_str}, find the answer",
        f"The median of the numbers {list_str}, what does it give?",
        f"Let's find the result of finding the median of the numbers {list_str}",
        f"{list_str}, their median, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_median_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
