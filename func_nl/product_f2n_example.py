import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_product_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num_count = random.randint(2, 5)  # Generate 2 to 5 numbers
        numbers = [random.uniform(-100.0, 100.0) for _ in range(num_count)]
        examples.append(
            {
                "inputStr": f"##product({numbers})",
                "outputStr": __random_explanation_product(numbers, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_product(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"The product of the numbers {lst_str}",
        f"product({vector})",
        f"The result of multiplying the numbers {lst_str}",
        f"Calculation: product({vector})",
        f"The value obtained by multiplying the numbers {lst_str}",
        f"The outcome of multiplying the elements in the list {lst_str}",
        f"The total value of multiplying the numbers {lst_str}",
        f"The result of the multiplication of {lst_str}",
        f"The value achieved by multiplying the numbers {lst_str}",
        f"The product value of the numbers {lst_str}",
        f"The product obtained from the numbers {lst_str}",
        f"The final value after multiplying the numbers {lst_str}",
        f"The result of calculating the product of {lst_str}",
        f"The outcome of the multiplication of the elements {lst_str}",
        f"The value calculated by multiplying the numbers {lst_str}",
        f"The value of the product of the numbers {lst_str}",
        f"The total obtained from the multiplication of {lst_str}",
        f"The computed result of the product of {lst_str}",
        f"The product of the elements {lst_str} is",
        f"The product value of the list {lst_str}",
        f"The result of product({vector}) is",
        f"The value from the multiplication of {lst_str} is",
        f"The calculated result of multiplying the numbers {lst_str}",
        f"The value achieved by product({vector}) is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_product_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
