import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_calculate_dot_product_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        vector1 = RandomValueGenerator.generate_random_list(3, -10, 10)
        vector2 = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(vector1, vector2, (None if identifier is None else identifier+i)),
            "outputStr": f"##calculate_dot_product({vector1}, {vector2})",
        })
    return examples


def __random_explanation(vector: list, vector1: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    lst_str1 = " , ".join(str(num) for num in vector1)
    explanations = [
        f"Calculate the dot product of vectors {lst_str} and {lst_str1}",
        f"CALCULATE_DOT_PRODUCT({lst_str}, {lst_str1})",
        f"Determine the result of the dot product for vectors {lst_str} and {lst_str1}",
        f"Find the dot product of vectors {lst_str} and {lst_str1}",
        f"The result of calculating the dot product for vectors {lst_str} and {lst_str1}",
        f"Performing the calculate_dot_product operation for vectors {lst_str} and {lst_str1}",
        f"The dot product of vectors {lst_str} and {lst_str1}",
        f"CALCULATE_DOT_PRODUCT operation: {lst_str}, {lst_str1}",
        f"The result after calculating the dot product for vectors {lst_str} and {lst_str1}, what is it?",
        f"Determine the dot product of vectors {lst_str} and {lst_str1}",
        f"Let's calculate the dot product of vectors {lst_str} and {lst_str1}",
        f"The dot product result of vectors {lst_str} and {lst_str1}, is it true?",
        f"Calculating the dot product of vectors {lst_str} and {lst_str1}",
        f"The dot product result after calculating dot product for vectors {lst_str} and {lst_str1}",
        f"The dot product of vectors {lst_str} and {lst_str1}, what is its value?",
        f"Let's determine the dot product of vectors {lst_str} and {lst_str1}",
        f"The dot product of vectors {lst_str} and {lst_str1}",
        f"The dot product of vectors {lst_str} and {lst_str1}, what is the result?",
        f"The dot product of vectors {lst_str} and {lst_str1}, what does it give?",
        f"The dot product of vectors {lst_str} and {lst_str1} and provide the result",
        f"CALCULATE_DOT_PRODUCT({vector}, {vector1}), what does it yield?",
        f"The dot product of vectors {lst_str} and {lst_str1}, ignoring order",
        f"The result after calculating the dot product of vectors {lst_str} and {lst_str1}",
        f"Calculate the dot product of vectors {lst_str} and {lst_str1}, find the answer",
        f"The dot product of vectors {lst_str} and {lst_str1}, what does it give?",
        f"Let's find the result after calculating the dot product of vectors {lst_str} and {lst_str1}",
        f"The dot product result of vectors {lst_str} and {lst_str1}, what is the output?",
        f"The result after calculating the dot product of vectors {lst_str} and {lst_str1}, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_calculate_dot_product_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
