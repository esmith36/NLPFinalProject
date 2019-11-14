import sys


def run(args = sys.argv[1:]):
    tags = []
    file = open(args[0], encoding="utf-8")
    for line in file:
        line_list = line.split()
        tag = line_list[1]
        if tag not in tags:
            tags.append(tag)
    print(tags)



if __name__ == "__main__":
    run()
    pass