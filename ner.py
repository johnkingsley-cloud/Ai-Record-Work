import spacy

nlp = spacy.load("en_core_web_sm")

text = "Compare the growth rates of Advanced Computing and Nova Ventures."

doc = nlp(text)

for entity in doc.ents:
    print(entity.text, "->", entity.label_)