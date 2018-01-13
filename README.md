# Flashcard app

This program generates a reveal.js style flashcard application, and records the number of times each card is 'gotten', sorting by the most commonly 'got' cards last, but otherwise in a random order.

## Dependencies

- Flask Python3 package
- pandoc

## Installation.

1. Put reveal.js in the correct place:
```bash
wget https://github.com/hakimel/reveal.js/archive/master.tar.gz
tar -xzvf master.tar.gz
mv reveal.js-master reveal.js
```

2. Write your flashcards in `flashcards.md`, there are examples in there. Each heading is translated to a flashcard, subheadings can be used to categorise each card.

3. Run `make` to produce flashcards.html, which you can navigate your web browser to

4. To record your 'Got its' you must also run `make record` in the background while you are reading your flashcards
