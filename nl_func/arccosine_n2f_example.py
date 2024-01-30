import random
import math

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_arccosine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float(-1, 1, round_to=1)  # Random value in the range [-1, 1]
        examples.append(
            {
                "inputStr": __random_explanation_arccosine(value, (None if identifier is None else identifier+i)),
                "outputStr": f"##arccosine({value})",
            }
        )
    return examples


def __random_explanation_arccosine(value: float, identifier: int | None) -> str:
    value = round(math.degrees(math.acos(value)), 2)  # Round the angle to two decimal places
    explanations = [
        f"Arccosine of {value}",
        f"Arccos({value})",
        f"The arccosine value for {value}",
        f"Calculate arccosine for {value}",
        f"Arccosine function applied to {value}",
        f"Arccos({value}), what is it",
        f"The result of arccos({value})",
        f"Find the arccosine of {value}",
        f"Arccosine value when input is {value}",
        f"Input: {value}, arccosine",
        f"Arccosine of {value}, tell me",
        f"Arccos({value}), the answer",
        f"Calculate arccos({value})",
        f"The arccosine for input {value}",
        f"What is arccos({value})",
        f"Arccosine of {value}, result",
        f"Arccos({value}), find the value",
        f"The arccosine value for input {value}",
        f"Arccosine of input {value}, what does it give",
        f"Find arccos({value})",
        f"Arccosine function for input {value}",
        f"Arccosine of {value}, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_arccosine_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
