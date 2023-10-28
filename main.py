from algorithms.algorithm_kmp import AlgorithmKnuthMorrisPratt


def main():
    text = "лилилось лилилась"
    subtext = "лилила"
    alg_kmp = AlgorithmKnuthMorrisPratt(subtext, text)

    print(alg_kmp, type(alg_kmp))
    print(alg_kmp.create_array())


if __name__ == '__main__':
    main()
