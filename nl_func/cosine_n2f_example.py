import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_cosine_example(count: int, identifier: int | None, seed: int,):
    examples = []
    for i in range(count):
        angle = RandomValueGenerator.generate_random_float(0, 360, round_to=1, seed=seed)  # Random angle in degrees
        examples.append(
            {
                "inputStr": __random_cosine_explanation(angle, (None if identifier is None else identifier+i)),
                "outputStr": f"##cosine({angle})",
            }
        )
    return examples


def __random_cosine_explanation(angle: float, identifier: int | None) -> str:
    explanations = [
        f"cosine value for {angle} degrees",
        f"cosine of {angle} degrees",
        f"cos of {angle} degrees",
        f"cosine({angle}) value",

        f"cosine function value at {angle} degrees",
        f"Calculate the cosine of {angle} degrees",
        f"Find the cosine of {angle} degrees",
        f"The cosine value when angle is {angle}",
        f"Cosine function for {angle}",
        f"The cosine of the angle {angle}",
        f"Cosine of the angle {angle}, calculate",
        f"The result of cos({angle}) calculation",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cosine_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
