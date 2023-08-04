from func_nl.f2n_sample_generator import F2NSamples
from nl_func.n2f_sample_generator import N2FSamples

if __name__ == "__main__":
    generator = F2NSamples()
    print(generator.get_f2n_samples(2))
    print(generator.get_next_random_f2n_sample())
    pass
