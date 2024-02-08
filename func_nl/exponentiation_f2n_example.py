import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_exponentiation_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        base = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        exponent = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##exponentiation({base},{exponent})",
                "outputStr": __random_explanation_exp(
                    base,
                    exponent,
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_exp(base: float, exponent: float, identifier: int | None) -> str:
    explanations = [
        f"{base} raised to the power of {exponent}",
        f"The result of {base} raised to the power of {exponent}",
        f"Calculation: {base} ^ {exponent}",
        f"{base} raised to {exponent}",
        f"The value of {base} ^ ({exponent})",
        f"{base} to the power of {exponent} is",
        f"{base} raised to the exponent {exponent}",
        f"{base} ^ ({exponent}) equals",
        f"{base} raised to the {exponent} power",
        f"{base} to the {exponent} exponent",
        f"The exponentiation of {base} and {exponent}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_exponentiation_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
