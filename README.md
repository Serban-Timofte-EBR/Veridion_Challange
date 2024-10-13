# Furniture Stores Product Extraction Challenge

## Challenge Overview

The goal of this project is to develop a model that can extract product names from various furniture store websites. We aim to use Named Entity Recognition (NER) techniques to identify and classify product names from the text extracted from the pages of these websites.

### Inputs

You’ll be given a list of URLs from furniture store sites. Some of these pages will have products listed, some may not, and others might be inaccessible or broken.

The provided dataset can be found in the following CSV file:
- [furniture_stores_pages.csv](https://file.notion.so/f/f/5e227651-b0a7-4a7d-93a5-e46562440f31/7eb63a03-791b-4006-bfe9-30753d08d5b3/furniture_stores_pages.csv?table=block&id=1de397a6-25e7-4697-971f-604522fc238d&spaceId=5e227651-b0a7-4a7d-93a5-e46562440f31&expirationTimestamp=1728900000000&signature=nELBQHBBdqeFD34APXUHI-v2GLAfySnQKkVKWa4A4PQ&downloadName=furniture+stores+pages.csv)

### Outputs

The output of this project will be a list of product names extracted from each of the URLs. However, additional insights such as the most popular product, aggregated data from multiple pages, or trends in product names can also be presented.

## Approach

The recommended approach is to build a Named Entity Recognition (NER) model that identifies the 'PRODUCT' entity from the web pages' content. The following steps outline the process:

1. **Crawl ~100 pages** from the provided list of URLs.
2. **Extract the text** from the crawled pages.
3. **Tag some sample products** manually to create labeled training data.
4. **Train an NER model** using a transformer architecture such as BERT from Huggingface or Spark NLP.
5. **Apply the trained model** to new pages and extract product names.
6. **Showcase the solution**, highlighting strengths like identifying trends, extracting the most popular product, etc.

## Tools & Libraries

You are free to use any programming language or tools, but it is recommended to use one of the following:

- **Spark NLP** with Transformer architecture
  - [NER with Spark NLP](https://towardsdatascience.com/named-entity-recognition-ner-with-bert-in-spark-nlp-874df20d1d77)
  
- **Huggingface Transformers**
  - [NER with Huggingface Transformers](https://medium.com/@andrewmarmon/fine-tuned-named-entity-recognition-with-hugging-face-bert-d51d4cb3d7b5)

## Project Structure

1. **Data Crawling and Preprocessing**
   - Crawling and extracting text from furniture store pages.
   - Cleaning and preparing data for tagging.

2. **NER Model Training**
   - Manually tagging products as 'PRODUCT'.
   - Training a transformer-based NER model on the tagged data.

3. **Model Evaluation and Application**
   - Evaluating the model on new, unseen pages.
   - Extracting and presenting product names.

4. **Results and Analysis**
   - Aggregating results and showcasing additional insights such as popular products or trends.
