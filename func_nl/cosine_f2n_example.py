import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_cosine_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        angle = random.uniform(0.0, 360.0)
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
        f"cos({angle} °)",
        f"The result of taking the cosine of {angle} degrees",
        f"Calculation: cos({angle} °)",
        f"The cosine value of {angle} ° is",
        f"The value of cos({angle} °)",
        f"The trigonometric cosine function applied to {angle} °",
        f"The cosine of {angle} ° equals?",
        f"The ratio of the length of the adjacent side to the hypotenuse",
        f"The cosine of the angle {angle} °",
        f"The cosine function output for {angle} °",
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
