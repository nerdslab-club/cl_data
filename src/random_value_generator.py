import random


class RandomValueGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_random_list(length=4, start_range=1, end_range=99, seed=54):
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
    def generate_random_integer(start_range=1, end_range=99, seed=54):
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
    def generate_random_float(start_range=1.0, end_range=99, round_to=1, seed=54):
        """
        Generate a random float.

        Parameters:
            start_range (float): The inclusive start of the random range.
            end_range (float): The exclusive end of the random range.
            seed (int, optional): The seed value for random number generation.
                If provided, the same seed will produce the same random float.
            round_to: round to the round to.

        Returns:
            float: A random float within the specified range.

        """
        if seed is not None:
            random.seed(seed)

        random_float = round(random.uniform(start_range, end_range), round_to)
        return random_float

    @staticmethod
    def generate_random_boolean(seed=54):
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

    @staticmethod
    def generate_random_binary_string(seed=54):
        """
        Generate a random binary string of the specified length.

        Parameters:
            seed (int, optional): The seed value for random binary string generation.
                If provided, the same seed will produce the same random binary string.

        Returns:
            str: A random binary string of the specified length.
        """
        length = RandomValueGenerator.generate_random_integer(2, 20)
        if seed is not None:
            random.seed(seed)

        random_binary_string = ""
        for _ in range(length):
            random_binary_string += str(random.choice(["0", "1"]))

        return random_binary_string

    @staticmethod
    def generate_random_string(seed=54):
        """
        Generate a random string.

        :return: random generated string.
        """
        if seed is not None:
            random.seed(seed)
        return "".join(
            random.choice("abccbadeffeghihgjklmnonmlkjpqrstuuuvwxwvyvz")
            for _ in range(RandomValueGenerator.generate_random_integer(2, 16))
        )


if __name__ == "__main__":
    print(RandomValueGenerator.generate_random_float())
    print(RandomValueGenerator.generate_random_list(6, 1, 100, 43))
