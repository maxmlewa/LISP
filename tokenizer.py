"""

"""

def tokenize(source):
    """
    Splits the input string into meaningful tokens.

    @params
        source : a string containing the source code of a
            Scheme expression
    """

    white_space = {" ", "\n"}
    parentheses = {"(" , ")"}
    token_list = []

    return None

def recursiveTokenizer(sub_source, token = "", tokens = []):
    """
    Recursively populates the tokens_list using
    arguments from the source passed when calling tokenize

    @params
        sub_source : a string containing a subset of the 
            original Scheme expression
        token : the cumulatively grown token to be added
            to the token list
    @returns a populated list of tokens
    """
    
    if not sub_source:
        if token != "":
            tokens.append(token)
            return tokens
    
    next_element = sub_source[0]

    if next_element == ";":
        pass