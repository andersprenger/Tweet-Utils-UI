"""
Twitter Sentiment Classifier

    This script is designed to classify tweets based on their sentiment, categorizing them as positive, negative,
    or neutral.

- Authors: Anderson Sprenger, Gustavo Duarte
- Email: anderson.sprenger@edu.pucrs.br
- Date: June 22, 2023

The script utilizes the following classifiers:

- Logistic Regression
- Multinomial Naive Bayes
- Support Vector Machine
"""

import re
from enum import Enum

import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


class Sentiment(Enum):
    """
    Enum os sentimentos a serem classificados nos tweets.
    """

    NEGATIVE = 0
    POSITIVE = 1
    NEUTRAL = 2


class SentimentClassifier:
    """
    Classe com a implementação do classificador de sentimento.
    """

    def __init__(self):
        """
        Construtor da classe com a implementação do classificador de sentimento.
        """

        # Inicializando o tokenizador de tweets...
        self.tweet_tokenizer = TweetTokenizer()

        # Inicializando o stemmer de palavras...
        self.text_stemmer = PorterStemmer()

        # Inicializando os vetorizadores de palavras...
        self.vectorizerPositiveNegative = CountVectorizer(analyzer="word", tokenizer=self.tweet_tokenizer.tokenize)
        self.vectorizerPositiveNeutral = CountVectorizer(analyzer="word", tokenizer=self.tweet_tokenizer.tokenize)
        self.vectorizerNegativeNeutral = CountVectorizer(analyzer="word", tokenizer=self.tweet_tokenizer.tokenize)

        # Inicializando os classificadores...
        self.classifierLRPositiveNegative = LogisticRegression(random_state=0)
        self.classifierMultinomialPositiveNeutral = MultinomialNB()
        self.classifierSVMNegativeNeutral = svm.SVC(kernel='linear')
        self.train_sentiment_classifiers()

    def train_sentiment_classifiers(self) -> None:
        """
        Função para treinar os classificadores de sentimento...
        :return: None
        """

        # Carregando o dataset de treinamento...
        generalTrainingData = pd.read_excel('dataset.xlsx', engine='openpyxl').fillna(' ')

        # Preparando os dados para o treinamento do modelo...
        positiveNegativeTrainData = generalTrainingData[generalTrainingData['SentimentoFinal'] != 0]
        positiveNeutralTrainData = generalTrainingData[generalTrainingData['SentimentoFinal'] != 2]
        negativeNeutralTrainData = generalTrainingData[generalTrainingData['SentimentoFinal'] != 1]

        tweetsForPositiveNegativeTrain = positiveNegativeTrainData['full_text'].values
        tweetsForPositiveNeutralTrain = positiveNeutralTrainData['full_text'].values
        tweetsForNegativeNeutralTrain = negativeNeutralTrainData['full_text'].values

        # Vetorizando os dados de treinamento...
        vectPositiveNegativeTrain = self.vectorizerPositiveNegative.fit_transform(tweetsForPositiveNegativeTrain)
        vectPositiveNeutralTrain = self.vectorizerPositiveNeutral.fit_transform(tweetsForPositiveNeutralTrain)
        vectNegativeNeutralTrain = self.vectorizerNegativeNeutral.fit_transform(tweetsForNegativeNeutralTrain)

        # Obtendo as classes dos dados de treinamento...
        classesPositiveNegativeTrain = positiveNegativeTrainData['SentimentoFinal'].values
        classesPositiveNeutralTrain = positiveNeutralTrainData['SentimentoFinal'].values
        classesNegativeNeutralTrain = negativeNeutralTrainData['SentimentoFinal'].values

        # Treinando os classificadores...
        self.classifierLRPositiveNegative.fit(vectPositiveNegativeTrain, classesPositiveNegativeTrain)
        self.classifierMultinomialPositiveNeutral.fit(vectPositiveNeutralTrain, classesPositiveNeutralTrain)
        self.classifierSVMNegativeNeutral.fit(vectNegativeNeutralTrain, classesNegativeNeutralTrain)

    def preprocess_data(self, data: str) -> str:
        """
        Função para pré-processar os dados...

        - Remove caracteres especiais, números, espaços em branco, pontuação e links.
        - Aplica o stemming.

        :param data: Uma string com o texto do tweet.
        :return: Uma lista de palavras pré-processadas extraídas do texto do tweet.
        """

        # Limpando os dados...
        data = re.sub(r'[^a-zA-Z0-9\s]', '', data)  # Remove caracteres especiais
        data = re.sub(r'\d+', '', data)  # Remove números
        data = re.sub(r'\s+', ' ', data)  # Remove espaços em branco
        data = re.sub(r'[.?!,:;]', '', data)  # Remove pontuação
        data = re.sub(r'http\S+|www\S+|\S+\.com\S+', '', data)  # remove links

        # Preparando os dados para o stemming...
        tokenized_data = self.tweet_tokenizer.tokenize(data)

        # Aplicando o stemming...
        stemmed_data = []
        for word in tokenized_data:
            stemmed_data += [self.text_stemmer.stem(word)]

        return ' '.join(stemmed_data)

    def predict(self, data: str) -> Sentiment:
        """
        Função para classificar os tweets em sentimentos positivo, negativo ou neutro.

        :param data: uma string com o texto do tweet
        :return: o Sentiment encontrado na classificação
        """

        # Preparando os dados para a classificação...
        preprocessed_data = [self.preprocess_data(data)]

        # Vetorizando os dados para a classificação...
        vectPositiveNegative = self.vectorizerPositiveNegative.transform(preprocessed_data)
        vectPositiveNeutral = self.vectorizerPositiveNeutral.transform(preprocessed_data)
        vectNegativeNeutral = self.vectorizerNegativeNeutral.transform(preprocessed_data)

        # Classificando os tweets...
        resultPositiveNeutral = self.classifierMultinomialPositiveNeutral.predict(vectPositiveNeutral)
        resultNegativeNeutral = self.classifierSVMNegativeNeutral.predict(vectNegativeNeutral)
        resultPositiveNegative = self.classifierLRPositiveNegative.predict(vectPositiveNegative)

        # Verificando o resultado da classificação...
        if (resultPositiveNeutral == 0).any() and (resultNegativeNeutral == 0).any():
            return Sentiment.NEUTRAL
        elif (resultPositiveNeutral == 1).any() and (resultPositiveNegative == 1).any():
            return Sentiment.POSITIVE
        elif (resultNegativeNeutral == 2).any() and (resultPositiveNegative == 2).any():
            return Sentiment.NEGATIVE
        else:
            return Sentiment.NEUTRAL
