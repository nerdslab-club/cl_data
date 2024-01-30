import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_relu_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##relu({num})",
        })
    return examples


def __random_explanation(x: float, identifier: int | None) -> str:
    explanations = [
        f"Apply the Rectified Linear Unit (ReLU) activation to {x}",
        f"Use ReLU activation on {x}",
        f"The result of applying ReLU activation to {x}",
        f"Calculate the ReLU activation for {x}",
        f"Applying ReLU to {x}",
        f"The value after ReLU activation: {x}",
        f"RELU activation calculation: {x}",
        f"The result of ReLU activation on {x}, what is it",
        f"The output after ReLU activation of {x}, what does it give",
        f"Let's apply ReLU activation to {x}",
        f"Apply the ReLU function to {x}",
        f"The value after ReLU activation: {x}, result is",
        f"Calculating the ReLU activation for {x}",
        f"The result after applying ReLU activation to {x}",
        f"The output of ReLU activation on {x}, what is its value",
        f"Let's determine the output after applying ReLU activation to {x}",
        f"The value after ReLU activation for {x}",
        f"Apply ReLU to {x}, what is the result",
        f"The output of ReLU activation on {x}, what does it give",
        f"Apply ReLU activation to {x} and provide the result",
        f"The output after ReLU activation of {x}, ignoring order",
        f"The result after applying ReLU activation to {x}",
        f"The value after ReLU activation of {x}, what is it",
        f"Calculate the ReLU activation for {x}, find the answer",
        f"The output after applying ReLU to {x}, what does it give",
        f"Let's find the result after applying ReLU activation to {x}",
        f"Apply ReLU to {x}, what is the output",
        f"The result after ReLU activation of {x}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_relu_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
