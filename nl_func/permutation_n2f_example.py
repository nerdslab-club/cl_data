import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_permutation_example(count: int):
    examples = []
    for _ in range(count):
        n = RandomValueGenerator.generate_random_integer(2, 10)
        r = RandomValueGenerator.generate_random_integer(1, n)
        examples.append({
            "inputStr": __random_explanation(n, r),
            "outputStr": f"##permutation({n}, {r})",
        })
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Calculate the permutation of {x} objects taken {y} at a time",
        f"PERMUTATION({x}, {y})",
        f"Determine the permutation of {x} objects taken {y} at a time",
        f"Find the permutation of {x} objects taken {y} at a time",
        f"The result of calculating the permutation of {x} objects taken {y} at a time",
        f"Performing the permutation operation for {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time",
        f"PERMUTATION calculation: ({x}, {y})",
        f"The result after calculating the permutation of {x} objects taken {y} at a time, what is it?",
        f"The permutation of {x} objects taken {y} at a time, what does it give?",
        f"Let's calculate the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, result is",
        f"Calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is its value?",
        f"Let's determine the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is the result?",
        f"The permutation of {x} objects taken {y} at a time, what does it give?",
        f"The permutation of {x} objects taken {y} at a time and provide the result",
        f"PERMUTATION({x}, {y}), what does it yield?",
        f"The permutation of {x} objects taken {y} at a time, ignoring order",
        f"The result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is it?",
        f"Calculate the permutation of {x} objects taken {y} at a time, find the answer",
        f"The permutation of {x} objects taken {y} at a time, what does it give?",
        f"Let's find the result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is the output?",
        f"The result after calculating the permutation of {x} objects taken {y} at a time, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_permutation_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
