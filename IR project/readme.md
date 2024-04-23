# Integrated Web Document Crawling and Search System Using Scrapy, Scikit-Learn, and Flask

## Abstract:

This project provides a concise Flask, Scikit-Learn, and Scrapy solution for web document search and retrieval. By combining a quick Scrapy crawler, a powerful Scikit-Learn indexer, and an easy-to-use Flask processor, users may quickly retrieve relevant online information using free-text queries. The architecture of the system makes sure that all of its parts communicate with each other without any problems, providing a dependable tool for web document searching and scraping. Though it performs well, there are still issues to be resolved, like scalability and indexing accuracy. All things considered, this well-coordinated method offers a promising framework for improving web document retrieval and search capabilities.


## Overview:
This document provides documentation of a viable solution for a web crawling and search system that utilizes Scrapy, Scikit-Learn, and Flask. The system comprises a Scrapy-based crawler designed for fast and efficient web document retrieval, a Scikit-Learn-based indexer for generating an inverted index, and a Flask-based processor for handling users' textual queries.

## Relevant Literature:
- [Yin et al., 2018](#biblio1): Proposes a research on a Scrapy-based distributed crawler system for semi-structured information crawling at high speed.
- [Bengfort et al., 2018](#biblio2): Provides insights into using machine learning for language-sensitive data products, relevant to the system's indexer component.
- [Copperwaite and Leifer, 2015](#biblio3): Offers complete coverage of the Flask Framework, useful for developing the system's processor.

## Proposed System:
The proposed solution integrates data from various sources to develop a web document scraping and searching tool. It includes a Scrapy-based crawler for extracting web documents, a Scikit-Learn-based indexer for efficient indexing, and a Flask-based processor for querying documents.

## Design:
The system's core competencies facilitate effective web document search. The Scrapy-based web-crawling module downloads HTML pages, while the Scikit-Learn-built indexer constructs an inverted index for faster and more precise search. The Flask integration allows users to ask free-text questions and receive top-ranking search results.

## Architecture:
The system consists of three main components: 
1. Scrapy-based crawler
2. Scikit-Learn-based indexer
3. Flask-based processor
These components interact via well-defined interfaces to enable efficient web document retrieval and search.

## Operation:
To utilize the system:
1. Build a virtual environment using Python's venv module.
2. Install dependencies from requirements.txt using pip install -r requirements.txt.
3. Launch the system with python app.py.
Users can then input queries and receive top-ranking search results.

## Execution
export FLASK_APP=app.py
flask run

## Conclusion:
The developed system achieves optimal crawling and search capabilities on web documents. However, challenges such as incomplete or inaccurate indexing and scalability issues may arise. Users should exercise caution when relying solely on search results.

## Data Sources:
Web crawling data was sourced from [books.toscrape.com](https://books.toscrape.com/), providing content for indexing and searching.

## Test Cases:
Unit tests were conducted using Python's unittest framework to ensure the system's robustness and consistency.

## Source Code:
The project's source code, which provides thorough documentation and an ordered structure for simple understanding and modification, is a monument to openness and adaptability. It is dependable and efficient, utilising key open-source tools like Scikit-Learn, Flask, and Scrapy. The codebase promotes transparency and reproducibility through careful organisation and adherence to best practices, providing a strong framework for further development.

## Bibliography
1. <a name="biblio1"></a> F. Yin, X. He, and Z. Liu, "Research on scrapy-based distributed crawler system for crawling semi-structure information at high speed," in 2018 IEEE 4th International Conference on Computer and Communications (ICCC), pp. 1356-1359, IEEE, December 2018.
2. <a name="biblio2"></a> B. Bengfort, R. Bilbro, and T. Ojeda, Applied text analysis with Python: Enabling language-aware data products with machine learning. "O'Reilly Media, Inc.", 2018.
3. <a name="biblio3"></a> M. Copperwaite and C. Leifer, Learning Flask Framework. Packt Publishing Ltd., 2015.
