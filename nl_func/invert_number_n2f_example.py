import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_invert_number_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        number = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(number, (None if identifier is None else identifier+i)),
            "outputStr": f"##invert_number({number})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Invert the number {f1}",
        f"Reverse the digits of the number {f1}",
        f"Find the inverted value of the number {f1}",
        f"The result of inverting the number {f1}",
        f"Performing the invert operation on the number {f1}",
        f"The inverted value of the number {f1}",
        f"Let's invert the number {f1}",
        f"Inverting the number {f1}",
        f"The inverted result after inverting the number {f1}",
        f"Let's determine the inverted value of the number {f1}",
        f"The inverted value of the number {f1}",
        f"The result after inverting the number {f1}",
        f"Invert the number {f1}, find the answer",
        f"Let's find the result after inverting the number {f1}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_invert_number_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
