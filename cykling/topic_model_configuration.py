import os
from sklearn.feature_extraction import text
from nltk.corpus import stopwords

# An import that should function both locally and when running an a remote server
try:
    from environment_configuration import *
except:
    from topics2themes.environment_configuration import *

if RUN_LOCALLY:
    from topic_model_constants import *
    from word2vec_term_similarity import *

else:
    from topics2themes.topic_model_constants import *
    from topics2themes.word2vec_term_similarity import *
    

"""
Nr of topics to retrieve
"""
NUMBER_OF_TOPICS = 25


"""
The topic modelling algorithm is rerun with a decrease number of requested topics
until the number of found stable topics are similar to the ones requested
The amont of similarity is set here.
"""

PROPORTION_OF_LESS_TOPIC_TO_ALLOW = 0.9

"""
Nr of words to display for each topic
"""

NR_OF_TOP_WORDS = 50

"""
Nr of most typical document to retrieve for each topic
"""

NR_OF_TOP_DOCUMENTS = 882

"""
Number of runs to check the stability of the retrieved topics.
Only topics that occur in all NUMBER_OF_RUNS runs will be
considered valid
"""
NUMBER_OF_RUNS = 100


"""
Mininimum overlap of retrieved terms to considered the retrieved topic as
the same topic of a another one
"""
OVERLAP_CUT_OFF = 0.50


"""
Whether to use pre-processing (collocation detection and synonym clustering)
"""
PRE_PROCESS = True

VECTOR_LENGTH = 100
SPACE_FOR_PATH = "/Users/marsk757/wordspaces/69/model.bin"
MAX_DIST_FOR_CLUSTERING = 0.71
WORDS_NOT_TO_INCLUDE_IN_CLUSTERING_FILE = "not_cluster.txt"
MANUAL_CLUSTER_FILE = "manual_clusters.txt"
MANUAL_COLLOCATIONS = "manual_collocations.txt"

"""
Mininimum occurrence in the corpus for a word to be included in the topic modelling
"""
MIN_DOCUMENT_FREQUENCY = 1

"""
Maximum occurrence in the corpus for a term to be included in the topic modelling
"""
MAX_DOCUMENT_FREQUENCY = 0.95

"""
Mininimum occurrence in the corpus for a term to be included in the clustering.
"""
MIN_DOCUMENT_FREQUENCY_TO_INCLUDE_IN_CLUSTERING = 1

"""
The stop word file of user-defined stopiwords to use (Scikit learn stop words are also used)
"""

STOP_WORD_FILE = "legends_stopwords_tilltal.txt"


NUMBER_OF_SENTENCES_IN_SUMMARY = 10

"""
The directories in which data is to be found. The data is to be in files with the ".txt" extension
in these directories. For each directory, there should also be a stance-label and a color associated with
the data
"""

DATA_LABEL_LIST = [{DATA_LABEL: 'cycling', DIRECTORY_NAME: 'cycling', LABEL_COLOR: '#ccad00'}]


TOPIC_MODEL_ALGORITHM = NMF_NAME


MAX_NR_OF_FEATURES = 100000

# Need to do nltk.download('stopwords') to get it to work
STOP_WORD_SET = set(stopwords.words('swedish'))
print("STOP_WORD_SET", STOP_WORD_SET)


SHOW_ARGUMENTATION = False
SHOW_SENTIMENT = False


REMOVE_DUPLICATES = False

BINARY_TF = False

def corpus_specific_text_cleaning(text):
    text = text.replace("cyklings", "cykling-s-")
    text = text.replace("cykling", "-cykling-")
    text = text.replace("cykel", "cykel-")
    text = text.replace("Cykel", "cykel-")
    text = text.replace("pendlar", "-pendlar-")
    text = text.replace("pendling", "-pendling-")
    text = text.replace("bilist", "bilist-")
    text = text.replace("cyklister", "-cyklister")
    text = text.replace("cykel-turistveck", "cykelturistveck")
    text = text.replace("Cykel-turistveck", "Cykelturistveck")
    text = text.replace("Cykel-turistveck", "Cykelturistveck")
    text = text.replace("Cykel-främja", "Cykelfrämja")
    text = text.replace("cykel-främja", "cykelfrämja")
    text = text.replace("infrafrågor", "infra-frågor")
    text = text.replace("infrastruktur", "-infrastruktur-")
    text = text.replace("bilsamhället", "bil-samhället")
    text = text.replace("säkerhetsfrågor", "säkerhets-frågor")
    
    

    return text
    
CLEANING_METHOD = corpus_specific_text_cleaning





