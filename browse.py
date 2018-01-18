import re
import math
import os
import time
import argparse
import collections
import html
import sys
import random
from csv import reader

hashes = re.compile(r'#')

seed = random.randrange(100)
random.seed(seed)

def urlify(s):
    return re.sub(r'[^a-zA-Z]+','-',s.lower())

def main(stdscr=None):
    global seed
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=None)
    args = parser.parse_args()
    if args.seed:
        seed = args.seed
        random.seed(args.seed)
    cards = []
    card_strings = []
    card_strings.append("---")
    card_strings.append("pagetitle: Flashcards")
    card_strings.append("seed: {}".format(seed))
    card_strings.append("---")
    def add_card(header_stack,body):
        cards.append((header_stack[::-1],body))
    header_stack = []
    with open("flashcards.md",'r+') as f:
        cur_card = None
        body = []
        for line in f:
            if not line:
                continue
            if line.strip().startswith('#'):
                if header_stack and body:
                    add_card(header_stack,body)
                    body = []
                header_level = len(hashes.findall(line))
                header = line.strip()[header_level:].strip()
                header_stack = header_stack[:header_level-1] + [header]
            else:
                body += [line]
        if header_stack and body:
            add_card(header_stack, body)

        random.shuffle(cards)
        if os.path.isfile('gotits.csv'):
            card_gotits = {}
            with open('gotits.csv') as f:
                r = reader(f)
                card_gotits = {q:int(c) for q,c in r}
            cards.sort(key=lambda card: card_gotits[str(card[0])] if str(card[0]) in card_gotits else 0)
        for i,card in enumerate(cards):
            # Build a tree of sections
            titles = card[0]
            title_text = titles[0] + "".join([" ([{}](/#/{}))".format(c,urlify(c))  for c in titles[1:]])
            front_page = "# " + title_text + "\n"
            back_page = "### " + title_text + "\n"+''.join(card[1])+'\n'
            card_strings.append(front_page)
            card_strings.append(back_page)
            card_strings.append(f"""
<form  id="{i}form" target="{i}transFrame" action = "http://127.0.0.1:5000/data" method = "post" ;">
    <input style="font-size:1em;" type="submit" name="{titles}" value="got it" onClick="document.getElementById('{i}form').setAttribute('style','display:none');" />
</form><iframe style="display:none;" name="{i}transFrame" id="{i}transFrame"></iframe>
""")
    print(html.unescape('\n'.join(card_strings)))
main()
