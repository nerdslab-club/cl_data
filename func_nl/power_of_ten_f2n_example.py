import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_power_of_ten_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-10.0, 10.0)
        examples.append(
            {
                "inputStr": f"##power_of_ten({x})",
                "outputStr": __random_explanation_power_of_ten(x),
            }
        )
    return examples


def __random_explanation_power_of_ten(x: float) -> str:
    explanations = [
        f"10 raised to the power of {x}",
        f"power_of_ten({x})",
        f"The result of 10 raised to the power of {x}",
        f"Calculation: power_of_ten({x})",
        f"The value obtained by exponentiating 10 with the power of {x}",
        f"The outcome of evaluating 10 raised to the power of {x}",
        f"The result of 10 raised to the exponent {x}",
        f"The value of 10 to the power of {x}",
        f"The computed result of raising 10 to the power of {x}",
        f"The value obtained by raising 10 to the power of {x}",
        f"The outcome of finding 10 raised to the power of {x}",
        f"The computed value of power_of_ten({x}) is",
        f"The result of evaluating 10 raised to the power of {x} is",
        f"The value calculated by exponentiation 10 with the power of {x} is",
        f"The computed result of 10 raised to the power of {x} is",
        f"The calculated value of 10 to the power of {x} is",
        f"The outcome of finding 10 raised to the exponent {x} is",
        f"The value obtained by raising 10 to the exponent {x} is",
        f"The result of 10 raised to the power of {x} is",
        f"The outcome of evaluating power_of_ten({x}) is",
        f"The value of 10 to the power of {x} is",
        f"The computed outcome of evaluating 10 raised to the power of {x} is",
        f"The calculated result of raising 10 to the power of {x} is",
        f"The value of 10 raised to the power of {x} is",
        f"The result of exponentiation 10 with the power of {x} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_power_of_ten_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
