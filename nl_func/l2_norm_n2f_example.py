import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_l2_norm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        vector = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(vector, (None if identifier is None else identifier+i)),
            "outputStr": f"##l2_norm({vector})",
        })
    return examples


def __random_explanation(vector: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    explanations = [
        f"Calculate the L2 norm of the vector {lst_str}",
        f"Determine the result of the L2 norm for the vector {lst_str}",
        f"Find the L2 norm of the vector {lst_str}",
        f"The result of calculating the L2 norm of the vector {lst_str}",
        f"Performing the L2 norm calculation for the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}",
        f"The result after calculating the L2 norm of the vector {lst_str}, what is it",
        f"The L2 norm of the vector {lst_str}, what does it give",
        f"Let's calculate the L2 norm of the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}, result is",
        f"Calculating the L2 norm of the vector {lst_str}",
        f"The L2 norm result after calculating L2 norm for the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}, what is its value",
        f"Let's determine the L2 norm of the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}, what is the result",
        f"The result after calculating the L2 norm of the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}, what is it",
        f"Calculate the L2 norm of the vector {lst_str}, find the answer",
        f"The L2 norm of the vector {lst_str}, what does it give",
        f"Let's find the result after calculating the L2 norm of the vector {lst_str}",
        f"The L2 norm of the vector {lst_str}, what is the output",
        f"The result after calculating the L2 norm of the vector {lst_str}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_l2_norm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
