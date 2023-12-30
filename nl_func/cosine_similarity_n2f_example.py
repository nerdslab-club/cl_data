import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_cosine_similarity_example(count: int):
    examples = []
    for _ in range(count):
        vector1 = RandomValueGenerator.generate_random_list(3, -10, 10)
        vector2 = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(vector1, vector2),
            "outputStr": f"##cosine_similarity({vector1}, {vector2})",
        })
    return examples


def __random_explanation(vector1: list, vector2: list) -> str:
    explanations = [
        f"Calculate the cosine similarity between vectors {vector1} and {vector2}",
        f"COSINE_SIMILARITY({vector1}, {vector2})",
        f"Determine the cosine similarity for vectors {vector1} and {vector2}",
        f"Find the cosine similarity between vectors {vector1} and {vector2}",
        f"The result of calculating the cosine similarity between vectors {vector1} and {vector2}",
        f"Performing the cosine similarity calculation for vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}",
        f"COSINE_SIMILARITY calculation: ({vector1}, {vector2})",
        f"The result after calculating the cosine similarity between vectors {vector1} and {vector2}, what is it?",
        f"The cosine similarity between vectors {vector1} and {vector2}, what does it give?",
        f"Let's calculate the cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}, result is",
        f"Calculating the cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity result after calculating between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}, what is its value?",
        f"Let's determine the cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}, what is the result?",
        f"The cosine similarity between vectors {vector1} and {vector2}, what does it give?",
        f"The cosine similarity between vectors {vector1} and {vector2} and provide the result",
        f"COSINE_SIMILARITY({vector1}, {vector2}), what does it yield?",
        f"The cosine similarity between vectors {vector1} and {vector2}, ignoring order",
        f"The result after calculating the cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}, what is it?",
        f"Calculate the cosine similarity between vectors {vector1} and {vector2}, find the answer",
        f"The cosine similarity between vectors {vector1} and {vector2}, what does it give?",
        f"Let's find the result after calculating the cosine similarity between vectors {vector1} and {vector2}",
        f"The cosine similarity between vectors {vector1} and {vector2}, what is the output?",
        f"The result after calculating the cosine similarity between vectors {vector1} and {vector2}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cosine_similarity_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
