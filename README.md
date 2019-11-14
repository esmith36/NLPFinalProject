# 1.  make this code work for me
Added encoding="utf-8" to each place where open file

# 2. create the POS tagged data with the following commands, might need to use different DICTs?
Russian:
(base) C:\Users\emory\PycharmProjects\NLP\Project\RDRPOSTagger\pSCRDRtagger>python RDRPOSTagger.py tag ../Models/ud-treebanks-v2.4/UD_Russian-GSD/ru_gsd-ud-train.conllu.UPOS.RDR ../Models/ud-treebanks-v2.4/UD_Russ
ian-GSD/ru_gsd-ud-train.conllu.UPOS.DICT ../data/Russian/rus-ge_web_2017_10K-sentences.txt

Arabic:
(base) C:\Users\emory\PycharmProjects\NLP\Project\RDRPOSTagger\pSCRDRtagger>python RDRPOSTagger.py tag ../Models/ud-treebanks-v2.4/UD_Arabic-PADT/ar_padt-ud-train.conllu.UPOS.RDR ../Models/ud-treebanks-v2.4/UD_Ara
bic-PADT/ar_padt-ud-train.conllu.UPOS.DICT ../data/Arabic/ara-ae_web_2017_10K-sentences.txt

German:
(base) C:\Users\emory\PycharmProjects\NLP\Project\RDRPOSTagger\pSCRDRtagger>python RDRPOSTagger.py tag ../Models/ud-treebanks-v2.4/UD_German-GSD/de_gsd-ud-train.conllu.UPOS.RDR ../Models/ud-treebanks-v2.4/UD_Germa
n-GSD/de_gsd-ud-train.conllu.UPOS.DICT ../data/German/deu-com_web_2018_10K-sentences.txt

Spanish:
(base) C:\Users\emory\PycharmProjects\NLP\Project\RDRPOSTagger\pSCRDRtagger>python RDRPOSTagger.py tag ../Models/ud-treebanks-v2.4/UD_Spanish-AnCora/es_ancora-ud-train.conllu.UPOS.RDR ../Models/ud-treebanks-v2.4/U
D_Spanish-AnCora/es_ancora-ud-train.conllu.UPOS.DICT ../data/Spanish/spa-ad_web_2017_10K-sentences.txt

Hindi:
(base) C:\Users\emory\PycharmProjects\NLP\Project\RDRPOSTagger\pSCRDRtagger>python RDRPOSTagger.py tag ../Models/ud-treebanks-v2.4/UD_Hindi-HDTB/hi_hdtb-ud-train.conllu.UPOS.RDR ../Models/ud-treebanks-v2.4/UD_Hind
i-HDTB/hi_hdtb-ud-train.conllu.UPOS.DICT ../data/Hindi/hin-in_web_2015_10K-sentences.txt

# 3. figure out which tags are nouns


