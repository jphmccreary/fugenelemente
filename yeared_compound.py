import requests

request_prefix = "http://localhost:2020?sentence="

class YearedCompound:
    """
    Stores relevant data for a compound from the corpus inc:
    year, number of occurances, corpus, type of corpus (eg news, website, ...?),
    splits, Fugenelement(e?)
    """
    def __init__(self, text, year, count, corpus, source) -> None:
        # CHOP IT UP
        response = requests.get(request_prefix + text)
        response.encoding = 'UTF-8'
        self.splits = response.text.split()
        if len(self.splits) < 2:
            self.is_compound = False
            return
        else:
            self.is_compound = True

        self.text = text
        self.year = year
        self.count = count
        self.corpus = corpus
        self.source = source

        pass # we will do determination of fugenelemente right here

    def __str__(self):
        return '\n'.join([
            'word:\t\t' + self.text,
            'year:\t\t' + str(self.year),
            'count:\t\t' + str(self.count),
            'corpus:\t\t' + self.corpus,
            'source:\t\t' + self.source,
            'splits:\t\t' + ' '.join(self.splits)
        ])
