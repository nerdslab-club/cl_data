import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_combination_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        n = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        r = RandomValueGenerator.generate_random_integer(1, n+1, seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##combination({n}, {r})",
                "outputStr": __random_explanation_combination(n, r, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_combination(n: int, r: int, identifier: int | None) -> str:
    explanations = [
        f"The number of combinations of {r} items taken from a set of {n} items",
        f"The result of calculating the combinations of {r} items from a set of {n} items",
        f"The count of possible selections of {r} items from a set of {n} items",
        f"The outcome of finding the number of combinations of {r} items from a set of {n} items",
        f"The total ways to choose {r} items from a set of {n} items",
        f"The result of determining the combinations of {r} items chosen from {n} items",
        f"The computed result of calculating the combinations of {r} items from a set of {n} items",
        f"The number of possible groups of {r} items from a set of {n} items",
        f"The value obtained by calculating the combinations of {r} items from {n} items",
        f"The result of evaluating combination({n}, {r})",
        f"The count of selections of {r} items picked from a set of {n} items",
        f"The computed number of combinations of {r} items from a set of {n} items",
        f"The total possible choices of {r} items from a set of {n} items",
        f"The calculated result of determining the combinations of {r} items chosen from {n} items",
        f"The number of ways to choose {r} items out of {n} items",
        f"The result obtained from calculating the combinations of {r} items from a set of {n} items",
        f"The computed combination count of {r} items from a set of {n} items",
        f"The number of distinct selections of {r} items from a set of {n} items",
        f"The calculated outcome of evaluating combination({n}, {r})",
        f"The total combinations of {r} items from a set of {n} items",
        f"The computed combination value of {r} items from a set of {n} items",
        f"The calculated count of combinations of {r} items chosen from {n} items",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_combination_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
