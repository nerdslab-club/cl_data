import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_is_prime_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 50)
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##is_prime({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Check if {a} is a prime number",
        f"IS_PRIME({a})",
        f"Determine if {a} is a prime number",
        f"The result of IS_PRIME({a})",
        f"Verify whether {a} is a prime number",
        f"Checking is prime for {a}",
        f"Decide if {a} is a prime number",
        f"Is prime calculation: {a}",
        f"Is {a} a prime number?",
        f"Is {a} a prime number? What does it give?",
        f"Let's check if {a} is a prime number",
        f"Check is prime for {a}",
        f"Is {a} a prime number? The result is",
        f"Determining if {a} is a prime number",
        f"Verifying whether {a} is a prime number",
        f"Is {a} a prime number? What is its value?",
        f"Let's decide if {a} is a prime number",
        f"Check if {a} is a prime number, find the answer",
        f"Is {a} a prime number? Result: ",
        f"Checking the primality of {a}",
        f"Is {a} a prime number? What is its status?",
        f"Check if {a} is a prime number and provide the result",
        f"is prime({a}), what does it yield?",
        f"Is {a} a prime number? Ignoring order",
        f"Is {a} a prime number? The decision is",
        f"Determine whether {a} is a prime number, find the answer",
        f"Check if {a} is a prime number. What is the result?",
        f"Is {a} a prime number? Let's find out",
        f"Is prime status for {a}, is it prime or not?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_prime_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
