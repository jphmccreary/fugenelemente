class TTRContainer:
    """
    Stores types and tokens from some list of tokenized data.\n
    ttr() returns type-token-ratio.\n
    Tokens are stored internally in a list.
    Types are stored in a set, which ignores attempts to add dupes.
    """

    def __init__(self, token_list: list[str] = []) -> None:
        # store tokens and types in a list and a set
        # we need to call list() to create a copy of the input list,
        # rather than a reference to it
        self.tokens = list(token_list)
        self.types = set(token_list)

    def add_token(self, token):
        """
        Add a token to the internal list.\n
        Also adds a type to the internal set, if not already present.
        """
        # add the token to the list and the set, if possible
        self.tokens.append(token)
        self.types.add(token)

    def ttr(self) -> float:
        'Returns # of types / # of tokens'
        return len(self.types) / len(self.tokens)

    def mean_token_length(self) -> float:
        'Returns the mean length of tokens in the list.'
        return avg_len(self.tokens)

    # fortunately len(list) and len(set) are O(1). it's just a lookup.
    def token_ct(self) -> int:
        'returns the number of tokens in this TTRContainer'
        return len(self.tokens)

    def type_ct(self) -> int:
        'returns the number of types in this TTRContainer'
        return len(self.types)
