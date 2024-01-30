import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_relu_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##relu({x})",
                "outputStr": __random_explanation_relu(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_relu(f: float, identifier: int | None) -> str:
    explanations = [
        f"The Rectified Linear Unit (ReLU) activation of {f}",
        f"The result of applying ReLU to {f}",
        f"Calculation: relu({f})",
        f"The output of the ReLU activation function for the input {f}",
        f"The outcome of applying the ReLU activation to {f}",
        f"The value obtained by applying ReLU to {f}",
        f"The ReLU value of {f}",
        f"The outcome of the ReLU operation on {f}",
        f"The result of applying the Rectified Linear Unit function to {f}",
        f"The value after applying the ReLU activation to {f}",
        f"The computed result of the ReLU activation on {f}",
        f"The result of passing {f} through the ReLU activation",
        f"The output obtained by applying ReLU to the value {f}",
        f"The ReLU activation result of {f} is",
        f"The value after the ReLU operation on {f} is",
        f"The result of evaluating relu({f}) is",
        f"The outcome of applying the ReLU function to {f} is",
        f"The ReLU value of the input {f} is",
        f"The value obtained by passing {f} through the ReLU activation is",
        f"The outcome of applying ReLU({f}) is",
        f"The calculated result of applying ReLU to {f} is",
        f"The ReLU output of {f} is",
        f"The value of relu({f}) is",
        f"The ReLU result of applying to {f} is",
        f"The outcome of evaluating the ReLU activation on {f} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_relu_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
