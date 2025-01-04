**Summary Generator: Set Cover Problem Using Greedy Approximation Algorithm**

**Project Overview**

This project develops a text summarization tool based on the Set Cover problem using greedy approximation algorithms and linear programming. The tool efficiently extracts key information from lengthy texts to generate concise summaries, enabling quick and easy information retrieval.

**Problem Statement**

With the vast amount of text available online, manually summarizing documents is time-consuming and inefficient. This project addresses the need for an automated tool to:

- Quickly identify and extract important sentences.

- Ensure coverage of key information without redundancy.

**Proposed Solution**

The tool uses:

Greedy Approximation Algorithm: Selects sentences covering maximum keywords iteratively.

Linear Programming Approach: Optimizes sentence selection based on keyword relevance.

TF-IDF: Extracts important keywords for sentence scoring.

**Key Features**

- Fetches text from URLs for processing.
- Supports keyword extraction using TF-IDF.
- Generates summaries using:

1. Greedy Approximation Algorithm.

2. Linear Programming Approach.

- Compares the two approaches in terms of execution time and accuracy using visualizations.

**File Descriptions**

1. summary_greedy.py - Implements the greedy algorithm for text summarization based on keyword coverage.
2. summary_linear_prog.py - Implements linear programming for optimized sentence selection.
3. summary_generator.py - Combines keyword extraction and summary generation.
4. greedy_vs_linear.py - Compares greedy and linear programming approaches with visualizations.

**Setup Instructions**

1. Clone the repository:

git clone <repository-url>
cd <project-folder>

2. Install dependencies:

pip install -r requirements.txt

3. Run the greedy summarizer:

python summary_greedy.py

4. Run the linear programming summarizer:

python summary_linear_prog.py

5. Compare the two approaches:

python greedy_vs_linear.py

**Requirements**

- Python 3.8+

- Libraries:

>  nltk

> numpy

> pulp

> requests

> beautifulsoup4

> matplotlib

> scipy

**How It Works**

1. Input a URL containing the text to be summarized.
2. The tool fetches and preprocesses the text.
3. Keywords are extracted using TF-IDF.
4. Sentences are selected based on coverage of keywords using greedy or linear programming.
5. The summary is displayed, and performance comparisons are visualized.
