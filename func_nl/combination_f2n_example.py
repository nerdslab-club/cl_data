import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_combination_example(count: int):
    examples = []
    for _ in range(count):
        n = random.randint(2, 10)
        r = random.randint(1, n)
        examples.append(
            {
                "inputStr": f"##combination({n}, {r})",
                "outputStr": __random_explanation_combination(n, r),
            }
        )
    return examples


def __random_explanation_combination(n: int, r: int) -> str:
    explanations = [
        f"The number of combinations of {r} items taken from a set of {n} items",
        f"combination({n}, {r})",
        f"The result of calculating the combinations of {r} items from a set of {n} items",
        f"Calculation: combination({n}, {r})",
        f"The count of possible selections of {r} items from a set of {n} items",
        f"The outcome of finding the number of combinations of {r} items from a set of {n} items",
        f"The total ways to choose {r} items from a set of {n} items",
        f"The result of determining the combinations of {r} items chosen from {n} items",
        f"The computed result of calculating the combinations of {r} items from a set of {n} items",
        f"The number of possible groups of {r} items from a set of {n} items",
        f"The outcome of evaluating combination({n}, {r})",
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
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_combination_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
