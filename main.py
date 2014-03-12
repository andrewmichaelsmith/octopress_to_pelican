import sys
import glob
import fileinput
import re

REPLACEMENTS = [
    (r"date: '?(.*)'$", r"Date: \1"),
    (r"title: [\"'](.*?)[\"']$", r"Title: \1"),
    (r"categories: ?(.*)$", r"Tags: \1"),
    (r"slug: ?(.*)$", r"Slug: \1"),
]

DELETE = [
    "---"
]
def main():

    if len(sys.argv) < 2:
        sys.exit("Usage: %s directory" % sys.argv[0])


    posts =  glob.glob("%s/*.markdown" % sys.argv[1])

    print "Going to update: %s" % posts

    for post in posts:
        process_post(post)

def process_post(post):
    for line in fileinput.input(post, inplace=True):
        r = repl(line)
        if r:
            print r.rstrip()

def repl(line):

    if line.strip() in DELETE:
        return None

    for r in REPLACEMENTS:
        sub = re.sub(r[0], r[1], line)
        if sub != line:
            return sub
    return line




if __name__ == "__main__":
    main()
