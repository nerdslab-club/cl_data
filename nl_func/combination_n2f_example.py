import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_combination_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        n = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        r = RandomValueGenerator.generate_random_integer(1, n+1, seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(n, r, (None if identifier is None else identifier+i)),
            "outputStr": f"##combination({n}, {r})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate the combination of {a} objects taken {b} at a time",
        f"Determine the combination of {a} objects taken {b} at a time",
        f"Find the combination of {a} objects taken {b} at a time",
        f"The result of calculating the combination of {a} objects taken {b} at a time",
        f"Performing the combination operation for {a} objects taken {b} at a time",
        f"The combination of {a} objects taken {b} at a time",
        f"Let's calculate the combination of {a} objects taken {b} at a time",
        f"The combination of {a} objects taken {b} at a time, result is",
        f"Calculating the combination of {a} objects taken {b} at a time",
        f"Let's determine the combination of {a} objects taken {b} at a time",
        f"The result after calculating the combination of {a} objects taken {b} at a time",
        f"Calculate the combination of {a} objects taken {b} at a time, find the answer",
        f"The combination of {a} objects taken {b} at a time, what does it give",
        f"Let's find the result after calculating the combination of {a} objects taken {b} at a time",
        f"The combination of {a} objects taken {b} at a time, what is the output",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_combination_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
