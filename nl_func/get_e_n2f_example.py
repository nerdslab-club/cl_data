import random
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_n2f_get_e_example(count: int):
    examples = []
    for _ in range(count):
        examples.append({
            "inputStr": __random_explanation(),
            "outputStr": "##get_e()",
        })
    return examples


def __random_explanation() -> str:
    explanations = [
        "Get the mathematical constant e",
        "GET_E()",
        "Retrieve the value of e",
        "Obtain the constant e",
        "The result of calling the get_e function",
        "Performing the get_e operation",
        "The value of the mathematical constant e",
        "GET_E operation",
        "The result after calling the get_e function, what is it?",
        "What is the value of e?",
        "Let's get the value of e",
        "The constant e, what is its value?",
        "Getting the value of e",
        "The value of e, result is",
        "Obtaining the constant e, what does it give?",
        "Let's determine the value of e",
        "The constant e",
        "The value of e, what is the result?",
        "The constant e, what does it give?",
        "The constant e and provide the result",
        "GET_E(), what does it yield?",
        "The constant e, ignoring order",
        "The result after calling the get_e function",
        "Call get_e, find the answer",
        "Calling get_e, what does it give?",
        "Let's find the result after calling the get_e function",
        "The constant e, what is the output?",
        "The result after calling the get_e function, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_get_e_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
