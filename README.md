Parallel corpora for 6 Indian languages created on Mechanical Turk 
==================================================================

This directory contains data sets for Bengali, Hindi, Malayalam, Tamil, Telugu, and Urdu.
Each data set was created by taking around 100 Indian-language Wikipedia pages and obtaining four independent translations of each of the sentences in those documents.
The procedure used to create them, along with descriptions of initial experiments, is described in:

> [Constructing Parallel Corpora for Six Indian Languages via Crowdsourcing](http://www.aclweb.org/anthology/W12-3152). 2012.
> Matt Post, Chris Callison-Burch, and Miles Osborne.
> Proceedings of the NAACL Workshop for Statistical Machine Translation (WMT).

The PDF and BibTeX files are in the doc/ directory.

The corpora are organized into directories by language pairs:

    bn-en/		Bengali-English
    hi-en/		Hindi-English
    ml-en/		Malayalam-English
    ta-en/		Tamil-English
    te-en/		Telugu-English
    ur-en/		Urdu-English

Within each directory, you'll find the following files:

    PAIR/
       PAIR.metadata
       dict.PAIR.{LANG,en}
       training.PAIR.{LANG,en,seg_ids}
       dev.PAIR.{LANG,en.{0,1,2,3},seg_ids}
       devtest.PAIR.{LANG,en.{0,1,2,3},seg_ids}
       test.PAIR.{LANG,en.{0,1,2,3},seg_ids}
       votes.LANG

The metadata file is organized into rows with four columns each.
The rows correspond to the original documents that were translated, and the colums denote (1) the (internal) segment ID assigned to the document (2) the document's original title (3) a translation of the title (4) the manual category assignment we assigned to the document.
The data splits were constructed by manually assigning the documents to one of eight categories (Technology, Sex, Language and Culture, Religion, Places, People, Events, and Things), and then selecting about 10% of the documents in each category for dev, devtest, and test data (that is, roughly 30% of the data), and the remaining for training data.
Corresponding to each split is a file containing the segment ID of each sentence.
The segment ID identifies the original document ID and the sentence number within that document.
A metadata file in each directory matches between document IDs, Wikipedia page name, a corresponding English translation, and the manual categorization.

The dictionaries were created in a separate MTurk job.
We suggest that you append them to the end of your training data when you train the translation model (as was done in the paper).

The votes files contain the results from a separate MTurk task wherein new Turkers were asked to vote on which of the four translations of a given sentence was the best.
We have such information for all languages except Malayalam.
The format of the votes file is:

> seg_id num_votes sentence votes [sentence votes ...]

Since the data was created by non-expert translators hired over Mechanical Turk, it's of mixed quality.
However, it should be useful enough to get you started training models.
You can download it [from Github](https://github.com/joshua-decoder/indian-parallel-corpora).

In addition, there are some scripts in the scripts/ that manipulate the data in various ways.
