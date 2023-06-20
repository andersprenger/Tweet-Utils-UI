"""
Twitter Sentiment Classifier

Authors: Anderson Sprenger, Gustavo Duarte
Email: anderson.sprenger@edu.pucrs.br
Date: June 19, 2023

This script is designed to classify tweets based on their sentiment, categorizing them as positive, negative, or neutral.

The script utilizes the following classifiers:
- Logistic Regression
- Multinomial Naive Bayes
- Support Vector Machine
"""

from enum import Enum

import pandas as pd
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
        tweet_tokenizer = TweetTokenizer()

        # Inicializando os vetorizadores de palavras...
        self.vectorizerPositiveNegative = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)
        self.vectorizerPositiveNeutral = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)
        self.vectorizerNegativeNeutral = CountVectorizer(analyzer="word", tokenizer=tweet_tokenizer.tokenize)

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

    def predict(self, data: [str]) -> Sentiment:
        """
        Função para classificar os tweets...
        :param data: um [str] com o texto do tweet
        :return: o Sentiment encontrado na classificação
        """

        # Vetorizando os dados para a classificação...
        vectPositiveNegative = self.vectorizerPositiveNegative.transform(data)
        vectPositiveNeutral = self.vectorizerPositiveNeutral.transform(data)
        vectNegativeNeutral = self.vectorizerNegativeNeutral.transform(data)

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
