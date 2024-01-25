import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_sigmoid_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##sigmoid({x})",
                "outputStr": __random_explanation_sigmoid(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_sigmoid(f: float, identifier: int | None) -> str:
    explanations = [
        f"The sigmoid function value of the number {f}",
        f"sigmoid({f})",
        f"The result of evaluating the sigmoid function for the number {f}",
        f"Calculation: sigmoid({f})",
        f"The value of the sigmoid curve at the point {f}",
        f"The outcome of calculating the sigmoid function value for the number {f}",
        f"The logistic sigmoid value of the number {f}",
        f"The result of determining the sigmoid value for the number {f}",
        f"The computed result of evaluating the sigmoid function for the number {f}",
        f"The value of the sigmoid function at the input {f}",
        f"The outcome of evaluating sigmoid({f})",
        f"The value obtained by calculating the sigmoid function for the number {f}",
        f"The result of evaluating sigmoid({f})",
        f"The sigmoid curve's value at the input {f}",
        f"The computed sigmoid value of the number {f}",
        f"The sigmoid function value at the point {f}",
        f"The calculated result of determining the sigmoid value for the number {f}",
        f"The logistic sigmoid function value for the number {f}",
        f"The outcome of calculating the sigmoid value for the number {f}",
        f"The computed value of the sigmoid function at the point {f}",
        f"The sigmoid value for the number {f} is",
        f"The result derived from evaluating the sigmoid function for the number {f}",
        f"The computed sigmoid curve value of the number {f}",
        f"The sigmoid value obtained by evaluating sigmoid({f})",
        f"The calculated outcome of evaluating sigmoid({f})",
        f"The logistic sigmoid value at the input {f}",
        f"The calculated sigmoid curve value of the number {f}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sigmoid_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
