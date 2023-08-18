import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_sigmoid_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##sigmoid({x})",
                "outputStr": __random_explanation_sigmoid(x),
            }
        )
    return examples


def __random_explanation_sigmoid(x: float) -> str:
    explanations = [
        f"The sigmoid function value of the number {x}",
        f"sigmoid({x})",
        f"The result of evaluating the sigmoid function for the number {x}",
        f"Calculation: sigmoid({x})",
        f"The value of the sigmoid curve at the point {x}",
        f"The outcome of calculating the sigmoid function value for the number {x}",
        f"The logistic sigmoid value of the number {x}",
        f"The result of determining the sigmoid value for the number {x}",
        f"The computed result of evaluating the sigmoid function for the number {x}",
        f"The value of the sigmoid function at the input {x}",
        f"The outcome of evaluating sigmoid({x})",
        f"The value obtained by calculating the sigmoid function for the number {x}",
        f"The result of evaluating sigmoid({x})",
        f"The sigmoid curve's value at the input {x}",
        f"The computed sigmoid value of the number {x}",
        f"The sigmoid function value at the point {x}",
        f"The calculated result of determining the sigmoid value for the number {x}",
        f"The logistic sigmoid function value for the number {x}",
        f"The outcome of calculating the sigmoid value for the number {x}",
        f"The computed value of the sigmoid function at the point {x}",
        f"The sigmoid value for the number {x} is",
        f"The result derived from evaluating the sigmoid function for the number {x}",
        f"The computed sigmoid curve value of the number {x}",
        f"The sigmoid value obtained by evaluating sigmoid({x})",
        f"The calculated outcome of evaluating sigmoid({x})",
        f"The logistic sigmoid value at the input {x}",
        f"The calculated sigmoid curve value of the number {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_sigmoid_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
