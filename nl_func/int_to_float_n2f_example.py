import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_int_to_float_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(value, (None if identifier is None else identifier+i)),
            "outputStr": f"##int_to_float({value})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Convert the integer value {a} to a float",
        f"INT_TO_FLOAT({a})",
        f"Change the integer value {a} to a float",
        f"Find the float equivalent of the integer value {a}",
        f"The result of converting the integer value {a} to a float",
        f"Performing the integer to float conversion on the value {a}",
        f"The float equivalent of the integer value {a}",
        f"INT_TO_FLOAT calculation: {a}",
        f"The result after converting the integer value {a} to a float, what is it?",
        f"The float equivalent of {a}, what does it give?",
        f"Let's convert the integer value {a} to a float",
        f"The float equivalent of the integer value {a}, result is",
        f"Converting the integer value {a} to a float",
        f"The conversion result after converting the integer value {a} to a float",
        f"The float equivalent of the integer value {a}, what is its value?",
        f"Let's determine the float equivalent of the integer value {a}",
        f"The float equivalent of the integer value {a}",
        f"The float equivalent of the integer value {a}, what is the result?",
        f"The float equivalent of the integer value {a}, what does it give?",
        f"The float equivalent of the integer value {a} and provide the result",
        f"INT_TO_FLOAT({a}), what does it yield?",
        f"The float equivalent of the integer value {a}, ignoring order",
        f"The result after converting the integer value {a} to a float",
        f"The float equivalent of the integer value {a}, what is it?",
        f"Convert the integer value {a} to a float, find the answer",
        f"The float equivalent of the integer value {a}, what does it give?",
        f"Let's find the result after converting the integer value {a}",
        f"The float equivalent of the integer value {a}, what is the output?",
        f"The result after converting the integer value {a} to a float, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_int_to_float_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
