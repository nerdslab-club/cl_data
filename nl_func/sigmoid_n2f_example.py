import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_sigmoid_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(x, (None if identifier is None else identifier+i)),
            "outputStr": f"##sigmoid({x})",
        })
    return examples


def __random_explanation(x: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the sigmoid function value for {x}",
        f"Determine the result of the sigmoid function for {x}",
        f"Find the sigmoid value for {x}",
        f"The result of applying the sigmoid function to {x}",
        f"Performing the sigmoid operation for {x}",
        f"The sigmoid value for {x}",
        f"SIGMOID calculation: {x}",
        f"The result after applying the sigmoid function to {x}, what is it",
        f"The sigmoid value for {x}, what does it give",
        f"Let's calculate the sigmoid value for {x}",
        f"The sigmoid value for {x}, result is",
        f"Calculating the sigmoid value for {x}",
        f"The sigmoid result after applying the sigmoid function to {x}",
        f"The sigmoid value for {x}, what is its value",
        f"Let's determine the sigmoid value for {x}",
        f"The sigmoid value for {x}, what is the result",
        f"The result after applying the sigmoid function to {x}",
        f"The sigmoid value for {x}, what is it",
        f"Calculate the sigmoid value for {x}, find the answer",
        f"The sigmoid value for {x}, what does it give",
        f"Let's find the result after applying the sigmoid function to {x}",
        f"The sigmoid value for {x}, what is the output",
        f"The result after applying the sigmoid function to {x}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_sigmoid_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
