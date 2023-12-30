import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_pow_mod_example(count: int):
    examples = []
    for _ in range(count):
        base = RandomValueGenerator.generate_random_integer(1, 100)
        exponent = RandomValueGenerator.generate_random_integer(0, 10)
        modulus = RandomValueGenerator.generate_random_integer(1, 50)
        examples.append({
            "inputStr": __random_explanation(base, exponent, modulus),
            "outputStr": f"##pow_mod({base}, {exponent}, {modulus})",
        })
    return examples


def __random_explanation(x: int, y: int, mod: int) -> str:
    explanations = [
        f"The result of {x} raised to the power of {y} modulo {mod}",
        f"POW_MOD({x}, {y}, {mod})",
        f"Calculate {x} to the power of {y} modulo {mod}",
        f"The modular exponentiation of {x} raised to {y} modulo {mod}",
        f"The result of POW_MOD({x}, {y}, {mod})",
        f"Raise {x} to the power of {y} and take modulo {mod}",
        f"Finding POW_MOD for {x}, {y}, and {mod}",
        f"{x} raised to {y} modulo {mod}, what does it give?",
        f"The remainder when {x} to the power of {y} is divided by {mod}",
        f"POW_MOD calculation: {x}, {y}, {mod}",
        f"The result of raising {x} to the power of {y} and taking modulo {mod}",
        f"POW_MOD({x}, {y}, {mod}), what does it yield?",
        f"The modular exponentiation result for {x}, {y}, and {mod}",
        f"Let's find {x} to the power of {y} modulo {mod}",
        f"Find the POW_MOD for {x}, {y}, and {mod}",
        f"The remainder when you raise {x} to the power of {y} and divide by {mod}",
        f"POW_MOD({x}, {y}, {mod}), result is",
        f"The value of {x} raised to {y} modulo {mod}",
        f"The modular exponentiation of {x} to {y} modulo {mod}",
        f"The remainder when {x} to the power of {y} is divided by {mod}",
        f"Calculate POW_MOD({x}, {y}, {mod}), find the answer",
        f"The result of raising {x} to {y} and taking modulo {mod}",
        f"Let's calculate {x} to the power of {y} modulo {mod}",
        f"The modular exponentiation of {x} raised to the power of {y} modulo {mod}",
        f"POW_MOD({x}, {y}, {mod}), what is its value?",
        f"Find the result of {x} raised to the power of {y} modulo {mod}",
        f"The remainder when {x} to the power of {y} is divided by {mod}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_pow_mod_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
