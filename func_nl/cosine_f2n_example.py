import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_cosine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        angle = RandomValueGenerator.generate_random_float(0.0, 360.0, round_to=1, seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##cosine({angle})",
                "outputStr": __random_explanation_cosine(angle, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_cosine(angle: float, identifier: int | None) -> str:
    explanations = [
        f"The cosine of {angle} degrees",
        f"The result of taking the cosine of {angle} degrees",
        f"Calculation: cos({angle} degree)",
        f"The cosine value of {angle} degree is",
        f"The value of cos({angle} degree)",
        f"The trigonometric cosine function applied to {angle} degree",
        f"The cosine of the angle {angle} degree",
        f"The cosine function output for {angle} degree",
        f"The cosine of {angle} degrees is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_cosine_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
