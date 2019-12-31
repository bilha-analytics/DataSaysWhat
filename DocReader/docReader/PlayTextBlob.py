from textblob import TextBlob
import nltk

from nltk.book import text2, text4


# putting it into a function to get count vocab and % vocab in full text
def lexical_diversity(text):
    return( len(set(text)), (len(set(text))/len(text) )  )

def nltk_base_books():
    # get context of word
    text2.concordance( "monstrous" ) 
    text2.similar( "monstrous" ) 
    text2.common_contexts( ["monstrous", "very"]) 

    # position of word - dispersion plot
    text4.dispersion_plot( ["citizens", "democracy", "freedom", "duties", "America"])

    # generate random text from a book
    text2.generate()

    # counting vocabulary in a text
    len( text2 ) # count all words and puntuatations; i.e. count tokens 
    len( set(text2) )  # count uniques; i.e. count vocab or word types
    sorted( set(text4 ) ) # sorted list of vocab or word types 
    len( set(text2) ) / len( text2 )  # measure of lexical richness of the text
    text2.count( "pretty" ) # specific word count
    text2.count( "pretty" ) / len( text2 ) # specific word count as % of full text

    # indexing -- equiv( py lists)
    text2[123]
    text2.index( "pretty" )
    text2[0: 15]

    # string ops as usual
    "the quick brown fox".split()
    " === ".join( text2[:20] ) 
    "Hello " * 3 
    # etc @ py string and list operations 


def lang_stats():
    sent = "The quick brown fox jumped over the lazy dogs!"
    tokenz = sent.split()  
    vocabz = set( tokenz )

    ## A. Word frequency distributions 
    fq = FreqDist( text2 )
    # 1. most common
    fq.most_common( 10 ) # top 10 
    fq[ "pretty" ] 
    fq.freq( "pretty" ) # as a % 
    fq.plot( 10, cumulative=True) # plot top 10 , at this point the top of the list is still a lot of en_lang plumbing    #
    # 2. rare words ; called hapaxes 
    fq.hapaxes() # simple list dump; no tallies or such in this output
    # 3. selection by word length 
    [ w for w in set(text2) if len( w) > 15 ]  # all words in vocab of text2 that are longer than 15 characters; still just a list and not a list so duplicates are possible
    [ w for w in set(text2) if len( w) > 7  and fq[w] > 10 ]  # and now iff frquency of word > some value 
    # can use other string conditions e.g. is upper, is alphanum, starts with, etc << see string functions 

    # ditto without being case-sensitive and counting actual words only
    true_vocab = [ w.lower() for w in set(text2) if w.isalpha() ] 



    ## B. Grams and Co-locations
    # collocations are words that occur together unusually often and synonym subs don't deal. Bigrams as a way to access them 
    bigramz = list( bigrams(text2) ) 
    colocz = text2.collocation_list() #text2.collocations()


    ## C. Word-length frequency distribution 
    fq = FreqDist( [ len(w) for w in set(text2) ] ) 
    fq.max()   # sample with greatest count 
    fq.freq( 2 ) # fq of '2' 
    fq.tabulate() # table all 
    fq.plot( ) # plot all 
    # further analysis of word-length may bring out differences between author, genres, languages 
