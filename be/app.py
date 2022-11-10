
from flask import Flask
from flask import jsonify
import random
from translate import Translator

from kbbi import KBBI
# from kbbi import TidakDitemukan

app = Flask(__name__)
from translate import Translator
translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")

# import time
# from flask import g

# @app.before_request
# def before_request():
#     g.start = time.time()

# @app.after_request
# def after_request(response):
#     diff = time.time() - g.start
#     if ((response.response) and
#         (200 <= response.status_code < 300) and
#         (response.content_type.startswith('text/html'))):
#         response.set_data(response.get_data().replace(
#             b'__EXECUTION_TIME__', bytes(str(diff), 'utf-8')))
#     print(bytes(str(diff), 'utf-8'))
#     return response


def getWord():
 with open('word.txt') as file:
    f = file.read()
    words = list(map(str, f.split()))
    en = random.choice(words)
    return en

def getQuestion():
    en = getWord()
    translator= Translator(to_lang="id")
    id = translator.translate(en)
    result = KBBI(id)
    return {
        'en' : en,
        'id' : id,
        'kbbi' : result.__str__(),
    }

@app.route('/learn')
def learn():
    list_question = []
    for num in range(0,5):
        list_question.append(getQuestion())
    return jsonify(list_question)

@app.route('/list-random-word=<nnn>')
def listRandomWord(nnn):
    list = []
    for num in range(0, int(nnn)):
        list.append(getWord())
    return jsonify(list)



if __name__ == "__main__":
  app.run()