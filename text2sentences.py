from razdel import sentenize

def is_valid_text(text: str):
    text = text.strip('—').strip(' ')

    if "«" in text and "»" not in text:
        return False
    if "«" not in text and "»" in text:
        return False
    if '"' in text:
        return False
    if text[0].islower():
        return False
    if "|" in text:
        return False
    # if len(text.split(' ')) < 2:
    #     return False
    if text[-1] == '-':
        return False

    alphabet = 'ә!өҡғҫ,ҙһ?ң-үйцукенгшщзхъфывапролджэёәячсмитьбю.«» '
    alphabet += 'ӘӨҠҒҪ;ҘҺҢҮЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ:—'

    for c in text:
        if c not in alphabet:
            return False

    return True

if __name__ == "__main__":
    source_path = "book_raw.txt"
    result_path = "book_sentences.txt"

    with open(source_path, "rt", encoding="utf-8") as f:
        lines = f.readlines()

        with open(result_path, "wt", encoding="utf-8") as wf:
            for line in lines:
                sentences = sentenize(line)
                for sent in sentences:
                    if len(sent.text) == 0:
                        continue
                    if is_valid_text(sent.text):
                        wf.write(sent.text + '\n')
