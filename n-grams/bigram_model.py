from collections import Counter, defaultdict
import random

def train_bigram(words):
    bigram_counts = Counter()
    unigram_counts = Counter()

    for w in words:
        tokens = ["<s>"] + list(w) + ["</s>"]
        for ch1, ch2 in zip(tokens, tokens[1:]):
            bigram_counts[(ch1, ch2)] += 1
            unigram_counts[ch1] += 1  
    return bigram_counts, unigram_counts


def bigram_probabilities(bigram_counts, unigram_counts):
    probs = defaultdict(dict)

    for (ch1, ch2), count in bigram_counts.items():
        probs[ch1][ch2] = count / unigram_counts[ch1] # probs['c'] = {'a': 0.8, 'o': 0.2}

    return probs


def sample_word(probs, max_length=20):
    current = "<s>"
    result = []

    while True:
        next_chars = list(probs[current].keys())
        next_probs = list(probs[current].values())

        next_char = random.choices(next_chars, weights=next_probs, k=1)[0]

        if next_char == "</s>" or len(result) >= max_length:
            break

        result.append(next_char)
        current = next_char

    return "".join(result)


if __name__ == "__main__":
    # words = open("names.txt").read().splitlines()
    words = ["cat", "cap", "can", "dog", "dot"]

    bigram_counts, unigram_counts = train_bigram(words)
    probs = bigram_probabilities(bigram_counts, unigram_counts)

    for _ in range(10):
        print(sample_word(probs))
