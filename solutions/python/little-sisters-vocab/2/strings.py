def add_prefix_un(word):
    return 'un'+word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    return ' :: '.join([prefix] + [prefix + word for word in words])

def remove_suffix_ness(word):
    if word.endswith('ness'):
        root = word[:-4]
        if root.endswith('i'):
            root = root[:-1] + 'y'
        return root
    return word

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].strip('.')
    return adjective + 'en'