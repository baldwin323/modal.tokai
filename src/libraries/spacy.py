```python
import spacy

class SpacyNLP:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        return self.nlp(text)

    def get_entities(self, doc):
        return [(ent.text, ent.label_) for ent in doc.ents]

    def get_tokens(self, doc):
        return [token.text for token in doc]

    def get_lemmas(self, doc):
        return [token.lemma_ for token in doc]

    def get_pos_tags(self, doc):
        return [(token.text, token.pos_) for token in doc]

    def get_dependency_parse(self, doc):
        return [(token.text, token.dep_, token.head.text) for token in doc]
```