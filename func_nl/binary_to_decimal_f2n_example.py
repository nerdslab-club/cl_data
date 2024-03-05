import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_binary_to_decimal_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        binary = "".join(
            random.choice(["0", "1"]) for _ in range(random.randint(1, 10))
        )
        examples.append(
            {
                "inputStr": f"##binary_to_decimal('{binary}')",
                "outputStr": __random_explanation_binary_to_decimal(binary, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_binary_to_decimal(binary: str, identifier: int | None) -> str:
    explanations = [
        f"The decimal equivalent of the binary number {binary}",
        f"The result of converting the binary number {binary} to decimal",
        f"Calculation: binary_to_decimal('{binary}')",
        f"The decimal representation obtained by converting the binary number '{binary}'",
        f"The outcome of converting the binary number '{binary}' to its decimal equivalent",
        f"The decimal value of the binary number '{binary}'",
        f"The result of transforming the binary number '{binary}' into decimal form",
        f"The computed result of converting the binary number '{binary}' to decimal",
        f"The decimal value obtained by converting the binary number '{binary}' to decimal",
        f"The decimal number obtained from the binary number '{binary}'",
        f"The outcome of evaluating binary_to_decimal('{binary}')",
        f"The decimal value calculated from the binary number '{binary}'",
        f"The result of evaluating binary_to_decimal('{binary}')",
        f"The decimal number represented by the binary number '{binary}'",
        f"The computed decimal value of the binary number '{binary}'",
        f"The decimal equivalent obtained by converting the binary number '{binary}'",
        f"The result derived from converting the binary number '{binary}' into decimal",
        f"The calculated outcome of evaluating binary_to_decimal('{binary}')",
        f"The decimal value corresponding to the binary number '{binary}'",
        f"The computed decimal result of binary_to_decimal('{binary}')",
        f"The calculated decimal representation of the binary number '{binary}'",
        f"The decimal value calculated by converting the binary number '{binary}'",
        f"The result obtained by converting the binary number '{binary}' to decimal",
        f"The computed decimal equivalent of the binary number '{binary}'",
        f"The calculated decimal value obtained from the binary number '{binary}'",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_binary_to_decimal_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
