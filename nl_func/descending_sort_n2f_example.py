import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_descending_sort_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 10)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##descending_sort({numbers})",
        })
    return examples


def __random_explanation(vector: list) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"Sort the list {lst_str} in descending order",
        f"DESCENDING_SORT({vector})",
        f"Arrange the elements in {lst_str} in descending order",
        f"The result of sorting {lst_str} in descending order",
        f"Perform descending sort on the list {lst_str}",
        f"Sorting {lst_str} in descending order",
        f"The sorted version of {lst_str} in descending order",
        f"DESCENDING_SORT calculation: {lst_str}",
        f"The result after arranging {lst_str} in descending order, what is it?",
        f"The sorted order of {lst_str} in descending fashion, what does it give?",
        f"Let's sort {lst_str} in descending order",
        f"Sort the list {lst_str} in descending order, result is",
        f"Calculating the descending sort for {lst_str}",
        f"The sorted result after sorting {lst_str} in descending order",
        f"The arrangement of {lst_str} in descending order, what is its value?",
        f"Let's determine the sorted order of {lst_str} in descending fashion",
        f"The sorted version of {lst_str} in descending order",
        f"Sort {lst_str} in descending order, what is the result?",
        f"The arrangement of {lst_str} in descending order, what does it give?",
        f"Sort {lst_str} in descending order and provide the result",
        f"DESCENDING_SORT({vector}), what does it yield?",
        f"The sorted order of {lst_str} in descending fashion, ignoring order",
        f"The result after sorting {lst_str} in descending order",
        f"The arrangement of {lst_str} in descending order, what is it?",
        f"Calculate the descending sort for {lst_str}, find the answer",
        f"The sorted order of {lst_str} in descending fashion, what does it give?",
        f"Let's find the result after sorting {lst_str} in descending order",
        f"Sort {lst_str} in descending order, what is the output?",
        f"The sorted result after sorting {lst_str} in descending order, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_descending_sort_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
