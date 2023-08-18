import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_pow_mod_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(1, 100)
        y = random.randint(1, 20)
        mod = random.randint(2, 100)
        examples.append(
            {
                "inputStr": f"##pow_mod({x}, {y}, {mod})",
                "outputStr": __random_explanation_pow_mod(x, y, mod),
            }
        )
    return examples


def __random_explanation_pow_mod(x: int, y: int, mod: int) -> str:
    explanations = [
        f"The modular exponentiation of {x} raised to the power {y} modulo {mod}",
        f"pow_mod({x}, {y}, {mod})",
        f"The result of raising {x} to the power {y} and then taking modulo {mod}",
        f"Calculation: pow_mod({x}, {y}, {mod})",
        f"The value of ({x}^{y}) % {mod}",
        f"The value of {x} raised to the power {y} modulo {mod}",
        f"The modular result of {x}^{y} % {mod}",
        f"The remainder when {x}^{y} is divided by {mod}",
        f"The value of ({x}^{y}) mod {mod}",
        f"The result of raising {x} to the power {y} and then finding the remainder when divided by {mod}",
        f"The value of {x} raised to the power of {y} and then taken modulo {mod}",
        f"The outcome of ({x}^{y}) % {mod}",
        f"The outcome of raising {x} to the power {y} and then taking modulo {mod}",
        f"The value of {x} raised to the power {y} and then reduced modulo {mod}",
        f"The modular exponentiation result of {x} raised to the power {y} modulo {mod}",
        f"The outcome of raising {x} to the power {y} and then finding the modulo {mod}",
        f"The remainder when raising {x} to the power {y} divided by {mod}",
        f"The result of {x}^{y} modulo {mod}",
        f"The modular value of raising {x} to the power {y} with modulo {mod}",
        f"The result of {x}^{y} % {mod}",
        f"The modular result of {x} raised to the power of {y} with modulo {mod}",
        f"The outcome of ({x}^{y}) modulo {mod}",
        f"The value of pow_mod({x}, {y}, {mod}) is",
        f"The outcome of raising {x} to the power {y} and then reducing modulo {mod}",
        f"The result of raising {x} to the power {y} modulo {mod} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_pow_mod_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
