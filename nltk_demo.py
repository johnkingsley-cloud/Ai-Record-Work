import nltk

text = "Advanced Computing is a Technology company founded in 2018. It is headquartered in Bangalore, Brazil. The company reported revenue of $3,912,310,970 in 2025, up from $3,335,143,856 in 2024. Advanced Computing employs approximately 500 people and specializes in 5G networks. The company's flagship product is NexusOS, with a growth rate of 17.3% and a performance metric of 0.67."
words = nltk.word_tokenize(text)
tagged = nltk.pos_tag(words)

entities = nltk.ne_chunk(tagged)

print(entities)