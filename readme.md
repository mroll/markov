# markov

This script computes text using a markov chain process. Given text files
as command line arguments, it builds a hash table with info about what
words follow what sequences of words and how often. The script has
functions that easily allow you to get back sentences and paragraphs of
markov generated text.

## examples

Here are a few examples:

    matt@fitz ~/s/p/markov ∂ python markov.py txt/jefferson.txt

    Committee, however, insisted on any matter whatever, be it ever so new or
    difficult, if he does not prohibit exportation of arms, ammunition, &c .,
    but leaves them to be confiscated, if seized, 558, 560. At Europe be as
    little can either enrol them in the courts, 538, 540, 541, 585. No just
    cause of war, 387. Producing any proof. Immediately wrote circular
    letters to you the enclosed pamphlet. Adieus, to his appointment, 329.
    January 17, 1792.

    ----------

    matt@fitz ~/s/p/markov ∂ python markov.py txt/plague.txt txt/alien3a.txt txt/commandments.txt

    Take as follows. Times they would have already begun to change.
    Communicate itself, but if it did, and if they are not of that type
    already, even when thou desirest to make thy program may be long even
    though the days of thy current machine be short. The guard, with 'Who
    comes there?' these could hear the audience cheering in my head as I
    read this scene).

    ----------

    matt@fitz ~/s/p/markov ∂ python markov.py txt/plague.txt txt/alien3a.txt txt/b5quotes.txt

    ." "'Indisposed'! She's in a position to bargain, G'Kar ." "Neither are
    you. Faith for a little while, in a position to bargain, G'Kar ."
    "Neither are you. . Strange, that a human in his last moments should be
    more of a fanatical few who have endangered the lives of our citizens,
    Clarke proclaimed today a planetary holiday. Means they died by heaps,
    that is your final chance for redemption ." "I can not have an aide who
    will not look up. Better bestowed. Me that ye make such piteous
    lamentations as often moved the hearts of the Wolf "Words have meaning
    and names have power ." Lorien, Falling Toward Apotheosis There lies the
    port; the vessel puffs her sail; There gloom the.
