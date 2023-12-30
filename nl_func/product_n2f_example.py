import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_product_example(count: int, max_list_length: int = 5):
    examples = []
    for _ in range(count):
        length = RandomValueGenerator.generate_random_integer(2, max_list_length + 1)
        numbers = RandomValueGenerator.generate_random_list(length, -10, 10)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##product({numbers})",
        })
    return examples


def __random_explanation(numbers: list) -> str:
    explanations = [
        f"The product of the numbers {numbers}",
        f"PRODUCT({numbers})",
        f"Find the product of the list {numbers}",
        f"The result of PRODUCT({numbers})",
        f"Calculate the product of the numbers {numbers}",
        f"Finding PRODUCT for the list {numbers}",
        f"The multiplication of the numbers {numbers}",
        f"PRODUCT calculation: {numbers}",
        f"The product of the list {numbers}, what is it?",
        f"The product of the list {numbers}, what does it give?",
        f"Let's find the product of the numbers {numbers}",
        f"Find the PRODUCT for the list {numbers}",
        f"The product of the list {numbers}, result is",
        f"Calculating the product of the numbers {numbers}",
        f"The result of multiplying the numbers {numbers}",
        f"The product of the list {numbers}, what is its value?",
        f"Let's determine the product of the numbers {numbers}",
        f"The multiplication result of the numbers {numbers}",
        f"{numbers}, what is their product?",
        f"Finding the product of the numbers {numbers}",
        f"The product of the list {numbers}, what is its value?",
        f"Find the product of the numbers {numbers} and provide the result",
        f"PRODUCT({numbers}), what does it yield?",
        f"The product of the numbers {numbers}, ignoring order",
        f"The result of multiplying the elements in the list {numbers}",
        f"The multiplication of the numbers {numbers}, what is it?",
        f"Calculate the product of the list {numbers}, find the answer",
        f"The product of the numbers {numbers}, what does it give?",
        f"Let's find the result of multiplying the numbers {numbers}",
        f"{numbers}, their product, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_product_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
