import nltk
# nltk.download()

#commenting the code for git checking!!

para = """
        Search is part of everyday life, especially considering the vast amounts of data generated in the modern interconnected world.
        Azure Cognitive Search exists to compliment existing technologies and provides a programmable search engine built on Apache Lucene. 
        Azure Cognitive Search is a highly available platform offering a 99.9% uptime SLA available for cloud and on-premises assets.

        """

sentences = nltk.sent_tokenize(para)
print(sentences)
words = nltk.word_tokenize(para)
print(words)

# words = nltk.sent
