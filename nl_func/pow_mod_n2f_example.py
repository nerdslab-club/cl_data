import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_pow_mod_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        base = RandomValueGenerator.generate_random_integer(1, 100)
        exponent = RandomValueGenerator.generate_random_integer(0, 10)
        modulus = RandomValueGenerator.generate_random_integer(1, 50)
        examples.append({
            "inputStr": __random_explanation(base, exponent, modulus, (None if identifier is None else identifier+i)),
            "outputStr": f"##pow_mod({base}, {exponent}, {modulus})",
        })
    return examples


def __random_explanation(a: int, b: int, x: int, identifier: int | None) -> str:
    explanations = [
        f"The result of {a} raised to the power of {b} modulo {x}",
        f"POW_MOD({a}, {b}, {x})",
        f"Calculate {a} to the power of {b} modulo {x}",
        f"The modular exponentiation of {a} raised to {b} modulo {x}",
        f"The result of POW_MOD({a}, {b}, {x})",
        f"Raise {a} to the power of {b} and take modulo {x}",
        f"Finding POW_MOD for {a}, {b}, and {x}",
        f"{a} raised to {b} modulo {x}, what does it give?",
        f"The remainder when {a} to the power of {b} is divided by {x}",
        f"POW_MOD calculation: {a}, {b}, {x}",
        f"The result of raising {a} to the power of {b} and taking modulo {x}",
        f"POW_MOD({a}, {b}, {x}), what does it yield?",
        f"The modular exponentiation result for {a}, {b}, and {x}",
        f"Let's find {a} to the power of {b} modulo {x}",
        f"Find the POW_MOD for {a}, {b}, and {x}",
        f"The remainder when you raise {a} to the power of {b} and divide by {x}",
        f"POW_MOD({a}, {b}, {x}), result is",
        f"The value of {a} raised to {b} modulo {x}",
        f"The modular exponentiation of {a} to {b} modulo {x}",
        f"The remainder when {a} to the power of {b} is divided by {x}",
        f"Calculate POW_MOD({a}, {b}, {x}), find the answer",
        f"The result of raising {a} to {b} and taking modulo {x}",
        f"Let's calculate {a} to the power of {b} modulo {x}",
        f"The modular exponentiation of {a} raised to the power of {b} modulo {x}",
        f"POW_MOD({a}, {b}, {x}), what is its value?",
        f"Find the result of {a} raised to the power of {b} modulo {x}",
        f"The remainder when {a} to the power of {b} is divided by {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_pow_mod_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
