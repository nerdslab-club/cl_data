from src.constants import TaskTypes


class NlToNlSamples:
    TASK_TYPE = TaskTypes.NL_TO_NL_TRANSLATION.value

    def __init__(self):
        self.nl_to_nl_samples = {}
        self.__set_nl_to_nl_samples()
        pass

    def __set_nl_to_nl_samples(self):
        pass

    def __add_to_nl_to_nl_samples(self):
        pass

    def get_nl_to_nl_samples(self):
        return self.nl_to_nl_samples
