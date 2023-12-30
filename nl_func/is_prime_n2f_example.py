import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_prime_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 50)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##is_prime({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Check if {x} is a prime number",
        f"IS_PRIME({x})",
        f"Determine if {x} is a prime number",
        f"The result of IS_PRIME({x})",
        f"Verify whether {x} is a prime number",
        f"Checking is prime for {x}",
        f"Decide if {x} is a prime number",
        f"Is prime calculation: {x}",
        f"Is {x} a prime number?",
        f"Is {x} a prime number? What does it give?",
        f"Let's check if {x} is a prime number",
        f"Check is prime for {x}",
        f"Is {x} a prime number? The result is",
        f"Determining if {x} is a prime number",
        f"Verifying whether {x} is a prime number",
        f"Is {x} a prime number? What is its value?",
        f"Let's decide if {x} is a prime number",
        f"Check if {x} is a prime number, find the answer",
        f"Is {x} a prime number? Result: ",
        f"Checking the primality of {x}",
        f"Is {x} a prime number? What is its status?",
        f"Check if {x} is a prime number and provide the result",
        f"is prime({x}), what does it yield?",
        f"Is {x} a prime number? Ignoring order",
        f"Is {x} a prime number? The decision is",
        f"Determine whether {x} is a prime number, find the answer",
        f"Check if {x} is a prime number. What is the result?",
        f"Is {x} a prime number? Let's find out",
        f"Is prime status for {x}, is it prime or not?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_prime_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
