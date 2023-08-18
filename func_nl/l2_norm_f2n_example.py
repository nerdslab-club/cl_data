import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_l2_norm_example(count: int):
    examples = []
    for _ in range(count):
        vector = [random.uniform(-10.0, 10.0) for _ in range(3)]
        examples.append(
            {
                "inputStr": f"##l2_norm({vector})",
                "outputStr": __random_explanation_l2_norm(vector),
            }
        )
    return examples


def __random_explanation_l2_norm(vector) -> str:
    explanations = [
        f"The L2 norm (Euclidean norm) of the vector {vector}",
        f"l2_norm({vector})",
        f"The result of calculating the L2 norm of the vector {vector}",
        f"Calculation: l2_norm({vector})",
        f"The Euclidean norm value of the vector {vector}",
        f"The outcome of finding the L2 norm of the vector {vector}",
        f"The 2-norm value of the vector {vector}",
        f"The result of determining the L2 norm of the vector {vector}",
        f"The computed result of calculating the L2 norm of the vector {vector}",
        f"The L2 norm (Euclidean norm) of the given vector {vector}",
        f"The outcome of evaluating l2_norm({vector})",
        f"The value obtained by calculating the L2 norm of the vector {vector}",
        f"The result of evaluating l2_norm({vector})",
        f"The 2-norm value of the given vector {vector}",
        f"The computed L2 norm value of the vector {vector}",
        f"The Euclidean norm value of the given vector {vector}",
        f"The calculated result of determining the L2 norm of the vector {vector}",
        f"The L2 norm (Euclidean norm) of the vector {vector} is",
        f"The result derived from calculating the L2 norm of the vector {vector}",
        f"The computed 2-norm value of the vector {vector}",
        f"The calculated outcome of evaluating l2_norm({vector})",
        f"The computed Euclidean norm value of the vector {vector}",
        f"The calculated L2 norm value of the vector {vector}",
        f"The calculated 2-norm value of the vector {vector}",
        f"The outcome of finding the 2-norm value of the vector {vector}",
        f"The calculated Euclidean norm value of the vector {vector}",
        f"The calculated value of the L2 norm of the vector {vector}",
        f"The outcome of evaluating l2_norm({vector})",
        f"The outcome of calculating the L2 norm value of the vector {vector}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_l2_norm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
