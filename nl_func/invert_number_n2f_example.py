import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_invert_number_example(count: int):
    examples = []
    for _ in range(count):
        number = RandomValueGenerator.generate_random_float(1.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(number),
            "outputStr": f"##invert_number({number})",
        })
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"Invert the number {f1}",
        f"INVERT_NUMBER({f1})",
        f"Reverse the digits of the number {f1}",
        f"Find the inverted value of the number {f1}",
        f"The result of inverting the number {f1}",
        f"Performing the invert operation on the number {f1}",
        f"The inverted value of the number {f1}",
        f"INVERT_NUMBER calculation: {f1}",
        f"The result after inverting the number {f1}, what is it?",
        f"The inverted value of {f1}, what does it give?",
        f"Let's invert the number {f1}",
        f"The inverted value of the number {f1}, result is",
        f"Inverting the number {f1}",
        f"The inverted result after inverting the number {f1}",
        f"The inverted value of the number {f1}, what is its value?",
        f"Let's determine the inverted value of the number {f1}",
        f"The inverted value of the number {f1}",
        f"The inverted value of the number {f1}, what is the result?",
        f"The inverted value of the number {f1}, what does it give?",
        f"The inverted value of the number {f1} and provide the result",
        f"INVERT_NUMBER({f1}), what does it yield?",
        f"The inverted value of the number {f1}, ignoring order",
        f"The result after inverting the number {f1}",
        f"The inverted value of the number {f1}, what is it?",
        f"Invert the number {f1}, find the answer",
        f"The inverted value of the number {f1}, what does it give?",
        f"Let's find the result after inverting the number {f1}",
        f"The inverted value of the number {f1}, what is the output?",
        f"The result after inverting the number {f1}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_invert_number_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
