import paralleldots

class API:
    def __init__(self) :
        paralleldots.set_api_key('x')
    
    def sentiment_analysis(self,text):
    
         res=paralleldots.sentiment(text)
         if "Error" in res:
             res={'sentiment':{'negative':0.10,"neutral":0.50,"positive":0.30}}
         return res
    
    def ner(self,text):
        res=paralleldots.ner(text)
        if res["code"]==400:
            res={'ner':{'name':"Hello","place":"India"}}
        return res
    
    def emotion(self,text):
        res=paralleldots.emotion(text)
        print(res)
        if "Error" in res:
            res={'emotion':{"result":1}}
        return res
    