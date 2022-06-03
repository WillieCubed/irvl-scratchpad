"""
How to use:

Run the script with the Flickr30k dataset as a parameter. E.g.:
```bash
python language_grounding/noun_extraction.py datasets/flickr30k-captions/results_20130124.token
```
"""
import re
import sys
from sys import argv
from typing import Tuple, List
import spacy
from spacy import displacy

PARSE_REGEX = r'(\w*\.jpg)#([0-9])\s(.*)'

nlp = spacy.load("en_core_web_sm")


def main():
    if len(argv) < 2:
        print("Please provide a filename")
        sys.exit(1)
    filename = argv[1]

    captions = parse_lines(filename)
    for filename, caption_items in captions:
        for caption in caption_items:
            phrases = process_object_phrases(caption)
            print(f'{filename}: {phrases}')


def parse_line(line) -> Tuple[str, int, str]:
    """Return a tuple containing the filename of the photo, the ID of the caption, and the caption."""
    results = re.match(PARSE_REGEX, line)
    filename, caption_number, caption = results.groups()
    return filename, caption_number, caption


def parse_lines(filename: str) -> List[Tuple[str, List[str]]]:
    results = {}
    with open(filename) as f:
        for line in f:
            filename, number, caption = parse_line(line)
            if filename not in results.keys():
                results[filename] = []
            results[filename].append(caption)

    processed_results: List[Tuple[str, List[str]]] = list(results.items())

    return processed_results


def process_object_phrases(line: str):
    """Return a list of noun phrases.

    This uses a naive implementation, but in the future, adjectives """
    doc = nlp(line)
    # displacy.serve(doc, style="dep")

    phrases = []
    for chunk in doc.noun_chunks:
        phrases.append(chunk.text)

    # for i in range(len(doc)):
    #    pass

    return phrases


if __name__ == '__main__':
    main()
