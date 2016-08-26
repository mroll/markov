import sys
import re
import random

random.seed()


def getwords(filename):
    with open(filename, 'r') as fp:
        content = fp.read().replace('\n', ' ').replace('\t', ' ').replace('\r', '').replace('.', ' .').split(' ')
        return filter(lambda x: x is not '', content)

def probabilities(words, sliderlen=2):
    wordmap = {}
    for i in range(len(words)-sliderlen):
        current = tuple(words[i:i+sliderlen])
        next    = words[i+sliderlen]
        if wordmap.has_key(words[i]):
            wordmap[current]['freq']     += 1

            if wordmap[current]['transitions'].has_key(next):
                wordmap[current]['transitions'][next] += 1
            else:
                wordmap[current]['transitions'][next] = 1
        else:
            wordmap[current] = {}
            wordmap[current]['transitions'] = {next : 1}
            wordmap[current]['freq'] = 1

    return wordmap

def next_func(word, wordmap):
    transitions = wordmap[word]['transitions']
    sorted_transitions = sorted(transitions.keys(), key=lambda x: transitions[x])
    occurrences = float(wordmap[word]['freq'])

    def nexter():
        prob = random.uniform(0, 1)
        ceiling = 0
        
        for x in sorted_transitions:
            if ceiling <= prob and prob < ceiling  + transitions[x]/occurrences:
                return x
            ceiling += transitions[x]/occurrences

    return nexter

def populate_next_functions(wordmap):
    for word in wordmap:
        wordmap[word]['next'] = next_func(word, wordmap)

def sentence(wordmap):
    startword = wordmap.keys()[random.randint(0, len(wordmap.keys()))]
    sliderlen = len(startword)
    maxiter = 37 + random.randint(-5, 5)
    words = [x for x in startword]
    current = wordmap[startword]['next']()

    i = 0
    while current is not '.' and i < maxiter:
        words.append(current)
        current = wordmap[tuple(words[-sliderlen:-1] + [current])]['next']()
        i += 1

    return ' '.join(words)

def paragraph(wordmap):
    sentences = []
    n = 7 + random.randint(-3, 3)
    
    for i in range(n):
        sentences.append(sentence(wordmap))

    return '. '.join(capitalize(sentences)) + '.'
    
def capitalize(sentences):
    return [s[0].title() + s[1:] for s in sentences]
        
def linewrap(string, tw=72):
    formatted = []
    i = col = 0

    while i < len(string):
        if col > tw:
            while string[i] is not ' ':
                i -= 1
                formatted.pop()
                
            i += 1
            formatted.append('\n')
            col = 0

        formatted.append(string[i])
        col += 1
        i += 1
            
    return ''.join(formatted)
                    
        

words = []
for file in sys.argv[1:]:
    words += getwords(file)
    
wordmap = probabilities(words, sliderlen=2)
populate_next_functions(wordmap)

paras = '\n\n'.join([paragraph(wordmap) for i in range(3)])

print linewrap(paras)
