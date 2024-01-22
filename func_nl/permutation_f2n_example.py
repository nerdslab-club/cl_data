import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_permutation_example(count: int):
    examples = []
    for _ in range(count):
        n = random.randint(2, 10)
        r = random.randint(1, n)
        examples.append(
            {
                "inputStr": f"##permutation({n}, {r})",
                "outputStr": __random_explanation_permutation(n, r),
            }
        )
    return examples


def __random_explanation_permutation(n: int, r: int) -> str:
    explanations = [
        f"The number of permutations of {r} items taken from a set of {n} items",
        f"permutation({n}, {r})",
        f"The result of calculating the permutations of {r} items from a set of {n} items",
        f"Calculation: permutation({n}, {r})",
        f"The count of possible arrangements of {r} items from a set of {n} items",
        f"The outcome of finding the number of permutations of {r} items from a set of {n} items",
        f"The total ways to arrange {r} items from a set of {n} items",
        f"The result of determining the permutations of {r} items chosen from {n} items",
        f"The computed result of calculating the permutations of {r} items from a set of {n} items",
        f"The number of possible orders of {r} items from a set of {n} items",
        f"The outcome of evaluating permutation({n}, {r})",
        f"The value obtained by calculating the permutations of {r} items from {n} items",
        f"The result of evaluating permutation({n}, {r})",
        f"The count of arrangements of {r} items selected from a set of {n} items",
        f"The computed number of permutations of {r} items from a set of {n} items",
        f"The total possible orders of {r} items from a set of {n} items",
        f"The calculated result of determining the permutations of {r} items chosen from {n} items",
        f"The number of ways to arrange {r} items out of {n} items",
        f"The result obtained from calculating the permutations of {r} items from a set of {n} items",
        f"The computed permutation count of {r} items from a set of {n} items",
        f"The number of distinct orders of {r} items from a set of {n} items",
        f"The calculated outcome of evaluating permutation({n}, {r})",
        f"The total permutations of {r} items from a set of {n} items",
        f"The computed permutation value of {r} items from a set of {n} items",
        f"The calculated count of permutations of {r} items chosen from {n} items",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_permutation_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
