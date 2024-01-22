import random
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_n2f_get_pi_example(count: int):
    examples = []
    for _ in range(count):
        examples.append({
            "inputStr": __random_explanation(),
            "outputStr": "##get_pi()",
        })
    return examples


def __random_explanation() -> str:
    explanations = [
        "Get the mathematical constant pi",
        "GET_PI()",
        "Retrieve the value of pi",
        "Obtain the constant pi",
        "The result of calling the get_pi function",
        "Performing the get_pi operation",
        "The value of the mathematical constant pi",
        "GET_PI operation",
        "The result after calling the get_pi function, what is it?",
        "What is the value of pi?",
        "Let's get the value of pi",
        "The constant pi, what is its value?",
        "Getting the value of pi",
        "The value of pi, result is",
        "Obtaining the constant pi, what does it give?",
        "Let's determine the value of pi",
        "The constant pi",
        "The value of pi, what is the result?",
        "The constant pi, what does it give?",
        "The constant pi and provide the result",
        "GET_PI(), what does it yield?",
        "The constant pi, ignoring order",
        "The result after calling the get_pi function",
        "Call get_pi, find the answer",
        "Calling get_pi, what does it give?",
        "Let's find the result after calling the get_pi function",
        "The constant pi, what is the output?",
        "The result after calling the get_pi function, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_get_pi_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
