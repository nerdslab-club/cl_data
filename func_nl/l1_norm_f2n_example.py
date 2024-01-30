import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_l1_norm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        vector = RandomValueGenerator.generate_random_list()
        examples.append(
            {
                "inputStr": f"##l1_norm({vector})",
                "outputStr": __random_explanation_l1_norm(vector, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_l1_norm(vector, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)

    explanations = [
        f"The L1 norm (Manhattan norm) of the vector {lst_str}",
        f"The result of calculating the L1 norm of the vector {lst_str}",
        f"Calculation: l1_norm({vector})",
        f"The Manhattan norm value of the vector {lst_str}",
        f"The outcome of finding the L1 norm of the vector {lst_str}",
        f"The Taxicab norm value of the vector {lst_str}",
        f"The result of determining the L1 norm of the vector {lst_str}",
        f"The computed result of calculating the L1 norm of the vector {lst_str}",
        f"The L1 norm (Manhattan norm) of the given vector {lst_str}",
        f"The outcome of evaluating l1_norm({vector})",
        f"The value obtained by calculating the L1 norm of the vector {lst_str}",
        f"The result of evaluating l1_norm({vector})",
        f"The Taxicab norm value of the given vector {lst_str}",
        f"The computed L1 norm value of the vector {lst_str}",
        f"The Manhattan norm value of the given vector {lst_str}",
        f"The calculated result of determining the L1 norm of the vector {lst_str}",
        f"The L1 norm (Manhattan norm) of the vector {lst_str} is",
        f"The result derived from calculating the L1 norm of the vector {lst_str}",
        f"The computed Taxicab norm value of the vector {lst_str}",
        f"The calculated outcome of evaluating l1_norm({vector})",
        f"The computed Manhattan norm value of the vector {lst_str}",
        f"The calculated L1 norm value of the vector {lst_str}",
        f"The calculated Taxicab norm value of the vector {lst_str}",
        f"The outcome of finding the Taxicab norm value of the vector {lst_str}",
        f"The calculated Manhattan norm value of the vector {lst_str}",
        f"The calculated value of the L1 norm of the vector {lst_str}",
        f"The outcome of evaluating l1_norm({vector})",
        f"The outcome of calculating the L1 norm value of the vector {lst_str}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_l1_norm_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
