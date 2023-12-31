import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_calculate_dot_product_example(count: int):
    examples = []
    for _ in range(count):
        vector1 = RandomValueGenerator.generate_random_list(3, -10, 10)
        vector2 = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(vector1, vector2),
            "outputStr": f"##calculate_dot_product({vector1}, {vector2})",
        })
    return examples


def __random_explanation(vector1: list, vector2: list) -> str:
    explanations = [
        f"Calculate the dot product of vectors {vector1} and {vector2}",
        f"CALCULATE_DOT_PRODUCT({vector1}, {vector2})",
        f"Determine the result of the dot product for vectors {vector1} and {vector2}",
        f"Find the dot product of vectors {vector1} and {vector2}",
        f"The result of calculating the dot product for vectors {vector1} and {vector2}",
        f"Performing the calculate_dot_product operation for vectors {vector1} and {vector2}",
        f"The dot product of vectors {vector1} and {vector2}",
        f"CALCULATE_DOT_PRODUCT operation: {vector1}, {vector2}",
        f"The result after calculating the dot product for vectors {vector1} and {vector2}, what is it?",
        f"Determine the dot product of vectors {vector1} and {vector2}",
        f"Let's calculate the dot product of vectors {vector1} and {vector2}",
        f"The dot product result of vectors {vector1} and {vector2}, is it true?",
        f"Calculating the dot product of vectors {vector1} and {vector2}",
        f"The dot product result after calculating dot product for vectors {vector1} and {vector2}",
        f"The dot product of vectors {vector1} and {vector2}, what is its value?",
        f"Let's determine the dot product of vectors {vector1} and {vector2}",
        f"The dot product of vectors {vector1} and {vector2}",
        f"The dot product of vectors {vector1} and {vector2}, what is the result?",
        f"The dot product of vectors {vector1} and {vector2}, what does it give?",
        f"The dot product of vectors {vector1} and {vector2} and provide the result",
        f"CALCULATE_DOT_PRODUCT({vector1}, {vector2}), what does it yield?",
        f"The dot product of vectors {vector1} and {vector2}, ignoring order",
        f"The result after calculating the dot product of vectors {vector1} and {vector2}",
        f"Calculate the dot product of vectors {vector1} and {vector2}, find the answer",
        f"The dot product of vectors {vector1} and {vector2}, what does it give?",
        f"Let's find the result after calculating the dot product of vectors {vector1} and {vector2}",
        f"The dot product result of vectors {vector1} and {vector2}, what is the output?",
        f"The result after calculating the dot product of vectors {vector1} and {vector2}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_calculate_dot_product_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
