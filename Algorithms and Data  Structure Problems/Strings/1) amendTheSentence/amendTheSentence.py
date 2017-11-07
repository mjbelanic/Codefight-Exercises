def amendTheSentence(s):
    s = re.sub(r"(?<=\w)([A-Z])", r" \1",, s)
    s = s.lower()
    return s

