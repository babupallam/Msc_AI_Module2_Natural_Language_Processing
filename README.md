# MSc AI Module 2: Natural Language Processing (NLP)

This repository contains coursework, research, and hands-on implementations for **MSc AI Module 2: Natural Language Processing (NLP)**. The focus is on deep learning-based NLP techniques, including **Feedforward Neural Networks**, **Recurrent Neural Networks**, **Graph Neural Networks**, and **transformer-based models**, with structured **learning notes, tests, and analyses** accompanying each topic.

---

## Repository Structure

The repository is divided into folders corresponding to lecture topics and projects. Each folder contains:

- **Learning Notes:** Detailed explanations of concepts, algorithms, and methodologies.
- **Code Files:** Jupyter notebooks or Python scripts demonstrating the implementation of the discussed concepts.
- **Tests:** Sample datasets and testing workflows for practical evaluation of models.
- **Analysis Reports:** Results and insights gained from experiments and evaluations.

---

## Folder Descriptions

### 1. **L01-Introduction to Module**
   - **Content:** Overview of NLP concepts and evolution from rule-based systems to deep learning approaches.
   - **Includes:**
     - Learning notes on NLP fundamentals.
     - Analysis of traditional NLP methods versus deep learning techniques.

### 2. **L02-Categorizing and Tagging Words**
   - **Content:** Techniques for parts-of-speech tagging and word categorization.
   - **Includes:**
     - Notebooks for implementing tagging algorithms.
     - Analysis of tagging accuracy on benchmark datasets.
     - Tests comparing different tagging models.

### 3. **L03-Learning to Classify Text**
   - **Content:** Text classification techniques, from feature extraction to model evaluation.
   - **Includes:**
     - Learning notes on classification workflows.
     - Code examples for text preprocessing and feature engineering.
     - Tests using machine learning and neural network classifiers.
     - Analysis reports comparing model performance.

### 4. **L04-Extracting Information from Text**
   - **Content:** Methods for structured information extraction, including Named Entity Recognition (NER) and relationship extraction.
   - **Includes:**
     - Notes on entity extraction and dependency parsing.
     - Implementation of NER models using pre-trained embeddings.
     - Tests on benchmark datasets with performance evaluation.

### 5. **L05-Feedforward Networks for NLP**
   - **Content:** Application of feedforward neural networks in NLP tasks.
   - **Includes:**
     - Learning notes on word embeddings and dense neural networks.
     - Code examples demonstrating the use of embedding layers.
     - Tests on sentiment analysis and similar tasks.
     - Analysis of embedding effectiveness and network performance.

### 6. **L06-Recurrent Neural Networks (RNNs)**
   - **Content:** Sequential data processing with RNNs, LSTMs, and GRUs.
   - **Includes:**
     - Detailed notes on sequence modeling and long-term dependencies.
     - Code implementations for language modeling and text generation.
     - Tests evaluating RNN performance on sequential datasets.
     - Comparative analysis of LSTM vs. GRU performance.

### 7. **L07-Chatbot Based on PyTorch**
   - **Content:** Building an intent-based chatbot using PyTorch.
   - **Includes:**
     - Learning notes on conversational AI workflows.
     - Implementation of chatbot architecture.
     - Tests using predefined intents and user interaction scenarios.
     - Analysis of chatbot accuracy and user experience.

### 8. **L08-NLP From Scratch - PyTorch**
   - **Content:** End-to-end NLP implementation from tokenization to model training.
   - **Includes:**
     - Notes on data pipelines, tokenization, and embedding techniques.
     - Scripts for building and training models from scratch.
     - Tests on sample datasets for classification and sequence labeling.
     - Insights into optimization strategies and challenges.

### 9. **L09-Large Language Models (LLMs)**
   - **Content:** Introduction to transformer-based models like BERT, GPT, and T5.
   - **Includes:**
     - Notes on architecture and pretraining objectives of LLMs.
     - Code examples using the Hugging Face Transformers library.
     - Tests on transfer learning and fine-tuning for downstream tasks.
     - Analysis of LLM effectiveness on specific NLP tasks.

### 10. **L10-Graph Convolutional Networks**
   - **Content:** Graph-based approaches for NLP using GraphSAGE and GIN architectures.
   - **Includes:**
     - Notes on graph representation of text and GNN principles.
     - Implementation of graph-based models for NLP tasks.
     - Tests on datasets with graph-like structures.
     - Analysis of GNN performance and interpretability.

### 11. **Supporting Works/MCQs**
   - **Content:** Supplementary material to enhance understanding.
   - **Includes:**
     - Research papers and references for deeper insights.
     - Multiple-choice questions for self-assessment.
     - Notes on advanced RNN structures, attention mechanisms, and transformer enhancements.

---

## Key Features

- **Comprehensive Notes:** Detailed explanations of theoretical and practical aspects of NLP.
- **Hands-On Practice:** Jupyter notebooks and Python scripts for practical implementation.
- **Testing Workflows:** Predefined tests to evaluate the performance of models and techniques.
- **Analysis Reports:** Insights and findings from experiments, comparing different approaches.
- **Advanced Topics:** Exploration of cutting-edge NLP advancements, including LLMs and GNNs.

---

## Installation and Setup

### Prerequisites

- **Programming Language:** Python 3.8 or higher.
- **Tools and Libraries:**
  - Jupyter Notebook
  - PyTorch 1.8 or higher
  - Hugging Face Transformers
  - Numpy, Pandas, NLTK, Matplotlib, NetworkX

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/babupallam/msc-ai-module2-natural-language-processing.git
   cd msc-ai-module2-natural-language-processing
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the desired folder and open the relevant Jupyter notebook:
   ```bash
   jupyter notebook
   ```

---

## Learning Objectives

- Gain a deep understanding of modern NLP techniques.
- Implement practical NLP workflows using PyTorch and Python.
- Evaluate and analyze NLP models across various benchmarks.
- Explore advanced models like transformers and graph neural networks.
- Develop solutions for real-world challenges in text processing and analysis.

---

## Contributions

- **Author:** Babu Pallam
- **Course Mentor:** Aboozar Taherkhani (aboozar.taherkhani@dmu.ac.uk)

Contributions are welcome! Feel free to open an issue or submit a pull request with suggestions or improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
