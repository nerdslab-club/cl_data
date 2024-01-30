import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2f_cosine_similarity_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        list1 = RandomValueGenerator.generate_random_list()
        list2 = RandomValueGenerator.generate_random_list()
        choice_one = __random_io_operation(list1, list2, (None if identifier is None else identifier+i))
        choice_two = __random_io_operation(list1, list2, (None if identifier is None else identifier+i), choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(list1, list2, identifier: int | None, prev_choice=None) -> str:
    explanations = [
        f"##cosine_similarity({list1}, {list2})",
        f"##division(##calculate_dot_product({list1}, {list2}), ##multiplication( ##l2_norm({list1}), ##l2_norm({list2})))",
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
            create_f2f_cosine_similarity_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
