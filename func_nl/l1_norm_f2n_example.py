import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_l1_norm_example(count: int):
    examples = []
    for _ in range(count):
        vector = [random.uniform(-10.0, 10.0) for _ in range(3)]
        examples.append(
            {
                "inputStr": f"##l1_norm({vector})",
                "outputStr": __random_explanation_l1_norm(vector),
            }
        )
    return examples


def __random_explanation_l1_norm(vector) -> str:
    explanations = [
        f"The L1 norm (Manhattan norm) of the vector {vector}",
        f"l1_norm({vector})",
        f"The result of calculating the L1 norm of the vector {vector}",
        f"Calculation: l1_norm({vector})",
        f"The Manhattan norm value of the vector {vector}",
        f"The outcome of finding the L1 norm of the vector {vector}",
        f"The Taxicab norm value of the vector {vector}",
        f"The result of determining the L1 norm of the vector {vector}",
        f"The computed result of calculating the L1 norm of the vector {vector}",
        f"The L1 norm (Manhattan norm) of the given vector {vector}",
        f"The outcome of evaluating l1_norm({vector})",
        f"The value obtained by calculating the L1 norm of the vector {vector}",
        f"The result of evaluating l1_norm({vector})",
        f"The Taxicab norm value of the given vector {vector}",
        f"The computed L1 norm value of the vector {vector}",
        f"The Manhattan norm value of the given vector {vector}",
        f"The calculated result of determining the L1 norm of the vector {vector}",
        f"The L1 norm (Manhattan norm) of the vector {vector} is",
        f"The result derived from calculating the L1 norm of the vector {vector}",
        f"The computed Taxicab norm value of the vector {vector}",
        f"The calculated outcome of evaluating l1_norm({vector})",
        f"The computed Manhattan norm value of the vector {vector}",
        f"The calculated L1 norm value of the vector {vector}",
        f"The calculated Taxicab norm value of the vector {vector}",
        f"The outcome of finding the Taxicab norm value of the vector {vector}",
        f"The calculated Manhattan norm value of the vector {vector}",
        f"The calculated value of the L1 norm of the vector {vector}",
        f"The outcome of evaluating l1_norm({vector})",
        f"The outcome of calculating the L1 norm value of the vector {vector}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_l1_norm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
