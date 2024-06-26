import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2f_permutation_example(count: int):
    examples = []
    for _ in range(count):
        n = random.randint(5, 1000)  # Random integer for n, between 5 and 15
        r = random.randint(2, n - 1)
        choice_one = __random_io_permutation(n, r)
        choice_two = __random_io_permutation(n, r, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_permutation(n: int, r: int, prev_choice=None) -> str:
    explanations = [
        f"##permutation({n},{r}))",
        f"##multiplication(##combination({n},{r}), ##factorial({r}))",
    ]
    if prev_choice is not None:
        explanations.remove(prev_choice)
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_permutation_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
