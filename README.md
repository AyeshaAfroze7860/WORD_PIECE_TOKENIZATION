# WordPiece Tokenization

## Overview

This project implements the **WordPiece Tokenization algorithm** using Python.

WordPiece is a subword tokenization technique used in Natural Language Processing (NLP). Instead of representing every word as a single token, it breaks words into smaller subword units. Continuation subwords are represented using the `##` prefix.

This implementation demonstrates the complete WordPiece workflow, including word frequency calculation, initial vocabulary creation, pair frequency calculation, WordPiece scoring, vocabulary merging, final tokenization, and token ID generation.

## Project Structure

```text
WORD_PIECE_TOKENIZATION/
│
├── rawdata.txt
├── wordpiece.py
└── wordpiece.output
```

## Input Data

The input data is stored in `rawdata.txt`.

The file contains words such as:

```text
computer
computers
computing
computed
connect
connected
connecting
connection
create
created
creating
creator
```

Each word is stored on a separate line.

## How It Works

The program follows these steps:

### 1. Read Raw Data

The program reads the words from `rawdata.txt` and converts them to lowercase.

### 2. Calculate Word Frequencies

The frequency of every word is calculated using Python's `Counter`.

Example:

```text
computer : 1
computers : 1
connect : 2
connected : 1
```

### 3. Initial Word Splitting

Each word is initially divided into individual characters.

The first character is kept as it is, while subsequent characters receive the `##` prefix.

Example:

```text
computer
```

becomes:

```text
['c', '##o', '##m', '##p', '##u', '##t', '##e', '##r']
```

### 4. Create Initial Vocabulary

The unique character-level tokens are collected to form the initial vocabulary.

Example:

```text
c
##a
##c
##d
##e
##g
##i
##m
##n
##o
##p
##r
##s
##t
##u
```

### 5. Calculate Token Frequency

The program calculates how frequently each token occurs based on the word frequencies in the input data.

### 6. Calculate Pair Frequency

Adjacent token pairs are identified and their frequencies are calculated.

For example:

```text
##m + ##p
```

can form a token pair.

### 7. Calculate WordPiece Scores

A score is calculated for each token pair:

```text
score = pair_frequency / (frequency_of_first_token × frequency_of_second_token)
```

The pair with the highest score is selected for merging.

### 8. Merge Token Pairs

The selected pair is merged to create a new subword token.

For example:

```text
##m + ##p
```

can be merged into:

```text
##mp
```

The process continues until the target vocabulary size is reached.

### 9. Final Word Splits

After the merging process, the words are represented using the learned subword vocabulary.

For example, the project produces:

```text
computer -> ['compu', '##t', '##e', '##r']
```

### 10. Final Vocabulary

The learned vocabulary contains the original character tokens as well as the newly created subword tokens.

The project produces a final vocabulary containing **24 tokens**, including `[UNK]`.

### 11. Tokenization

The program uses the learned vocabulary to tokenize the test word.

For the test word:

```text
computer
```

the output is:

```text
['compu', '##t', '##e', '##r']
```

### 12. Token IDs

Each vocabulary token is assigned a numerical ID.

For the tokenized word:

```text
compu ##t ##e ##r
```

the project produces:

```text
[22, 17, 3, 14]
```

## Sample Output

```text
========== TOKENIZATION ==========

Input Word : computer
Tokens : ['compu', '##t', '##e', '##r']

========== TOKEN IDs ==========

Input Tokens : ['compu', '##t', '##e', '##r']
Token IDs : [22, 17, 3, 14]
```

## Requirements

* Python 3.x
* No external libraries are required.

The implementation uses Python's built-in `collections.Counter`.


## Technologies Used

* Python
* Natural Language Processing
* WordPiece Tokenization
* Subword Tokenization

## Conclusion

This project demonstrates how the WordPiece algorithm can be implemented from scratch. It starts with character-level representations, calculates token pair scores, merges suitable token pairs to create subwords, builds a final vocabulary, tokenizes a word using the learned vocabulary, and converts the resulting tokens into numerical token IDs.
