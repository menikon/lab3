from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

f = open ("wiki.txt","r")
trainings = [TaggedDocument(words = data.split(),tags = [i]) for i,data in enumerate(f)]

m = Doc2Vec(documents = trainings,dm = 1,vector_size = 100,window = 3,min_count = 1,worker = 4)


m.save("model/doc2vec.model")
m = Doc2Vec.load("model/doc2vec.model")

f.close()


doc_question = open("MeCab_question.txt","r")
doc_choice1 =[ "イニシエーション・ラブ", "同様" ,"最後", "数行", "どんでん返し", "いく", "時", "時", "様々", "シーン", "する" ,"れる", "伏線" ,"散りばめる", "られる" ,"いる", "こと", "気づく"]
doc_choice2 =["ラスト", "展開" ,"早い" ,"他" ,"作品", "衝撃", "受ける" ,"裏の裏" ,"つく","ミステリー"]
doc_choice3 =["独特", "世界観", "日常" ,"離れる","落ち着く","時","読む","本"]
doc_choice4 =["室町","戦国","年"]

print("Q-1 sim")
sim_value = m.docvecs.similarity_unseen_docs(m, doc_question, doc_choice1, alpha=1, min_alpha=0.0001, steps=5)
print(sim_value)

print("Q-2 sim")
print(m.docvecs.similarity_unseen_docs(m, doc_question, doc_choice2, alpha=1, min_alpha=0.0001, steps=5))

print("Q-3 sim")
print(m.docvecs.similarity_unseen_docs(m, doc_question, doc_choice3, alpha=1, min_alpha=0.0001, steps=5))

print("Q-4 sim")
print(m.docvecs.similarity_unseen_docs(m, doc_question, doc_choice4, alpha=1, min_alpha=0.0001, steps=5))
