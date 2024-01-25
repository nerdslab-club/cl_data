import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility

def create_f2n_sum_of_digits_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = random.randint(1, 10000)
        examples.append(
            {
                "inputStr": f"##sum_of_digits({num})",
                "outputStr": __random_explanation_sum_of_digits(num, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_sum_of_digits(a: int, identifier: int | None) -> str:
    explanations = [
        f"The sum of the digits of the number {a}",
        f"sum_of_digits({a})",
        f"The result of adding up the digits of the number {a}",
        f"Calculation: sum_of_digits({a})",
        f"The sum obtained by adding the digits of the number {a}",
        f"The outcome of computing the sum of the digits of the number {a}",
        f"The total of the digits in the number {a}",
        f"The result of summing up the individual digits of the number {a}",
        f"The computed result of calculating the sum of the digits of the number {a}",
        f"The sum of the individual digits in the number {a}",
        f"The outcome of evaluating sum_of_digits({a})",
        f"The value obtained by adding the digits of the number {a}",
        f"The result of evaluating sum_of_digits({a})",
        f"The total obtained by adding the digits of the number {a}",
        f"The computed sum of the digits of the number {a}",
        f"The sum obtained from adding the digits of the number {a}",
        f"The calculated result of summing the digits of the number {a}",
        f"The sum calculated by adding the digits of the number {a}",
        f"The result derived from summing the digits of the number {a}",
        f"The calculated outcome of evaluating sum_of_digits({a})",
        f"The total value of the digits in the number {a}",
        f"The computed sum result of sum_of_digits({a})",
        f"The calculated total obtained by adding the digits of the number {a}",
        f"The sum of the digits of the number {a} is",
        f"The result of summing the individual digits in the number {a}",
        f"The computed total of the digits in the number {a}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sum_of_digits_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
