import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_combination_example(count: int):
    examples = []
    for _ in range(count):
        n = RandomValueGenerator.generate_random_integer(2, 10)
        r = RandomValueGenerator.generate_random_integer(1, n)
        examples.append({
            "inputStr": __random_explanation(n, r),
            "outputStr": f"##combination({n}, {r})",
        })
    return examples


def __random_explanation(n: int, r: int) -> str:
    explanations = [
        f"Calculate the combination of {n} objects taken {r} at a time",
        f"COMBINATION({n}, {r})",
        f"Determine the combination of {n} objects taken {r} at a time",
        f"Find the combination of {n} objects taken {r} at a time",
        f"The result of calculating the combination of {n} objects taken {r} at a time",
        f"Performing the combination operation for {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time",
        f"COMBINATION calculation: ({n}, {r})",
        f"The result after calculating the combination of {n} objects taken {r} at a time, what is it?",
        f"The combination of {n} objects taken {r} at a time, what does it give?",
        f"Let's calculate the combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time, result is",
        f"Calculating the combination of {n} objects taken {r} at a time",
        f"The combination result after calculating the combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time, what is its value?",
        f"Let's determine the combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time, what is the result?",
        f"The combination of {n} objects taken {r} at a time, what does it give?",
        f"The combination of {n} objects taken {r} at a time and provide the result",
        f"COMBINATION({n}, {r}), what does it yield?",
        f"The combination of {n} objects taken {r} at a time, ignoring order",
        f"The result after calculating the combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time, what is it?",
        f"Calculate the combination of {n} objects taken {r} at a time, find the answer",
        f"The combination of {n} objects taken {r} at a time, what does it give?",
        f"Let's find the result after calculating the combination of {n} objects taken {r} at a time",
        f"The combination of {n} objects taken {r} at a time, what is the output?",
        f"The result after calculating the combination of {n} objects taken {r} at a time, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_combination_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
