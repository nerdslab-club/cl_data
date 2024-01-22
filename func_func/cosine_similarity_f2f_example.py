import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2f_cosine_similarity_example(count: int):
    examples = []
    for _ in range(count):
        item = RandomValueGenerator.generate_random_integer(2, 10)
        list1 = RandomValueGenerator.generate_random_list(
            length=item, start_range=-10, end_range=100
        )
        list2 = RandomValueGenerator.generate_random_list(
            length=item, start_range=-10, end_range=100
        )
        choice_one = __random_io_operation(list1, list2)
        choice_two = __random_io_operation(list1, list2, choice_one)
        examples.append(
            {
                "inputStr": Utility.remove_spaces(choice_one),
                "outputStr": Utility.remove_spaces(choice_two),
            }
        )
    return examples


def __random_io_operation(list1, list2, prev_choice=None) -> str:
    explanations = [
        f"##cosine_similarity({list1}, {list2})",
        f"##division(##calculate_dot_product({list1}, {list2}), ##multiplication( ##l2_norm({list1}), ##l2_norm({list2})))",
    ]

    if prev_choice is not None:
        explanations.remove(prev_choice)

    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2f_cosine_similarity_example(2), TaskTypes.FUNC_TO_FUNC_TRANSLATION
        )
    )
