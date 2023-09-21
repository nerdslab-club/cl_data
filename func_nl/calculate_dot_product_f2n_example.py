import random

from src.constants import TaskTypes
from src.utility import Utility
from src.random_value_generator import RandomValueGenerator


def create_f2n_calculate_dot_product_example(count: int):
    examples = []
    for _ in range(count):
        vector1 = RandomValueGenerator.generate_random_list(
            RandomValueGenerator.generate_random_integer(2, 10), -100, 10000
        )
        vector2 = RandomValueGenerator.generate_random_list(
            RandomValueGenerator.generate_random_integer(2, 10), -100, 10000
        )
        examples.append(
            {
                "inputStr": f"##calculate_dot_product({vector1}, {vector2})",
                "outputStr": __random_explanation_calculate_dot_product(
                    vector1, vector2
                ),
            }
        )
    return examples


def __random_explanation_calculate_dot_product(vector1_h, vector2_h) -> str:
    vector1 = ", ".join(str(num) for num in vector1_h)
    vector2 = ", ".join(str(num) for num in vector2_h)
    explanations = [
        f"Calculating the dot product of the vectors {vector1} and {vector2}",
        f"calculate_dot_product( {vector1_h}, {vector2_h} )",
        f"The result of calculating the dot product of the vectors {vector1} and {vector2}",
        f"Calculation: calculate_dot_product( {vector1_h}, {vector2_h} )",
        f"The scalar product of the vectors {vector1} and {vector2}",
        f"The outcome of evaluating calculate_dot_product( {vector1_h}, {vector2_h})",
        f"The result obtained by computing the dot product of the vectors {vector1} and {vector2}",
        f"The dot product value of the vectors {vector1} and {vector2}",
        f"The computed result of calculating the dot product of the vectors {vector1} and {vector2}",
        f"The dot product of the given vectors {vector1} and {vector2}",
        f"The outcome of determining the dot product of the vectors {vector1} and {vector2}",
        f"The numerical value of the dot product of the vectors {vector1} and {vector2}",
        f"The result of evaluating calculate_dot_product( {vector1_h}, {vector2_h} )",
        f"The dot product value of the vectors {vector1} and {vector2} is",
        f"The result derived from evaluating calculate_dot_product( {vector1_h}, {vector2_h} )",
        f"The scalar multiplication result of the vectors {vector1} and {vector2}",
        f"The value of the dot product of the vectors {vector1} and {vector2} is",
        f"The computed dot product of the vectors {vector1} and {vector2}",
        f"The calculated result of calculating the dot product of the vectors {vector1} and {vector2}",
        f"The dot product of the vectors {vector1} and {vector2} equals",
        f"The computed value of the dot product of the vectors {vector1} and {vector2}",
        f"The outcome of evaluating calculate_dot_product( {vector1_h}, {vector2_h})",
        f"The outcome of calculating the dot product value of the vectors {vector1} and {vector2}",
        f"The outcome of evaluating calculate_dot_product( {vector1_h}, {vector2_h} )",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_calculate_dot_product_example(2),
            TaskTypes.FUNC_TO_NL_TRANSLATION,
        )
    )
