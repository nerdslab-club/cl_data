import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_power_of_ten_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##power_of_ten({x})",
                "outputStr": __random_explanation_power_of_ten(x, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_power_of_ten(a: float, identifier: int | None) -> str:
    explanations = [
        f"10 raised to the power of {a}",
        f"The result of 10 raised to the power of {a}",
        f"Calculation: power_of_ten({a})",
        f"The value obtained by exponentiating 10 with the power of {a}",
        f"The outcome of evaluating 10 raised to the power of {a}",
        f"The result of 10 raised to the exponent {a}",
        f"The value of 10 to the power of {a}",
        f"The computed result of raising 10 to the power of {a}",
        f"The value obtained by raising 10 to the power of {a}",
        f"The outcome of finding 10 raised to the power of {a}",
        f"The computed value of power_of_ten({a}) is",
        f"The result of evaluating 10 raised to the power of {a} is",
        f"The value calculated by exponentiation 10 with the power of {a} is",
        f"The computed result of 10 raised to the power of {a} is",
        f"The calculated value of 10 to the power of {a} is",
        f"The outcome of finding 10 raised to the exponent {a} is",
        f"The value obtained by raising 10 to the exponent {a} is",
        f"The result of 10 raised to the power of {a} is",
        f"The outcome of evaluating power_of_ten({a}) is",
        f"The value of 10 to the power of {a} is",
        f"The computed outcome of evaluating 10 raised to the power of {a} is",
        f"The calculated result of raising 10 to the power of {a} is",
        f"The value of 10 raised to the power of {a} is",
        f"The result of exponentiation 10 with the power of {a} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_power_of_ten_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
