import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_cosine_example(count: int):
    examples = []
    for _ in range(count):
        angle = RandomValueGenerator.generate_random_float(0, 360, round_to=2)  # Random angle in degrees
        examples.append(
            {
                "inputStr": __random_cosine_explanation(angle),
                "outputStr": f"##cosine({angle})",
            }
        )
    return examples


def __random_cosine_explanation(angle: float) -> str:
    explanations = [
        f"Calculate the cosine of {angle} degrees",
        f"Cosine value for {angle} degrees",
        f"The result of cosine({angle})",
        f"Cos({angle}), what is it?",
        f"Find the cosine of {angle} degrees",
        f"Compute cos({angle})",
        f"Cosine of {angle} degrees",
        f"The cosine value when angle is {angle}",
        f"Value of cos({angle})",
        f"Cosine function for {angle}",
        f"The cos of {angle} degrees",
        f"Evaluate cos({angle})",
        f"Cos({angle}), find the result",
        f"The cosine of the angle {angle}",
        f"Cosine({angle}), what does it give?",
        f"Cosine of the angle {angle}, calculate",
        f"Find cos({angle})",
        f"Cos({angle}) value",
        f"The result of cos({angle}) calculation",
        f"Cosine function value at {angle} degrees",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cosine_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
