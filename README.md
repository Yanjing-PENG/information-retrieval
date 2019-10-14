##  information-retrieval
A full-text information retrieval system basing on Vector Space Model.

### Illustration about data structures

- 'query' is a _**list**_ type in python.

- 'forward_index' is a **_dictionary_** type in python; the keys are DID; the values are **_list_** type where every element is a term of the document.

- 'inverted_index' is a _**dictionary**_ type in python; the keys are index terms; the values are **_dictionary_** type where the keys are DID and the values are **_list_** type where every element is a position of the term in the document.

- 'tf' is a **_dictionary_** type in python; the keys are DID; the values are _**dictionary**_ type where the keys are terms and the values are occurrence frequencies.

- 'tf_tfmax_idf' is a _**dictionary**_ type in python; the keys are DID; the values are _**dictionary**_ type where the keys are terms and the values are tf/tfmax*idf.

- 'magnitude' is a **_dictionary_** type in python; the keys are DID; the values are magnitude (L2 norm) of the document.

- 'score' is a _**dictionary**_ type in python; the keys are DID; the values are cosine similarity of the document.

- 'synonym' is a _**list**_ type in python where every element is _**list**_ type to store synonymic terms.

### Execution

- python main.py (python 3.0 or above)

### Synonym issue

When the Information Retrieval System returns nothing about a query, the system makes a new query by referring to the synonymic words database and tries to provide relevant information about the original query.