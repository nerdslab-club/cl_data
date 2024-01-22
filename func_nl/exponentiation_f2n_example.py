import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_exponentiation_example(count: int):
    examples = []
    for _ in range(count):
        base = RandomValueGenerator.generate_random_float(1.0, 100.0)
        exponent = RandomValueGenerator.generate_random_float(1.0, 100.0)
        examples.append(
            {##exponentiation({x},{y})
                "inputStr": f"##exponentiation({base},{exponent})",
                "outputStr": __random_explanation_exp(
                    base,
                    exponent,
                ),
            }
        )
    return examples


def __random_explanation_exp(base: float, exponent: float) -> str:
    explanations = [
        f"{base} raised to the power of {exponent}",
        f"{base} ^ ({exponent})",
        f"The result of {base} raised to the power of {exponent}",
        f"Calculation: {base} ^ {exponent}",
        f"{base} raised to {exponent}",
        f"{base} raised to the {exponent}th power",
        f"The value of {base} ^ ({exponent})",
        f"{base} to the power of {exponent} is",
        f"{base} raised to the exponent {exponent}",
        f"{base} ^ ({exponent}) equals?",
        f"{base} raised to the {exponent} power",
        f"{base} to the {exponent} exponent",
        f"The exponentiation of {base} and {exponent}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_exponentiation_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
