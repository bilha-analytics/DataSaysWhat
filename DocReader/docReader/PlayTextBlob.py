from textblob import TextBlob
import nltk

from nltk.book import text2, text4

# corpora
from nltk.corpus import gutenberg, webtext, nps_chat, brown, reuters, inaugural, udhr, PlaintextCorpusReader


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
    true_vocab = set( w.lower() for w in set(text2) if w.isalpha() )



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


def nltk_chatbot():
    ## nltk primitive dialog system <<< word sense disambiguation, verb target, biz logi reasoning .....
    nltk.chat.chatbots()


def nltk_corpora():
    ## 1. PROJECT GUTENBERG << Formal Language - Literature;ebooks 60K++
    emma = nltk.corpus.gutenberg.words( "austen-emma.txt") 
    emma = nltk.Text( emma ) 

    len( emma ) 
    lexical_diversity(emma) 

    emma.concordance( "brave" ) 
    emma.collocation_list()

    ## traits of the corpus text for each
    def corp_content( corporad):
        print( "{0} File {0} \t\tWord len   Sent len   Vocab   Lexical Complexity".format( " "*6  ) )
        print( "{}".format("-"*100))
        for i, txt in enumerate( corporad.fileids() ):
            sents_l = len( corporad.words( txt ) )
            try:
                sents_l = len( corporad.sents( txt ) ) 
            except:
                sents_l = len( corporad.posts( txt ) )
            w_len = round( len( corporad.raw( txt ) ) / len( corporad.words( txt ) ) ) 
            s_len = round( len( corporad.words( txt ) ) / sents_l )
            voc = len( set( w.lower() for w in corporad.words(txt) ) ) 
            # lexp = round( voc / len( [w.lower() for w in gutenberg.words(txt)] ) * 100 ) 
            lexp = round( voc / len( corporad.words(txt) ) * 100 ) 
            print( "{}. {} \t\t{}\t{}\t{}\t{}%\t{}".format(i, txt, w_len, s_len, voc, lexp, corporad.raw(txt)[:30] ) )
            # print( "{}. {} \t\t{}\t{}\t{}\t{}%\t{}".format(i, txt, w_len, s_len, voc, lexp, corporad.words(txt)[:5] ) )
    
    # 1. Formal Language - Project Gutenberg ebooks 60K++, 16+ languages 
    corp_content( gutenberg ) 

    # 2. Informal Language - Web content and Chat rooms 
    corp_content( webtext )
    corp_content( nps_chat )  

    # 3. Brown Corpus - 15+ Multi-genre, 500+ sources, En_lang << http://icame.uib.no/brown/bcm-los.html 
    # for studying systematic differences between genres I.E. stylistics
    corp_content( brown )  

    brown.categories()
    brown.words( categories="news")
    brown.words( categories=["news", "editorial", "reviews" ])
    # example stylistics - modal verbs usage between genres
    def modalz( modals):
        print( "\tCategory\t", end=" ")
        for m in modals:
            print( "\t{}".format( m), end=" ")
        print( "\n"+"-"*100)
        for i, cat in enumerate( brown.categories() ): 
            print( "{}.{}\t\t".format(i, cat), end=" ")
            fdist = nltk.FreqDist( w.lower() for w in brown.words(categories=cat) ) 
            for m in modals:
                print( "\t{}".format(fdist[m] ), end=" ")
            print("")

    modalz( ["can", "could", "may", "might", "must", "will"] ) 
    modalz( ["should", "ought", "would", "could", "do", "did", "does"])
    modalz( [ "what", "when", "where", "why", "who"])

    ## ditto using nltk conditional frequency distributions
    cfdist = nltk.ConditionalFreqDist( 
        (genre, word) 
        for genre in brown.categories()
        for word in brown.words(categories=genre ) ) 

    genz = ["news", "religion", "hobbies", "humor", "romance"]
    modz = ["can", "could", "may", "might", "must", "will"] 
    cfdist.tabulate(conditions=genz, samples=modz )     

    # 4. Reuters Corpus - news articles, 90 topics, grouped into training and testing sets
    # << Apparent goal is to predict the category/topic of a given article??
    corp_content( reuters )  
    # retrieve topic(s) of a given article 
    reuters.categories( "training/9865")
    reuters.categories( ["training/9865", "training/9880"] )
    # find articles that cover some topic(s) 
    reuters.fileids( "barley")
    reuters.fileids( ["barley", "corn"])

    # the first words are in all CAPs and are the titles of the article. The rest is the story text
    for i, txt in enumerate( reuters.fileids( [ "barley", "oil"])):
        print( "{}. {}\t{}".format( i, txt, reuters.words(txt)[:10] ) ) 


    # 5. Speeches - Inaugral Address Corpus << 55 USA Presidential addresses
    # << interesting in that there's a time horizon element from 1789  to 2009 (first 4 xters of fileid = year) ; can study how language changes with time; could reflect on priorities, culture, ???
    corp_content( inaugural )  
    # how America and Citizen ar eused over time 
    cfdist = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words( fileid ) 
        for target in ['america', 'citizen']
        if w.lower().startswith( target ) 
    )
    cfdist.plot() 

    # 6. Annotated Text Corpora
    # annotations: POS, named entities, syntatic structures, semantic roles, 

    # 7. Other Languages Corpora
    # includes udhr = Universal Declaration of Human Rights in over 300 languages

    # word length freq by diff languages
    langz = ["English", "Chickasaw",  "German_Deutsch", "Kinyarwanda", "Swahili_Kiswahili"]
    cfdist = nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in langz
        for word in udhr.words( lang+"-Latin1")
    )
    cfdist.plot()
    cfdist.plot(cumulative=True)

    # alphabet freq 
    nltk.FreqDist( udhr.raw( "Kinyarwanda-Latin1") ).plot()

    # 8. Loading your own Corpora
    # << txt files. Use PlaintextCorpusReader. Check dir location 
    # 
    my_corpus = PlaintextCorpusReader( "root_dir_path_here", ".*") # second param is a list of fileids defined as a list or an ls pattern
    