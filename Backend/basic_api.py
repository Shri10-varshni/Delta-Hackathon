from language_translator import find_lang, trans_to_en
from flask import jsonify,request,Flask

index_request_count=0
app = Flask(__name__)

index_request_count=0
@app.route('/index', methods=['GET'])
def task1():
    global index_request_count
    if(request.method == 'GET'):
        index_request_count=index_request_count+1
        data = {"Response": "Hello World", "Times-requested":index_request_count}
        return jsonify(data)

@app.route('/detect',methods=['GET','POST'])
def detection():
    snts=request.form.get("Sentence: ")
    detected_lang,lang_name=find_lang(snts)
    data={"Detected-Lang":detected_lang, "Lang-Name":lang_name,"Source-text":snts}
    return jsonify(data)

@app.route('/translate',methods=['GET','POST'])
def translation():
    snts=request.form.get("Sentence: ")
    eng_sent=trans_to_en(snts)
    data={"English":eng_sent,"Source-text":snts}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)       


  