import pandas as pd

class Database:
    def __init__(self): 
        self.df=pd.read_csv("startup_funding.csv")
        self.clean()
        
    def clean(self):    
        self.df.drop(columns=['Remarks'],inplace=True)

        self.df.set_index('Sr No',inplace=True)

        self.df.rename(columns={
            'Date dd/mm/yyyy':'date',
            'Startup Name':'startupname',
            'Industry Vertical':'vertical',
            'SubVertical':'subvertical',
            'City  Location':'city',
            'Investors Name':'investor',
            'InvestmentnType':'round',
            'Amount in USD':'amount'
        },inplace=True)

        self.df['amount']=self.df['amount'].fillna('0')
        self.df['amount']=self.df['amount'].str.replace(',','')
        self.df['amount']=self.df['amount'].str.replace('undisclosed','0')
        self.df['amount']=self.df['amount'].str.replace('unknown','0')
        self.df['amount']=self.df['amount'].str.replace('Undisclosed','0')
        self.df=self.df[self.df['amount'].str.isdigit()]
        self.df['amount']=self.df['amount'].astype('float')

        def to_INRCr(amount):
            return (amount * 82.5)/10000000
        self.df['amount']=self.df['amount'].apply(to_INRCr)

        self.df['date']=self.df['date'].str.replace('05/072018','05/07/2018')
        self.df['date']=self.df['date'].str.replace('01/07/015','01/07/2015')
        self.df['date']=self.df['date'].str.replace('12/05.2015','12/05/2015')
        self.df['date']=self.df['date'].str.replace('13/04.2015','13/04/2015')
        self.df['date']=self.df['date'].str.replace('15/01.2015','15/01/2015')
        self.df['date']=self.df['date'].str.replace('22/01//2015','22/01/2015')
        self.df['date']=pd.to_datetime(self.df['date'],format='%d/%m/%Y')

        self.df=self.df.dropna(subset=['date','startupname','vertical','city','investor','round','amount'])
        


