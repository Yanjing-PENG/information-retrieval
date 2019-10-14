# -*- encoding：utf-8 -*-

"""
Student Name: PENG, Yanjing
Student ID: 20656233
Email: ypengaw@connect.ust.hk
Environment: python 3.0 or above

"""
import os
import string
import math
import numpy as np

class InfoRetrieval(object):

    def __init__(self):
        self.N = 0
        self.query = None
        self.forward_index = {}
        self.inverted_index = {}
        self.tf = {}
        self.tf_tfmax_idf = {}
        self.magnitude = {}
        self.score = {}
        self.synonym = []

    # preprocess the passage
    def preprocess(self, passage):

        # remove all punctuation marks
        tem = ''.join(c for c in passage if c not in string.punctuation)

        # remove all spaces
        tem = tem.split(' ')

        # remove words that have less than 4 characters
        target = []
        for i in tem:
            if len(i) >= 4:
                target.append(i)

        # remove ending's' from a word
        result = []
        for i in target:
            if i[-1] == 's':
                result.append(i[:-1])
            else:
                result.append(i)

        return result

    # input the query by users
    def get_query(self, sentence):
        self.query = sentence.split(' ')

    def get_synonym(self, path):
        file = open(path)
        for line in file:
            self.synonym.append(line.strip('\n').split(' '))

    # get forward index
    def get_forward_index(self, collection_path):
        file = open(collection_path, 'r')
        i = 1
        for line in file:
            line = line.strip('\n')
            if line != '':
                self.forward_index['D' + str(i)] = self.preprocess(line)
                i = i + 1
        self.N = i - 1

    # get inverted index
    def get_inverted_index(self):

        # get the vocabulary
        vocabulary = []
        for i in self.forward_index.keys():
            vocabulary = vocabulary + self.forward_index[i]
        vocabulary = list(set(vocabulary))

        # initialize the inverted index
        for term in vocabulary:
            self.inverted_index[term] = {}

        # loop basing on documents
        for d in self.forward_index.keys():
            for i in range(len(self.forward_index[d])):
                term = self.forward_index[d][i]
                if d in self.inverted_index[term].keys():
                    self.inverted_index[term][d].append(i)
                else:
                    self.inverted_index[term][d] = [i]

    # get tf for each document
    def get_tf(self):
        for d in self.forward_index.keys():
            self.tf[d] = {}
            for i in set(self.forward_index[d]):
                self.tf[d][i] = len(self.inverted_index[i][d])

    # get tf/tfmax*idf for each document
    def get_tf_tfmax_idf(self):
        for d in self.tf.keys():
            self.tf_tfmax_idf[d] = {}
            tfmax = max(self.tf[d].values())
            for i in self.tf[d].keys():
                self.tf_tfmax_idf[d][i] = self.tf[d][i] / tfmax * math.log2(self.N / len(self.inverted_index[i]))

    # get magnitude for each document
    def get_magnitude(self):
        for d in self.tf_tfmax_idf.keys():
            self.magnitude[d] = math.sqrt((np.array(list(self.tf_tfmax_idf[d].values())) ** 2).sum())


    # retrieve the documents according the query
    def retrieval(self):
        for q in self.query:
            if q in self.inverted_index.keys():
                for d in self.inverted_index[q].keys():
                    if d in self.score.keys():
                        self.score[d] += self.tf_tfmax_idf[d][q]
                    else:
                        self.score[d] = self.tf_tfmax_idf[d][q]

        if len(self.score) == 0:
            # use synonymic words to alternate the original query word
            self.get_synonym(os.getcwd() + '/data/' + 'synonym.txt')
            for item in self.synonym:
                if set(self.query).intersection(set(item)):
                    self.query = list(set(self.query).union(set(item)))
                    return self.retrieval()
            print('No passage matches the query!')
            return None

        else:
            for d in self.score.keys():
                self.score[d] = self.score[d] / (math.sqrt(len(self.query)) + self.magnitude[d])

            res = sorted(self.score.items(), key=lambda d: d[1], reverse=True)
            if len(res) < 3:
                print('Only %d passage(s) match(es) the query!' % len(res))
                return [k[0] for k in res]
            else:
                return [res[k][0] for k in range(3)]

    # display a document
    def display(self, DID):
        print('--------------------------------------------------------')
        print(DID)
        print('First 5 keywords of the document and the posting lists')
        tem = sorted(self.tf_tfmax_idf[DID].items(), key=lambda d: d[1], reverse=True)
        for i in range(5):
            print(tem[i][0], '-> |', self.inverted_index[tem[i][0]])
        print('\n')
        print('Number of unique keywords in document: %d' % len(self.tf[DID]))
        print('Magnitude of the document vector(L2 norm): %f' % self.magnitude[DID])
        print('Similarity score: %f' % self.score[DID])

