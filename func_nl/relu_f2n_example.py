import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_relu_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##relu({x})",
                "outputStr": __random_explanation_relu(x),
            }
        )
    return examples


def __random_explanation_relu(x: float) -> str:
    explanations = [
        f"The Rectified Linear Unit (ReLU) activation of {x}",
        f"relu({x})",
        f"The result of applying ReLU to {x}",
        f"Calculation: relu({x})",
        f"The output of the ReLU activation function for the input {x}",
        f"The outcome of applying the ReLU activation to {x}",
        f"The value obtained by applying ReLU to {x}",
        f"The ReLU value of {x}",
        f"The outcome of the ReLU operation on {x}",
        f"The result of applying the Rectified Linear Unit function to {x}",
        f"The value after applying the ReLU activation to {x}",
        f"The computed result of the ReLU activation on {x}",
        f"The result of passing {x} through the ReLU activation",
        f"The output obtained by applying ReLU to the value {x}",
        f"The ReLU activation result of {x} is",
        f"The value after the ReLU operation on {x} is",
        f"The result of evaluating relu({x}) is",
        f"The outcome of applying the ReLU function to {x} is",
        f"The ReLU value of the input {x} is",
        f"The value obtained by passing {x} through the ReLU activation is",
        f"The outcome of applying ReLU({x}) is",
        f"The calculated result of applying ReLU to {x} is",
        f"The ReLU output of {x} is",
        f"The value of relu({x}) is",
        f"The ReLU result of applying to {x} is",
        f"The outcome of evaluating the ReLU activation on {x} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_relu_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
