import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_geometric_series_sum_example(count: int):
    examples = []
    for _ in range(count):
        a = random.uniform(1.0, 10.0)
        r = random.uniform(0.1, 2.0)
        n = random.randint(1, 10)
        examples.append(
            {
                "inputStr": f"##geometric_series_sum({a}, {r}, {n})",
                "outputStr": __random_explanation_geometric_series_sum(a, r, n),
            }
        )
    return examples


def __random_explanation_geometric_series_sum(a: float, r: float, n: int) -> str:
    explanations = [
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"geometric_series_sum({a}, {r}, {n})",
        f"The result of calculating the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"Calculation: geometric_series_sum({a}, {r}, {n})",
        f"The total sum of a geometric sequence with initial term {a}, ratio {r}, and {n} terms",
        f"The outcome of finding the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The cumulative value of a geometric progression with initial term {a}, ratio {r}, and {n} terms",
        f"The result of determining the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The computed result of calculating the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The summation of a geometric progression with initial term {a}, common ratio {r}, and {n} terms",
        f"The outcome of evaluating geometric_series_sum({a}, {r}, {n})",
        f"The value obtained by calculating the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The result of evaluating geometric_series_sum({a}, {r}, {n})",
        f"The total accumulation of a geometric sequence with initial term {a}, common ratio {r}, and {n} terms",
        f"The computed sum of the geometric progression with initial term {a}, ratio {r}, and {n} terms",
        f"The overall sum of a geometric sequence with initial term {a}, ratio {r}, and {n} terms",
        f"The calculated result of determining the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The cumulative total of a geometric sequence with initial term {a}, ratio {r}, and {n} terms",
        f"The result obtained from calculating the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The computed summation of a geometric sequence with initial term {a}, ratio {r}, and {n} terms",
        f"The summation value of the geometric progression with initial term {a}, ratio {r}, and {n} terms",
        f"The calculated outcome of evaluating geometric_series_sum({a}, {r}, {n})",
        f"The cumulative result of a geometric sequence with initial term {a}, common ratio {r}, and {n} terms",
        f"The calculated sum of the geometric progression with initial term {a}, common ratio {r}, and {n} terms",
        f"The calculated value of the sum of the geometric series with initial term {a}, common ratio {r}, and {n} terms",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_geometric_series_sum_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
