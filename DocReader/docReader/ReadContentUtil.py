from PyPDF2 import PdfFileReader as pdf 
from newspaper import Article

"""
fpath: local path to file 
return: String array of text lines
"""
def readTextFileLocal(fpath):
    res = []
    with open( fpath, "r") as dfile:
        res = dfile.readLines()
    return res


"""
fpath: local path to file 
return: String array of text lines
uses: PyPDF2
"""
def readPDFLocal(fpath):
    res = []
    with open( fpath, "rb") as dfile:
        doc = pdf( dfile )
        len = doc.getNumPages() # doc.numPages
        for i in range(len):
            res.append( doc.getPage(i).extractText() )
    return res     



"""
fpath: www path to newspaper article  
return: String array of text lines
uses: newspaper3k << already has nlp and can use nltk << effing more capabilities including build entire site @ article scraping and curation
"""
def readNewsArtcile( upath):
    res = [ ]
    article = Article( upath )
    article.download() # fetch html
    article.parse( ) # parse for content and meta ; ready it for tokeninzer and nltk nlp 
    res.append( article.text ) 
    return res



def spewResults( resArray ):    
    print( "Len of result = {}".format( len(resArray) ) )
    if( len( resArray) > 0 ) :
        temp = resArray[0]
        print( "First line is: {}".format( temp[0: min(30, len(temp)) ] ) ) 
    print("-------\n")

if __name__ == "__main__":
    spewResults( readPDFLocal( "example.pdf") ) 
    spewResults( readNewsArtcile("https://www.nation.co.ke/counties/nairobi/Nairobi-to-host-diaspora-convention/1954174-5381376-bok1o/index.html") ) 
    

