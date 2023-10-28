from algorithms.algorithm_kmp import AlgorithmKnuthMorrisPratt


obj = AlgorithmKnuthMorrisPratt("kikika", "kikilaki kikikata")


def test_create_array():
    assert obj.create_array() == [0, 0, 1, 2, 3, 0]


def test_create_array_empty_subtext():
    obj.subtext = ""
    assert obj.create_array() is None


def test_create_array_one_sym_in_subtext():
    obj.subtext = "2"
    assert obj.create_array() == [0]


def test_create_array_two_syms_in_subtext():
    obj.subtext = "2a"
    assert obj.create_array() == [0, 0]


def test_create_array_two_equal_syms_in_subtext():
    obj.subtext = "tt"
    assert obj.create_array() == [0, 1]


def test_search_subtext():
    obj.subtext = "kikika"
    obj.text = "kikilaki kikikata"
    assert obj.search_subtext() == 9


def test_search_subtext_empty_subtext():
    obj.subtext = ""
    obj.text = "kikilaki kikikata"
    assert obj.search_subtext() is None



def test_search_subtext_no_success_search():
    obj.subtext = "bro"
    obj.text = "kikilaki kikikata"
    assert obj.search_subtext() is None


def test_search_subtext_where_text_shorter_than_subtext():
    obj.subtext = "kikika long subtext for test"
    obj.text = "kikilaki kikikata"
    assert obj.search_subtext() is None


def test_search_subtext_where_subtext_equal_text():
    obj.subtext = "kikilaki kikikata"
    obj.text = "kikilaki kikikata"
    assert obj.search_subtext() == 0


def test_search_subtext_with_empty_text():
    obj.subtext = "kikika"
    obj.text = ""
    assert obj.search_subtext() is None


def test_search_subtext_with_empty_text_and_subtext():
    obj.subtext = ""
    obj.text = ""
    assert obj.search_subtext() is None
