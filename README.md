# Flashcard app

This program generates a random reveal.js slideshow from given flashcards, it records when you remembered a card before you saw it. The next time you generate it will show least-remembered first.

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

3. Run `make` to produce flashcards.html, which you can open in your web browser.

4. To record whether you 'got it', you must also run `make record` in the background while you are reading your flashcards.
