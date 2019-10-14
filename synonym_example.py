# -*— encoding : utf-8 -*-

from info_retrieval import InfoRetrieval

info_retrieval = InfoRetrieval()
info_retrieval.get_forward_index('collection.txt')
info_retrieval.get_inverted_index()
info_retrieval.get_tf()
info_retrieval.get_tf_tfmax_idf()
info_retrieval.get_magnitude()


sentence = "corporation"
info_retrieval.get_query(sentence)
res = info_retrieval.retrieval()
print('\n' + '**** When query is:', sentence, '****')
for d in res:
    info_retrieval.display(d)
