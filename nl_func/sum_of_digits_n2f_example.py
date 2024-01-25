import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_sum_of_digits_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        number = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(number, (None if identifier is None else identifier+i)),
            "outputStr": f"##sum_of_digits({number})",
        })
    return examples


def __random_explanation(number: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate the sum of digits for the number {number}",
        f"SUM_OF_DIGITS({number})",
        f"Determine the sum of digits for the number {number}",
        f"Find the sum of digits value for the number {number}",
        f"The result of calculating the sum of digits for {number}",
        f"Performing the sum of digits operation on the number {number}",
        f"The sum of digits for the number {number}",
        f"SUM_OF_DIGITS calculation: {number}",
        f"The result after calculating the sum of digits for {number}, what is it?",
        f"The sum of digits value of {number}, what does it give?",
        f"Let's calculate the sum of digits for the number {number}",
        f"The sum of digits value for the number {number}, result is",
        f"Calculating the sum of digits for the number {number}",
        f"The sum of digits result after calculating the sum of digits for {number}",
        f"The sum of digits for the number {number}, what is its value?",
        f"Let's determine the sum of digits for the number {number}",
        f"The sum of digits value for the number {number}",
        f"The sum of digits for the number {number}, what is the result?",
        f"The sum of digits for the number {number}, what does it give?",
        f"The sum of digits for the number {number} and provide the result",
        f"SUM_OF_DIGITS({number}), what does it yield?",
        f"The sum of digits value for the number {number}, ignoring order",
        f"The result after calculating the sum of digits for {number}",
        f"The sum of digits for the number {number}, what is it?",
        f"Calculate the sum of digits for the number {number}, find the answer",
        f"The sum of digits for the number {number}, what does it give?",
        f"Let's find the result after calculating the sum of digits for {number}",
        f"The sum of digits for the number {number}, what is the output?",
        f"The result after calculating the sum of digits for {number}, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_sum_of_digits_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
