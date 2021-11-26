def spin_words(sentence):
    sentence_list = [word[-1::-1] if len(word) >= 5 else word for word in sentence.split(" ")]
    return ' '.join(sentence_list)