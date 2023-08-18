import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_cosine_similarity_example(count: int):
    examples = []
    for _ in range(count):
        vector1 = [random.uniform(-1.0, 1.0) for _ in range(3)]
        vector2 = [random.uniform(-1.0, 1.0) for _ in range(3)]
        examples.append(
            {
                "inputStr": f"##cosine_similarity({vector1}, {vector2})",
                "outputStr": __random_explanation_cosine_similarity(vector1, vector2),
            }
        )
    return examples


def __random_explanation_cosine_similarity(vector1, vector2) -> str:
    explanations = [
        f"The cosine similarity between the vectors {vector1} and {vector2}",
        f"cosine_similarity({vector1}, {vector2})",
        f"The result of calculating the cosine similarity between the vectors {vector1} and {vector2}",
        f"Calculation: cosine_similarity({vector1}, {vector2})",
        f"The cosine similarity value between the vectors {vector1} and {vector2}",
        f"The outcome of finding the cosine similarity between the vectors {vector1} and {vector2}",
        f"The similarity measure of the vectors {vector1} and {vector2} using cosine similarity",
        f"The result of determining the cosine similarity between the vectors {vector1} and {vector2}",
        f"The computed result of calculating the cosine similarity between the vectors {vector1} and {vector2}",
        f"The cosine similarity score between the vectors {vector1} and {vector2}",
        f"The outcome of evaluating cosine_similarity({vector1}, {vector2})",
        f"The value obtained by calculating the cosine similarity between the vectors {vector1} and {vector2}",
        f"The result of evaluating cosine_similarity({vector1}, {vector2})",
        f"The similarity value between the vectors {vector1} and {vector2} using cosine similarity",
        f"The computed cosine similarity value between the vectors {vector1} and {vector2}",
        f"The cosine similarity score of the vectors {vector1} and {vector2}",
        f"The calculated result of determining the cosine similarity between the vectors {vector1} and {vector2}",
        f"The cosine similarity coefficient between the vectors {vector1} and {vector2}",
        f"The result obtained from calculating the cosine similarity between the vectors {vector1} and {vector2}",
        f"The computed similarity measure of the vectors {vector1} and {vector2} using cosine similarity",
        f"The similarity index between the vectors {vector1} and {vector2} using cosine similarity",
        f"The cosine similarity value between the vectors {vector1} and {vector2} is",
        f"The result derived from calculating the cosine similarity between the vectors {vector1} and {vector2}",
        f"The computed cosine similarity coefficient of the vectors {vector1} and {vector2}",
        f"The cosine similarity value obtained by evaluating cosine_similarity({vector1}, {vector2})",
        f"The calculated outcome of evaluating cosine_similarity({vector1}, {vector2})",
        f"The computed similarity index between the vectors {vector1} and {vector2} using cosine similarity",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_cosine_similarity_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
