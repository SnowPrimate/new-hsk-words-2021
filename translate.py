from google.cloud import translate_v2 as translator
import six
translator = translator.Client()
new1 = open('new1.txt', encoding="utf8").read().split('\n')
new2 = open('new2.txt', encoding="utf8").read().split('\n')
new3 = open('new3.txt', encoding="utf8").read().split('\n')
new4 = open('new4.txt', encoding="utf8").read().split('\n')
new5 = open('new5.txt', encoding="utf8").read().split('\n')
new6 = open('new6.txt', encoding="utf8").read().split('\n')
new = [new1, new2, new3, new4, new5, new6]

def translate(files):
    text = []
    for word in files:
        translation = translator.translate(word, source_language='zh-CN', target_language='en')
        print(translation)
        a = translation['input'] + "," + translation['translatedText']
        text.append(a)
    return text


file = translate(new[4])
with open(f'trans{5}.txt', 'w',encoding='utf8') as f:
    for item in file:
        f.write("%s\n" % item)
