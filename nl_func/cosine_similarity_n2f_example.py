import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_cosine_similarity_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        vector1 = RandomValueGenerator.generate_random_list()
        vector2 = RandomValueGenerator.generate_random_list()
        examples.append({
            "inputStr": __random_explanation(vector1, vector2, (None if identifier is None else identifier+i)),
            "outputStr": f"##cosine_similarity({vector1}, {vector2})",
        })
    return examples


def __random_explanation(vector: list, vector1: list, identifier: int | None) -> str:
    lst_str = " , ".join(str(num) for num in vector)
    lst_str1 = " , ".join(str(num) for num in vector1)
    explanations = [
        f"Calculate the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"Determine the cosine similarity for vectors {lst_str} and {lst_str1}",
        f"Find the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The result of calculating the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"Performing the cosine similarity calculation for vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The result after calculating the cosine similarity between vectors {lst_str} and {lst_str1}, what is it",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what does it give",
        f"Let's calculate the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, result is",
        f"Calculating the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity result after calculating between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what is its value",
        f"Let's determine the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what is the result",
        f"The result after calculating the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what is it",
        f"Calculate the cosine similarity between vectors {lst_str} and {lst_str1}, find the answer",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what does it give",
        f"Let's find the result after calculating the cosine similarity between vectors {lst_str} and {lst_str1}",
        f"The cosine similarity between vectors {lst_str} and {lst_str1}, what is the output",
        f"The result after calculating the cosine similarity between vectors {lst_str} and {lst_str1}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cosine_similarity_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
