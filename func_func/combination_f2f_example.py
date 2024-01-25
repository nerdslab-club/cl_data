import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2f_combination_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        n = random.randint(5, 1000)  # Random integer for n, between 5 and 15
        r = random.randint(2, n - 1)
        choice_one = __random_io(n, r, (None if identifier is None else identifier+i))
        choice_two = __random_io(n, r, (None if identifier is None else identifier+i), choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io(n: int, r: int, identifier: int | None, prev_choice=None) -> str:
    explanations = [
        f"##combination({n},{r})",
        f"##floor_division(##permutation({n},{r}), ##factorial({r}))",
        f"##float_to_int(##multiplication(##permutation({n},{r}), ##invert_number(##factorial({r}))))",
    ]
    if prev_choice is not None:
        explanations.remove(prev_choice)
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_combination_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
