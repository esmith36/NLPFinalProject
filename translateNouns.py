from googletrans import Translator
import sys

def run(args = sys.argv[1:]):
    file = open(args[0], "r", encoding="utf-8")
    translated_file = open(args[1], "a", encoding="utf-8")
    #print(file)
    for i, line in enumerate(file):
        if i < 429:
            continue
        string = ""
        line_list = line.split()
        for part in line_list[:-1]:
            string = string + " " + part
        # print(string)
        translator = Translator()
        translated_string = translator.translate(string)
        translated_file.write(string + " " + translated_string.text + "\n")
        print(i)
    return


if __name__ == "__main__":
    run()
    pass