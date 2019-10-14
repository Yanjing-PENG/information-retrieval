# -*— encoding : utf-8 -*-

import os
from info_retrieval import InfoRetrieval

info_retrieval = InfoRetrieval()
info_retrieval.get_forward_index(os.getcwd() + '/data/' + 'collection.txt')
info_retrieval.get_inverted_index()
info_retrieval.get_tf()
info_retrieval.get_tf_tfmax_idf()
info_retrieval.get_magnitude()

query_file = open(os.getcwd() + '/data/' + 'query.txt')
for line in query_file:
    info_retrieval.get_query(line.strip('\n'))
    res = info_retrieval.retrieval()
    print('\n' + '**** When query is:', line.strip('\n'), '****')
    for d in res:
        info_retrieval.display(d)
