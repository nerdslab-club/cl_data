import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_prime_factors_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 100)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##prime_factors({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"The prime factors of {x}",
        f"PRIME_FACTORS({x})",
        f"Find the prime factors of {x}",
        f"The result of PRIME_FACTORS({x})",
        f"Calculate the prime factors of {x}",
        f"Finding prime factors for {x}",
        f"The list of prime numbers that divide {x}",
        f"prime factors calculation: {x}",
        f"The prime factors of {x}, what are they?",
        f"The prime factors of {x}, what does it give?",
        f"Let's find the prime factors of {x}",
        f"Find the prime factors for {x}",
        f"The prime factors of {x}, result is",
        f"Calculating the prime factors of {x}",
        f"The list of prime numbers that divide {x}, what are they?",
        f"The prime factors of {x}, what is their value?",
        f"Let's determine the prime factors of {x}",
        f"The list of prime numbers that divide {x}, what are they exactly?",
        f"{x}, what are its prime factors?",
        f"Finding the prime factors of {x}",
        f"The prime factors of {x}, what is their value?",
        f"Find the prime factors of {x} and provide the result",
        f"prime factors({x}), what does it yield?",
        f"The prime factors of {x}, ignoring order",
        f"The list of prime numbers that divide {x}, what is it?",
        f"Calculate the prime factors of {x}, find the answer",
        f"The prime factors of {x}, what does it give?",
        f"Let's find the list of prime numbers that divide {x}",
        f"{x}, its prime factors, what are they?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_prime_factors_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
