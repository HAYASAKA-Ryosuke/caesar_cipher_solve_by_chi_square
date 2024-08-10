from string import ascii_lowercase


alphabet_frequencies = {
    "a": 8.167 / 100,
    "b": 1.492 / 100,
    "c": 2.782 / 100,
    "d": 4.253 / 100,
    "e": 12.702 / 100,
    "f": 2.228 / 100,
    "g": 2.015 / 100,
    "h": 6.094 / 100,
    "i": 6.966 / 100,
    "j": 0.153 / 100,
    "k": 0.772 / 100,
    "l": 4.025 / 100,
    "m": 2.406 / 100,
    "n": 6.749 / 100,
    "o": 7.507 / 100,
    "p": 1.929 / 100,
    "q": 0.095 / 100,
    "r": 5.987 / 100,
    "s": 6.327 / 100,
    "t": 9.056 / 100,
    "u": 2.758 / 100,
    "v": 0.978 / 100,
    "w": 2.360 / 100,
    "x": 0.150 / 100,
    "y": 1.974 / 100,
    "z": 0.074 / 100,
}


def rotate_lower_str(s: str, n: int):
    result = ''
    for c in s:
        result += chr(ord('a') + (ord(c) - ord('a') + n) % len(ascii_lowercase))
    return result


def calc_chi_squared(s: str):
    frequencies = {c: 0 for c in ascii_lowercase}
    for c in s:
        frequencies[c] += 1
    result = 0
    for c in ascii_lowercase:
        expected = alphabet_frequencies[c] * len(s)
        result += ((frequencies[c] - expected) ** 2) / expected
    return result


def estimate_rotation_index(sentence: str):
    result = 0
    min_chi_squared_value = float('inf')
    for i in range(len(ascii_lowercase)):
        chi_squared_value = calc_chi_squared(rotate_lower_str(sentence.lower(), i))
        if min_chi_squared_value > chi_squared_value:
            result = i
            min_chi_squared_value = chi_squared_value
    return result


sentence = 'QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD'
print(rotate_lower_str(sentence.lower(), estimate_rotation_index(sentence)))
