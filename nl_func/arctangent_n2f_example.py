import random
import math  # Import the math module for arctangent function

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_arctangent_example(count: int):
    examples = []
    for _ in range(count):
        value = RandomValueGenerator.generate_random_float(-1000, 1000, round_to=2)  # Random value in a wider range
        angle = math.degrees(math.atan(value))  # Calculate corresponding angle in degrees
        examples.append(
            {
                "inputStr": __random_explanation_arctangent(value),
                "outputStr": f"##arctangent({value})",
            }
        )
    return examples


def __random_explanation_arctangent(value: float) -> str:
    value = round(math.degrees(math.atan(value)), 2)  # Round the angle to two decimal places
    explanations = [
        f"Arctangent of {value}",
        f"Arctan({value})",
        f"The arctangent value for {value}",
        f"Calculate arctangent for {value}",
        f"Arctangent function applied to {value}",
        f"Arctan({value}), what is it?",
        f"The result of arctan({value})",
        f"Find the arctangent of {value}",
        f"Arctangent value when input is {value}",
        f"Input: {value}, arctangent?",
        f"Arctangent of {value}, tell me",
        f"Arctan({value}), the answer?",
        f"Calculate arctan({value})",
        f"The arctangent for input {value}",
        f"What is arctan({value})?",
        f"Arctangent of {value}, result?",
        f"Arctan({value}), find the value",
        f"The arctangent value for input {value}",
        f"Arctangent of input {value}, what does it give?",
        f"Find arctan({value})",
        f"Arctangent function for input {value}",
        f"Arctangent of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_arctangent_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
