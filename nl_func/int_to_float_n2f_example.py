import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_int_to_float_example(count: int):
    examples = []
    for _ in range(count):
        value = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(value),
            "outputStr": f"##int_to_float({value})",
        })
    return examples


def __random_explanation(value: int) -> str:
    explanations = [
        f"Convert the integer value {value} to a float",
        f"INT_TO_FLOAT({value})",
        f"Change the integer value {value} to a float",
        f"Find the float equivalent of the integer value {value}",
        f"The result of converting the integer value {value} to a float",
        f"Performing the integer to float conversion on the value {value}",
        f"The float equivalent of the integer value {value}",
        f"INT_TO_FLOAT calculation: {value}",
        f"The result after converting the integer value {value} to a float, what is it?",
        f"The float equivalent of {value}, what does it give?",
        f"Let's convert the integer value {value} to a float",
        f"The float equivalent of the integer value {value}, result is",
        f"Converting the integer value {value} to a float",
        f"The conversion result after converting the integer value {value} to a float",
        f"The float equivalent of the integer value {value}, what is its value?",
        f"Let's determine the float equivalent of the integer value {value}",
        f"The float equivalent of the integer value {value}",
        f"The float equivalent of the integer value {value}, what is the result?",
        f"The float equivalent of the integer value {value}, what does it give?",
        f"The float equivalent of the integer value {value} and provide the result",
        f"INT_TO_FLOAT({value}), what does it yield?",
        f"The float equivalent of the integer value {value}, ignoring order",
        f"The result after converting the integer value {value} to a float",
        f"The float equivalent of the integer value {value}, what is it?",
        f"Convert the integer value {value} to a float, find the answer",
        f"The float equivalent of the integer value {value}, what does it give?",
        f"Let's find the result after converting the integer value {value}",
        f"The float equivalent of the integer value {value}, what is the output?",
        f"The result after converting the integer value {value} to a float, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_int_to_float_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
