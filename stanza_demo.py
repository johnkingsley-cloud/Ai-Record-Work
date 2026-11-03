import stanza

stanza.download("en")
nlp = stanza.Pipeline("en", processors="tokenize,ner")

text = "Iota Logistics is a Healthcare company founded in 2000. It is headquartered in Bangalore, UK. The company reported revenue of $3,658,007,647 in 2025, up from $2,951,476,158 in 2024. Iota Logistics employs approximately 100 people and specializes in computer vision. The company's flagship product is SynergyPro, with a growth rate of 23.9% and a performance metric of 0.86."
doc = nlp(text)

for entity in doc.ents:
    print(entity.text, "->", entity.type)