import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_float_to_int_example(count: int):
    examples = []
    for _ in range(count):
        value = RandomValueGenerator.generate_random_float(1.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(value),
            "outputStr": f"##float_to_int({value})",
        })
    return examples


def __random_explanation(value: float) -> str:
    explanations = [
        f"Convert the float value {value} to an integer",
        f"FLOAT_TO_INT({value})",
        f"Change the float value {value} to an integer",
        f"Find the integer equivalent of the float value {value}",
        f"The result of converting the float value {value} to an integer",
        f"Performing the float to integer conversion on the value {value}",
        f"The integer equivalent of the float value {value}",
        f"FLOAT_TO_INT calculation: {value}",
        f"The result after converting the float value {value} to an integer, what is it?",
        f"The integer equivalent of {value}, what does it give?",
        f"Let's convert the float value {value} to an integer",
        f"The integer equivalent of the float value {value}, result is",
        f"Converting the float value {value} to an integer",
        f"The conversion result after converting the float value {value} to an integer",
        f"The integer equivalent of the float value {value}, what is its value?",
        f"Let's determine the integer equivalent of the float value {value}",
        f"The integer equivalent of the float value {value}",
        f"The integer equivalent of the float value {value}, what is the result?",
        f"The integer equivalent of the float value {value}, what does it give?",
        f"The integer equivalent of the float value {value} and provide the result",
        f"FLOAT_TO_INT({value}), what does it yield?",
        f"The integer equivalent of the float value {value}, ignoring order",
        f"The result after converting the float value {value} to an integer",
        f"The integer equivalent of the float value {value}, what is it?",
        f"Convert the float value {value} to an integer, find the answer",
        f"The integer equivalent of the float value {value}, what does it give?",
        f"Let's find the result after converting the float value {value}",
        f"The integer equivalent of the float value {value}, what is the output?",
        f"The result after converting the float value {value} to an integer, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_float_to_int_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
