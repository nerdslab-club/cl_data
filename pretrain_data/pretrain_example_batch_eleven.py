import random

import spacy

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_eleven_example_paragraph():
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_bool = RandomValueGenerator.generate_random_boolean()
    random_list = Utility.remove_spaces(
        str(RandomValueGenerator.generate_random_list())
    )
    random_binary_str = RandomValueGenerator.generate_random_binary_string()

    examples = [
        [
            f"In the realm of Numerosia, where numbers held the key to unlocking cosmic mysteries, two fearless explorers, Ava and Leo, embarked on a journey to decode the mathematical enigmas that governed the universe.",
            f"Guided by their insatiable curiosity, Ava turned her attention to the mystic realm of trigonometry. She gazed upon the infinite cosmos and pondered the cosmic dance of angles. The whisper of the stars revealed to her the hidden power of cosine. Embracing the energy of {random_float}, she chanted the cosmic incantation: ##cosine({random_float}).",
            f"Meanwhile, Leo ventured into the uncharted territories of tangents. Drawing inspiration from the ebb and flow of waves, he calculated the tangent of {random_float} and felt the pulse of the universe coursing through him: ##tangent({random_float}).",
            f"As the sun dipped below the horizon, casting an ethereal glow upon Numerosia, Ava turned her gaze to the stars and invoked the ancient knowledge of arcsine. In the quiet of the night, she pondered the balance of cosmic forces, calculating arcsine of {random_float} and unveiling its celestial secret: ##arcsine({random_float}).",
            f"Leo, on the other hand, sought the wisdom of arccosine, a cosmic reflection of harmony and equilibrium. With an air of reverence, he gazed upon the night sky and calculated the arccosine of {random_float}, feeling the cosmic threads of unity weave through his being: ##arccosine({random_float}).",
            f"The journey continued under the ever-watchful gaze of the moon, as Ava and Leo ventured deeper into the mathematical cosmos. Their next destination was the realm of arctangent, where the angles of existence converged. Leo calculated the arctangent of {random_float}, glimpsing the symphony of numbers that governed the celestial dance: ##arctangent({random_float}).",
            f"As dawn broke, bathing Numerosia in golden light, Ava turned her attention to the captivating world of hyperbolic functions. She immersed herself in the hyperbolic realm, calculating the hyperbolic sine of {random_float} and feeling the exponential embrace of the cosmos: ##hyperbolic_sine({random_float}).",
            f"Leo's quest led him to the contemplation of hyperbolic cosine, a force that mirrored the cosmic expansion itself. With focused determination, he calculated the hyperbolic cosine of {random_float}, sensing the fabric of spacetime stretch and bend beneath his calculations: ##hyperbolic_cosine({random_float}).",
            f"As the day progressed, Ava and Leo delved even deeper, now guided by the allure of hyperbolic tangent. Ava harnessed the unbounded energy of the hyperbolic tangent of {random_float}, feeling the ebb and flow of cosmic currents course through her veins: ##hyperbolic_tangent({random_float}).",
            f"In their quest for knowledge, the adventurers turned their attention to the ancient language of logarithms. Ava contemplated the cosmic vibrations and calculated the logarithm base 10 of {random_float}, a profound revelation of numerical resonance: ##logarithm_base_10({random_float}).",
            f"Leo, now entranced by the power of binary, embarked on a journey into the depths of logarithms. He calculated the logarithm base 2 of {random_float}, tapping into the primal language of the universe: ##logarithm_base_2({random_float}).",
            f"As the sun painted the sky with hues of orange and gold, Ava and Leo stood at the precipice of a new understanding. They realized that the language of mathematics was the cosmic symphony that harmonized the very fabric of Numerosia. Their journey had unveiled the hidden truths of the universe, and their legacy would forever echo through the ages, inspiring future explorers to unravel the mathematical wonders that shaped the cosmos.",
        ],
        [
            f"In a land where mathematical wonders abound, there was a town named Arctopia. The town's population, {random_list}, was fascinated by the mystical properties of numbers.",
            f"One day, a curious mathematician decided to explore the depths of trigonometry. Armed with a random angle value, {random_float}, the mathematician delved into the world of cosine.",
            f"The cosine of {random_float} radians was ##cosine({random_float}). This value intrigued the mathematician, who decided to find its tangent.",
            f"Calculating the tangent of ##arccosine({random_float}), the mathematician stumbled upon a hidden truth.",
            f"Meanwhile, on the other side of town, another mathematician was engrossed in hyperbolic equations. They pondered over the hyperbolic sine of {random_int_one}.",
            f"As the sun set, casting long shadows, a group of young students gathered to unravel logarithmic mysteries. They calculated the base-10 logarithm of {random_int_two}, discovering a peculiar pattern.",
            f"Among them, a prodigious child wondered about the cube root of ##hyperbolic_tangent({random_int_three}).",
            f"Lost in thought, a seasoned professor contemplated the profound question: What is the result of ##logarithm_base_2({random_int_four}) raised to the power of ##arcsine({random_float})?",
            f"In a twist of fate, the two mathematicians crossed paths and decided to combine their knowledge. They embarked on a journey to solve the equation ##hyperbolic_cosine({random_float}) * ##exponentiation({random_int_one},{random_int_four}) - ##tangent({random_int_three}).",
            f"After intense calculations, they found the solution: {random_int_two + random_int_four}. Overwhelmed by their success, the townspeople celebrated with a grand feast, and the legend of Arctopia's mathematical marvels lived on.",
        ],
    ]

    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator
    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_eleven_example_paragraph(),
        1,
    )
    # print(len(masked_example), masked_example)
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator
    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_eleven_example_paragraph(),
        1,
    )
    sample = Utility.create_sample_from_example(
        next_token_example, PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
