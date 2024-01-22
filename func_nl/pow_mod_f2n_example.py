import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


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


def __random_explanation_pow_mod(n: int, r: int, mod: int) -> str:
    explanations = [
        f"The modular exponentiation of {n} raised to the power {r} modulo {mod}",
        f"pow_mod({n}, {r}, {mod})",
        f"The result of raising {n} to the power {r} and then taking modulo {mod}",
        f"Calculation: pow_mod({n}, {r}, {mod})",
        f"The value of ({n}^{r}) % {mod}",
        f"The value of {n} raised to the power {r} modulo {mod}",
        f"The modular result of {n}^{r} % {mod}",
        f"The remainder when {n}^{r} is divided by {mod}",
        f"The value of ({n}^{r}) mod {mod}",
        f"The result of raising {n} to the power {r} and then finding the remainder when divided by {mod}",
        f"The value of {n} raised to the power of {r} and then taken modulo {mod}",
        f"The outcome of ({n}^{r}) % {mod}",
        f"The outcome of raising {n} to the power {r} and then taking modulo {mod}",
        f"The value of {n} raised to the power {r} and then reduced modulo {mod}",
        f"The modular exponentiation result of {n} raised to the power {r} modulo {mod}",
        f"The outcome of raising {n} to the power {r} and then finding the modulo {mod}",
        f"The remainder when raising {n} to the power {r} divided by {mod}",
        f"The result of {n}^{r} modulo {mod}",
        f"The modular value of raising {n} to the power {r} with modulo {mod}",
        f"The result of {n}^{r} % {mod}",
        f"The modular result of {n} raised to the power of {r} with modulo {mod}",
        f"The outcome of ({n}^{r}) modulo {mod}",
        f"The value of pow_mod({n}, {r}, {mod}) is",
        f"The outcome of raising {n} to the power {r} and then reducing modulo {mod}",
        f"The result of raising {n} to the power {r} modulo {mod} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_pow_mod_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
