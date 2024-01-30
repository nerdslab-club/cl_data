import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_product_example(count: int, identifier: int | None, max_list_length: int = 5):
    examples = []
    for i in range(count):
        numbers = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(numbers, (None if identifier is None else identifier+i)),
            "outputStr": f"##product({numbers})",
        })
    return examples


def __random_explanation(list_str: list, identifier: int | None) -> str:
    list_str = " , ".join(str(num) for num in list_str)

    explanations = [
        f"The product of the numbers {list_str}",
        f"Find the product of the list {list_str}",
        f"The result of PRODUCT({list_str})",
        f"Calculate the product of the numbers {list_str}",
        f"Finding PRODUCT for the list {list_str}",
        f"The multiplication of the numbers {list_str}",
        f"The product of the list {list_str}, what is it",
        f"The product of the list {list_str}, what does it give",
        f"Let's find the product of the numbers {list_str}",
        f"Find the PRODUCT for the list {list_str}",
        f"The product of the list {list_str}, result is",
        f"Calculating the product of the numbers {list_str}",
        f"The result of multiplying the numbers {list_str}",
        f"The product of the list {list_str}, what is its value",
        f"Let's determine the product of the numbers {list_str}",
        f"The multiplication result of the numbers {list_str}",
        f"{list_str}, what is their product",
        f"Finding the product of the numbers {list_str}",
        f"The product of the list {list_str}, what is its value",
        f"Find the product of the numbers {list_str} and provide the result",
        f"The product of the numbers {list_str}, ignoring order",
        f"The result of multiplying the elements in the list {list_str}",
        f"The multiplication of the numbers {list_str}, what is it",
        f"Calculate the product of the list {list_str}, find the answer",
        f"The product of the numbers {list_str}, what does it give",
        f"Let's find the result of multiplying the numbers {list_str}",
        f"{list_str}, their product, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_product_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
