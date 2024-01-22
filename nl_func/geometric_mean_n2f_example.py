import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_geometric_mean_example(count: int):
    examples = []
    for _ in range(count):
        numbers = RandomValueGenerator.generate_random_list(5, 1, 100)
        examples.append({
            "inputStr": __random_explanation(numbers),
            "outputStr": f"##geometric_mean({numbers})",
        })
    return examples


def __random_explanation(vector: list[float]) -> str:
    lst_str = ", ".join(str(num) for num in vector)
    explanations = [
        f"Calculate the geometric mean of the list {lst_str}",
        f"GEOMETRIC_MEAN({vector})",
        f"Determine the geometric mean of the elements in the list {lst_str}",
        f"Find the geometric mean value for the list {lst_str}",
        f"The result of calculating the geometric mean of {lst_str}",
        f"Performing the geometric mean operation on the list {lst_str}",
        f"The geometric mean of the list {lst_str}",
        f"GEOMETRIC_MEAN calculation: {lst_str}",
        f"The result after calculating the geometric mean of {lst_str}, what is it?",
        f"The geometric mean value of {lst_str}, what does it give?",
        f"Let's find the geometric mean value of the list {lst_str}",
        f"Geometric mean of the list {lst_str}, result is",
        f"Calculating the geometric mean for the list {lst_str}",
        f"The geometric mean result after calculating the geometric mean of {lst_str}",
        f"The geometric mean of the list {lst_str}, what is its value?",
        f"Let's determine the geometric mean of the list {lst_str}",
        f"The geometric mean value of the list {lst_str}",
        f"The geometric mean of the list {lst_str}, what is the result?",
        f"The geometric mean of the list {lst_str}, what does it give?",
        f"The geometric mean of the list {lst_str} and provide the result",
        f"GEOMETRIC_MEAN({vector}), what does it yield?",
        f"The geometric mean value of the list {lst_str}, ignoring order",
        f"The result after calculating the geometric mean of {lst_str}",
        f"The geometric mean of the list {lst_str}, what is it?",
        f"Calculate the geometric mean of the list {lst_str}, find the answer",
        f"The geometric mean of the list {lst_str}, what does it give?",
        f"Let's find the result after calculating the geometric mean of {lst_str}",
        f"Geometric mean of the list {lst_str}, what is the output?",
        f"The result after calculating the geometric mean of {lst_str}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_geometric_mean_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
