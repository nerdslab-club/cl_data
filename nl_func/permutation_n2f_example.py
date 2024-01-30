import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_permutation_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        n = RandomValueGenerator.generate_random_integer()
        r = RandomValueGenerator.generate_random_integer(1, n)
        examples.append({
            "inputStr": __random_explanation(n, r, (None if identifier is None else identifier+i)),
            "outputStr": f"##permutation({n}, {r})",
        })
    return examples


def __random_explanation(x: int, y: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate the permutation of {x} objects taken {y} at a time",
        f"Determine the permutation of {x} objects taken {y} at a time",
        f"Find the permutation of {x} objects taken {y} at a time",
        f"The result of calculating the permutation of {x} objects taken {y} at a time",
        f"Performing the permutation operation for {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time",
        f"The result after calculating the permutation of {x} objects taken {y} at a time, what is it",
        f"The permutation of {x} objects taken {y} at a time, what does it give",
        f"Let's calculate the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, result is",
        f"Calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is its value",
        f"Let's determine the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is the result",
        f"The result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is it",
        f"Calculate the permutation of {x} objects taken {y} at a time, find the answer",
        f"The permutation of {x} objects taken {y} at a time, what does it give",
        f"Let's find the result after calculating the permutation of {x} objects taken {y} at a time",
        f"The permutation of {x} objects taken {y} at a time, what is the output",
        f"The result after calculating the permutation of {x} objects taken {y} at a time, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_permutation_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
