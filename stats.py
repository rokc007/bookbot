def get_num_words(text):
    counter = 0
    for word in text.split():
        counter += 1
    return f"Found {counter} total words"


def count_characters(text):
    counts = {}
    for ch in text.lower():
        if ch.isalpha():             # keep only letters ? Hočemo vse znake?
            counts[ch] = counts.get(ch, 0) + 1
    return counts