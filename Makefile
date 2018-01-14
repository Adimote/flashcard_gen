
default: build run

flashcards_out.md: browse.py
	python browse.py > flashcards_out.md

flashcards.html:flashcards_out.md
	pandoc -t revealjs -V revealjs-url=http://lab.hakim.se/reveal-js -s -o flashcards.html flashcards_out.md --slide-level=3
	rm flashcards_out.md

clean:
	rm -f flashcards.html
	rm -f flashcards_out.md

run:
	export FLASK_APP=flaskstuff.py; python -m flask run

build: flashcards.html
