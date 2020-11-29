
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
np.random.seed(32)


from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.manifold import TSNE

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Conv1D, MaxPooling1D, Dropout
from keras.utils.np_utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import GlobalAveragePooling1D, Embedding
from keras.models import Model
from keras.models import Sequential
from keras import layers
from keras.layers import SpatialDropout1D
from keras.models import load_model
import keras

from keras.models import Sequential
from keras import layers

g='У нас сегодня акция'
g=pd.Series([g])


base=['From ','Theme','Text','Type','Activity','Akcia','Sber_news','Alerts_from_Sber','Question','Request','Servers']
post = pd.DataFrame( columns = base)

main_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_main')
activ_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_activ2')
money_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_money2')
news_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_news2')
notif_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_notif2')
questions_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_questions2')
req_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_req2')
server_model = keras.models.load_model('D:\Приложения\PostEffectFinal\mail\model_server')


def dew_it(letter):
    MAX_NB_WORDS = 20000
    EMBEDDING_DIM = 100
    MAX_SEQUENCE_LENGTH = 200
    N_CLASSES = 6

    res = []

    letter = letter.astype(str)
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, char_level=False)
    tokenizer.fit_on_texts(letter)
    sequences = tokenizer.texts_to_sequences(letter)
    letter = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

    main = main_model.predict(letter)
    activ = activ_model.predict(letter)
    money = money_model.predict(letter)
    news = news_model.predict(letter)
    notif = notif_model.predict(letter)
    question = questions_model.predict(letter)
    req = req_model.predict(letter)
    server = server_model.predict(letter)

    if ((main[0][0] > main[0][1]) and (main[0][0] > main[0][2]) and (main[0][0] > main[0][3]) and (
            main[0][0] > main[0][4])):
        res.append(0)
    if ((main[0][1] > main[0][0]) and (main[0][1] > main[0][2]) and (main[0][1] > main[0][3]) and (
            main[0][0] > main[0][4])):
        res.append(1)
    if ((main[0][2] > main[0][0]) and (main[0][2] > main[0][1]) and (main[0][2] > main[0][3]) and (
            main[0][2] > main[0][4])):
        res.append(2)
    if ((main[0][3] > main[0][0]) and (main[0][3] > main[0][1]) and (main[0][3] > main[0][2]) and (
            main[0][3] > main[0][4])):
        res.append(3)
    if ((main[0][4] > main[0][0]) and (main[0][4] > main[0][1]) and (main[0][4] > main[0][3]) and (
            main[0][4] > main[0][2])):
        res.append(4)

    if activ[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if money[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if news[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if notif[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if req[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if req[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    if server[0][0] < 0.5:
        res.append(0)
    else:
        res.append(1)

    return res
