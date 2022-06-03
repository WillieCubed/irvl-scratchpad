# How to Use

1. Download the [Flickr30k](https://shannon.cs.illinois.edu/DenotationGraph/) dataset.
2. Once you receive the email, choose the "Publicly Distributable Version of the
   Flickr 30k Dataset (tokenized captions only)" option on the website.
3. Extract the file with the caption into a `datasets/flickr30k-captions`
   directory that is a sibling to this directory.
4. Run the `language_grounding/noun_extraction.py` script with path to the the Flickr30k captions as a parameter. 
   For example:
    ```bash
    python noun_extraction.py ../datasets/flickr30k-captions/results_20130124.token
    ```