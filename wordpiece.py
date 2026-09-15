import re

# Read input file
with open("rawdata.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Basic vocabulary
vocab = {
    "[UNK]",
    "i", "love", "natural", "language", "processing",
    "artificial", "intelligence", "is", "changing",
    "the", "world", "token", "ization", "an", "important",
    "step", "in", "models"
}

def wordpiece_tokenize(word):
    word = word.lower()

    if word in vocab:
        return [word]

    tokens = []
    start = 0

    while start < len(word):
        end = len(word)
        current_token = None

        while start < end:
            subword = word[start:end]

            if start > 0:
                subword = "##" + subword

            if subword in vocab:
                current_token = subword
                break

            end -= 1

        if current_token is None:
            return ["[UNK]"]

        tokens.append(current_token)
        start = end

    return tokens


# Split text into words
words = re.findall(r"\b\w+\b", text)

# Apply WordPiece tokenization
all_tokens = []

for word in words:
    tokens = wordpiece_tokenize(word)
    all_tokens.extend(tokens)

# Write output
with open("wordpiece.output", "w", encoding="utf-8") as file:
    file.write("WordPiece Tokens:\n")
    file.write(" ".join(all_tokens))

print("WordPiece tokenization completed.")
print("Output saved to wordpiece.output")