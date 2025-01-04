pip install pulp

import nltk
nltk.download('punkt_tab')

import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
import math
import pulp


# Function to generate a summary using linear programming
def generate_summary_with_lp(url, num_sentences=10):
    # Fetch text from URL
    text = Get_Summary.fetch_text(url)
    sentences = sent_tokenize(text)
    keywords = Get_Summary.extract_keywords(url)

    # Generate a weight for each sentence based on keyword relevance
    sentence_weights = []
    keyword_coverage = []

    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        weight = sum([1 for word in words if word in keywords])
        sentence_weights.append(weight)
        coverage = [1 if keyword in words else 0 for keyword in keywords]
        keyword_coverage.append(coverage)

    # Set up the LP problem
    lp_problem = pulp.LpProblem("Summary_Generation", pulp.LpMaximize)

    # Decision variables: one for each sentence
    x = [pulp.LpVariable(f"x_{i}", cat="Binary") for i in range(len(sentences))]

    # Objective function: maximize weighted sum of selected sentences
    lp_problem += pulp.lpSum([sentence_weights[i] * x[i] for i in range(len(sentences))]), "Objective"

    # Constraint: Cover as many keywords as possible
    for j in range(len(keywords)):
        lp_problem += pulp.lpSum([keyword_coverage[i][j] * x[i] for i in range(len(sentences))]) >= 1, f"Keyword_{j}_Coverage"

    # Constraint: Limit the number of selected sentences
    lp_problem += pulp.lpSum([x[i] for i in range(len(sentences))]) <= num_sentences, "Sentence_Limit"

    # Solve the LP problem
    lp_problem.solve()

    # Extract selected sentences
    selected_sentences = [sentences[i] for i in range(len(sentences)) if x[i].varValue == 1]

    # Print the summary
    print("\nSummary:\n")
    for sentence in selected_sentences:
        print(sentence)
        print()
    return selected_sentences

if __name__ == "__main__":
    url = input("Enter the URL: ")
    generate_summary_with_lp(url)
