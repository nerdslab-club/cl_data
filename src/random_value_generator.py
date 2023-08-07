import random


class RandomValueGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random_list(length=4, start_range=0, end_range=500, seed=None):
        """
        Generate a random list of numbers.

        Parameters:
            length (int): The length of the list to generate.
            start_range (int): The inclusive start of the random range.
            end_range (int): The exclusive end of the random range.
            seed (int, optional): The seed value for random number generation.
            If provided, the same seed will produce the same random list.

        Returns:
            list: A list of random numbers within the specified range.
        """
        if seed is not None:
            random.seed(seed)

        random_list = [
            random.randint(start_range, end_range - 1) for _ in range(length)
        ]
        return random_list

    @staticmethod
    def generate_random_integer(start_range=0, end_range=10000, seed=None):
        """
        Generate a random integer.

        Parameters:
            start_range (int): The inclusive start of the random range.
            end_range (int): The exclusive end of the random range.
            seed (int, optional): The seed value for random number generation.
                If provided, the same seed will produce the same random integer.

        Returns:
            int: A random integer within the specified range.
        """
        if seed is not None:
            random.seed(seed)

        random_int = random.randint(start_range, end_range - 1)
        return random_int

    @staticmethod
    def generate_random_float(start_range=0.0, end_range=10000, seed=None):
        """
        Generate a random float.

        Parameters:
            start_range (float): The inclusive start of the random range.
            end_range (float): The exclusive end of the random range.
            seed (int, optional): The seed value for random number generation.
                If provided, the same seed will produce the same random float.

        Returns:
            float: A random float within the specified range.
        """
        if seed is not None:
            random.seed(seed)

        random_float = random.uniform(start_range, end_range)
        return random_float

    @staticmethod
    def generate_random_boolean(seed=None):
        """
        Generate a random boolean (True or False).

        Parameters:
            seed (int, optional): The seed value for random boolean generation.
                If provided, the same seed will produce the same random boolean.

        Returns:
            bool: A random boolean value.
        """
        if seed is not None:
            random.seed(seed)

        random_bool = random.choice([True, False])
        return random_bool


if __name__ == "__main__":
    # print(RandomValueGenerator.generate_random_list(6, 1, 100, 43))
    # print(RandomValueGenerator.generate_random_list(6, 1, 100, 43))
    pass
