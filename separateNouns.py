import sys


def run(args = sys.argv[1:]):
    noun_tags = ["NOUN", "PRON", "PROPN"]
    possible_tags = ["ADJ", "NOUN", "PRON", "ADP", "AUX", "NUM", "PART", "VERB", "X", "SYM", "SCONJ", "PUNCT", "PROPN", "INTJ", "DET", "CCONJ", "ADV"]
    file = open(args[0], encoding="utf-8")
    noun_file = open(args[1], "w", encoding="utf-8")
    for line in file:
        line_list = line.split()
        for word in line_list:
            word_tag_list = word.split("/")
            tag = word_tag_list[-1:][0]
            if tag not in possible_tags:
                print("tag not possible: {}".format(tag))
            if tag in noun_tags:
                for part in word_tag_list:
                    noun_file.write(part + " ")
                noun_file.write("\n")





if __name__ == "__main__":
    run()
    pass