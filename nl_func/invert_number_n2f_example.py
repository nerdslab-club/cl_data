import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_invert_number_example(count: int):
    examples = []
    for _ in range(count):
        number = RandomValueGenerator.generate_random_float(1.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(number),
            "outputStr": f"##invert_number({number})",
        })
    return examples


def __random_explanation(number: float) -> str:
    explanations = [
        f"Invert the number {number}",
        f"INVERT_NUMBER({number})",
        f"Reverse the digits of the number {number}",
        f"Find the inverted value of the number {number}",
        f"The result of inverting the number {number}",
        f"Performing the invert operation on the number {number}",
        f"The inverted value of the number {number}",
        f"INVERT_NUMBER calculation: {number}",
        f"The result after inverting the number {number}, what is it?",
        f"The inverted value of {number}, what does it give?",
        f"Let's invert the number {number}",
        f"The inverted value of the number {number}, result is",
        f"Inverting the number {number}",
        f"The inverted result after inverting the number {number}",
        f"The inverted value of the number {number}, what is its value?",
        f"Let's determine the inverted value of the number {number}",
        f"The inverted value of the number {number}",
        f"The inverted value of the number {number}, what is the result?",
        f"The inverted value of the number {number}, what does it give?",
        f"The inverted value of the number {number} and provide the result",
        f"INVERT_NUMBER({number}), what does it yield?",
        f"The inverted value of the number {number}, ignoring order",
        f"The result after inverting the number {number}",
        f"The inverted value of the number {number}, what is it?",
        f"Invert the number {number}, find the answer",
        f"The inverted value of the number {number}, what does it give?",
        f"Let's find the result after inverting the number {number}",
        f"The inverted value of the number {number}, what is the output?",
        f"The result after inverting the number {number}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_invert_number_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
