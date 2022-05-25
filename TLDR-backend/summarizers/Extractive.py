from summarizer import Summarizer

class Extractive:

    def __init__(self, input_paragraphs):
        """
        """
        self._input_paragraphs = input_paragraphs
        self._summarizations = []

    def collect_summarizations(self):
        """
        Gets most important 3
        :return: list : summarizations
        """
        summarizations = []
        for paragraph in self._input_paragraphs:
            summarizations.append(self.extract(paragraph))
        self._summarizations = summarizations
        return summarizations

    def extract(self, paragraph):
        """
        Gets most important with BERTSum
        :return: list : summarizations
        """
        model = Summarizer()
        result = model(paragraph, min_length=60)
        full = ''.join(result)
        return full