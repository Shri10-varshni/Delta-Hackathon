from googletrans import Translator,LANGCODES,LANGUAGES

#Gets a sentence in any language and returns it
def get_sentence():
    snt_to_trans=input("Enter a Sentence : ")
    return snt_to_trans

#Returns the english translated version of the snt_to_trans
def trans_to_en(snt_to_trans):
    translator = Translator()
    translated = translator.translate(snt_to_trans)
    en_text = translated.text
    return en_text

#Finds the language code of snt_to_trans and returns it
def find_lang(snt_to_trans):
    try:
        lang_code_detect=Translator().detect(snt_to_trans)
        return LANGUAGES[lang_code_detect.lang],lang_code_detect.lang
    except:
        return "Sorry! Unable to Find the language of the sentence."    

#Given a sentence, the translated text in trans_lang is returned
def trans_to_any(snt_to_trans, trans_lang):
    translator=Translator()
    translation = translator.translate(text=snt_to_trans, dest=LANGCODES[trans_lang])   
    return translation.text 

#Main Function
def final():
    print("\n", "WELCOME TO TRANSLATOR", "\n")
    snt_to_trans=get_sentence()
    print("Translation in English: ",trans_to_en(snt_to_trans)) 
    print("Detected Language: ",find_lang(snt_to_trans))
    trans_lang=input("Enter preferred language for translation : ").lower()
    print("Translation in ",trans_lang," : ", trans_to_any(snt_to_trans, trans_lang))
    print()

final()

