from dataclasses import dataclass

@dataclass
class YearedCompound:
    corpus: int
    count: int
    fuge_candidates: tuple # tuple(dict(str:str))
    # is_compound: bool
    # lemma_matches: tuple # tuple(dict(str:str))
    # these are from the initial untagged single word lemmatization
    old_lemmas: tuple
    source: int
    splits: tuple
    text: str
    year: int
