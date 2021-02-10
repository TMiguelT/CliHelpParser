import spacy
import wordsegment


def prevent_sentence_boundary_detection(doc):
    for token in doc:
        token.is_sent_start = False
    return doc


try:
    nlp = spacy.load("en_core_web_sm")
    no_sentences = spacy.load("en_core_web_sm")
    no_sentences.add_pipe(
        prevent_sentence_boundary_detection, name="prevent-sbd", before="parser"
    )
except IOError:
    raise Exception(
        "Spacy model doesn't exist! Install it with `python -m spacy download en`"
    )

# We load the spacy and the wordsegment models here as a kind of singleton pattern, to avoid multiple functions loading
# redundant copies

if len(wordsegment.WORDS) == 0:
    wordsegment.load()


def is_sentence(text: str, threshold: float = 0.8) -> bool:
    """
    Returns a bool that indicates if this text is likely a sentence. This should probably be replaced by a machine
    learning classifier in the future
    :param threshold: If the ratio of non-word tokens over word tokens is higher than this, then return False
    """

    doc = no_sentences(text)
    sents = list(doc.sents)

    if len(sents) == 0:
        return False

    sentence = sents[0]
    non_word_count = 0
    word_count = 0
    for tok in sentence:
        pos = tok.pos_
        if pos == "SPACE":
            # Ignore whitespace
            continue

        if pos in {"X", "SYM", "PUNCT", "NUM"}:
            non_word_count += 1
        word_count += 1

    result = word_count == 0 or non_word_count / word_count < threshold
    return result
