from collections import Counter
import string

def analizuj(text):
    # Zliczanie słów, zdań, i akapitów
    words = text.split()
    sentences = text.count('.') + text.count('!') + text.count('?')
    paragraphs = text.split('\n\n')

    # Najczęściej występujące słowa (bez stop words)
    stop_words = {'i', 'a', 'the', 'and', 'of', 'in', 'on'}
    filtered_words = [word.strip(string.punctuation).lower() for word in words if word.lower() not in stop_words]
    word_counts = Counter(filtered_words)
    most_common = word_counts.most_common(5)

    # Transformacja słów zaczynających się na 'a' lub 'A'
    transformed_words = [word[::-1] if word.lower().startswith('a') else word for word in words]

    return {
        "words_count": len(words),
        "sentences_count": sentences,
        "paragraphs_count": len(paragraphs),
        "most_common_words": most_common,
        "transformed_words": transformed_words
    }

# Przykładowe użycie:
text = "Apple and orange. Are amazing fruits. A wonderful day!"
result = analizuj(text)
print(result)
