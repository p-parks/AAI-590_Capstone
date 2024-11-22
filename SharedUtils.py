def trim_to_last_punctuation(text):
    # attempt to trim any of the cut off sentences
    # reverse find the last punctuation
    last_punctuation = -1
    for p in ['.', '!', '?']:
        last_punctuation = text.rfind(p)
        if last_punctuation != -1:
            break
    if last_punctuation != -1:
        text = text[:last_punctuation + 1]
    return text


max__text_length = 1024

def trim_to_max_length(text):
    # trim the text to max length
    if len(text) > max__text_length:
        text = text[:max__text_length]
    
    return trim_to_last_punctuation(text)