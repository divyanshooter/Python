import pandas as pd

class Database:
    def __init__(self): 
        self.df=pd.read_csv("startup_funding.csv")
        self.clean()
    
    def investor_analysis(self,investor):
        investor_df=self.df[self.df['investor'].str.contains(investor)]
        recent_investment=investor_df.sort_values('date',ascending=False).head()[['date','startupname','vertical','city','round','amount']]
        biggest_investments=investor_df.groupby('startupname')['amount'].sum().sort_values(ascending=False).head()
        sector_investments=investor_df.groupby('vertical')['amount'].sum()
        round_investments=investor_df.groupby('round')['amount'].sum()
        city_investments=investor_df.groupby('city')['amount'].sum()
        investor_df['year']=investor_df['date'].dt.year
        year_investments=investor_df.groupby('year')['amount'].sum()
        print(year_investments)
        return recent_investment,biggest_investments,sector_investments,round_investments,city_investments,year_investments
        
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
        


