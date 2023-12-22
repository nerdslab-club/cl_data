import random
import math  # Import the math module for arcsine function

from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_arcsine_example(count: int):
    examples = []
    for _ in range(count):
        value = RandomValueGenerator.generate_random_float(-1, 1, round_to=2)  # Random value in the range [-1, 1]
        angle = math.degrees(math.asin(value))  # Calculate corresponding angle in degrees
        examples.append(
            {
                "inputStr": __random_explanation_arcsine(value),
                "outputStr": f"##arcsine({value})",
            }
        )
    return examples


def __random_explanation_arcsine(value: float) -> str:
    angle_degrees = round(math.degrees(math.asin(value)), 2)  # Round the angle to two decimal places
    explanations = [
        f"Arcsine of {value}",
        f"Arcsin({value})",
        f"The arcsine value for {value}",
        f"Calculate arcsine for {value}",
        f"Arcsine function applied to {value}",
        f"Arcsin({value}), what is it?",
        f"The result of arcsin({value})",
        f"Find the arcsine of {value}",
        f"Arcsine value when input is {value}",
        f"Input: {value}, arcsine?",
        f"Arcsine of {value}, tell me",
        f"Arcsin({value}), the answer?",
        f"Calculate arcsin({value})",
        f"The arcsine for input {value}",
        f"What is arcsin({value})?",
        f"Arcsine of {value}, result?",
        f"Arcsin({value}), find the value",
        f"The arcsine value for input {value}",
        f"Arcsine of input {value}, what does it give?",
        f"Find arcsin({value})",
        f"Arcsine function for input {value}",
        f"Arcsine of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_arcsine_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
