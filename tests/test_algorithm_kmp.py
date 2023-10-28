from algorithms.algorithm_kmp import AlgorithmKnuthMorrisPratt


def test_create_array():
    obj = AlgorithmKnuthMorrisPratt("kikika", "kikilaki kikikata")
    assert obj.create_array() == [0, 0, 1, 2, 3, 0]


def test_create_array_empty_subtext():
    obj = AlgorithmKnuthMorrisPratt("", "kikilaki kikikata")
    assert obj.create_array() is None


def test_create_array_one_sym_in_subtext():
    obj = AlgorithmKnuthMorrisPratt("2", "kikilaki kikikata")
    assert obj.create_array() == [0]

