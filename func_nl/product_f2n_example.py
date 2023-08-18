import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_product_example(count: int):
    examples = []
    for _ in range(count):
        num_count = random.randint(2, 5)  # Generate 2 to 5 numbers
        numbers = [random.uniform(-100.0, 100.0) for _ in range(num_count)]
        examples.append(
            {
                "inputStr": f"##product({numbers})",
                "outputStr": __random_explanation_product(numbers),
            }
        )
    return examples


def __random_explanation_product(numbers: list) -> str:
    num_str = ", ".join(str(num) for num in numbers)
    explanations = [
        f"The product of the numbers {num_str}",
        f"product({num_str})",
        f"The result of multiplying the numbers {num_str}",
        f"Calculation: product({num_str})",
        f"The value obtained by multiplying the numbers {num_str}",
        f"The outcome of multiplying the elements in the list {num_str}",
        f"The total value of multiplying the numbers {num_str}",
        f"The result of the multiplication of {num_str}",
        f"The value achieved by multiplying the numbers {num_str}",
        f"The product value of the numbers {num_str}",
        f"The product obtained from the numbers {num_str}",
        f"The final value after multiplying the numbers {num_str}",
        f"The result of calculating the product of {num_str}",
        f"The outcome of the multiplication of the elements {num_str}",
        f"The value calculated by multiplying the numbers {num_str}",
        f"The value of the product of the numbers {num_str}",
        f"The total obtained from the multiplication of {num_str}",
        f"The computed result of the product of {num_str}",
        f"The product of the elements {num_str} is",
        f"The product value of the list {num_str}",
        f"The result of product({num_str}) is",
        f"The value from the multiplication of {num_str} is",
        f"The calculated result of multiplying the numbers {num_str}",
        f"The value achieved by product({num_str}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_product_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
