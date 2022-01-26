from datetime import timedelta
import telegram
from nsepy import get_history
import pandas as pd
from datetime import date
import telebot
API_KEY = "5299754604:AAG6RGM7_c57SgFuMXbvfZlCCVgd7iFYWkQ"
bot = telebot.TeleBot(API_KEY)
print("running.........................")


@bot.message_handler(commands=['start','help'])
def hi(message):
    bot.send_message(message.chat.id, str("I am price bot. Search your stock using its symbol. "
                                          "For example : if you search for axis bank then use /axisbank"))

@bot.message_handler(commands=["AARTIIND","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT",
                               "ADANIPORTS","ALKEM","AMARAJABAT","AMBUJACEM","APLLTD","APOLLOHOSP",
                               "APOLLOTYRE","ASHOKLEY","ASIANPAINT","ASTRAL","ATUL","AUBANK",
                               "AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE",
                               "BALKRISIND","BALRAMCHIN","BANDHANBNK","BANKBARODA","BATAINDIA",
                               "BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON",
                               "BOSCHLTD","BPCL","BRITANNIA","BSOFT","CADILAHC","CANBK",
                               "CANFINHOME","CHAMBLFERT","CHOLAFIN","CIPLA","COALINDIA",
                               "COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB",
                               "CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP",
                               "DIVISLAB","DIXON","DLF","DRREDDY","EICHERMOT","ESCORTS",
                               "EXIDEIND","FEDERALBNK","FSL","GAIL","GLENMARK","GMRINFRA",
                               "GNFC","GODREJCP","GODREJPROP","GRANULES","GRASIM","GSPL",
                               "GUJGASLTD","HAL","HAVELLS","HCLTECH","HDFC","HDFCAMC",
                               "HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER",
                               "HINDPETRO","HINDUNILVR","HONAUT","IBULHSGFIN","ICICIBANK",
                               "ICICIGI","ICICIPRULI","IDEA","IDFC","IDFCFIRSTB","IEX",
                               "IGL","INDHOTEL","INDIACEM","INDIAMART","INDIGO",
                               "INDUSINDBK","INDUSTOWER","INFY","IOC","IPCALAB",
                               "IRCTC","ITC","JINDALSTEL","JKCEMENT","JSWSTEEL",
                               "JUBLFOOD","KOTAKBANK","L&TFH","LALPATHLAB","LAURUSLABS",
                               "LICHSGFIN","LT","LTI","LTTS","LUPIN","M&M","M&MFIN",
                               "MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX",
                               "METROPOLIS","MFSL","MGL","MINDTREE","MOTHERSUMI",
                               "MPHASIS","MRF","MUTHOOTFIN","NAMINDIA","NATIONALUM",
                               "NAUKRI","NAVINFLUOR","NBCC","NESTLEIND","NMDC","NTPC",
                               "OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT",
                               "PETRONET","PFC","PFIZER","PIDILITIND","PIIND","PNB",
                               "POLYCAB","POWERGRID","PVR","RAIN","RAMCOCEM","RBLBANK",
                               "RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN",
                               "SHREECEM","SIEMENS","SRF","SRTRANSFIN","STAR","SUNPHARMA",
                               "SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM",
                               "TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN",
                               "TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL",
                               "ULTRACEMCO","UPL","VEDL","VOLTAS","WHIRLPOOL","WIPRO","ZEEL",
                               "aartiind","abbotindia","abcapital","abfrl","acc","adanient",
                               "adaniports","alkem","amarajabat","ambujacem","aplltd",
                               "apollohosp","apollotyre","ashokley","asianpaint","astral",
                               "atul","aubank","auropharma","axisbank","bajaj-auto",
                               "bajajfinsv","bajfinance","balkrisind","balramchin",
                               "bandhanbnk","bankbaroda","bataindia","bel","bergepaint",
                               "bharatforg","bhartiartl","bhel","biocon","boschltd",
                               "bpcl","britannia","bsoft","cadilahc","canbk","canfinhome",
                               "chamblfert","cholafin","cipla","coalindia","coforge",
                               "colpal","concor","coromandel","crompton","cub",
                               "cumminsind","dabur","dalbharat","deepakntr","deltacorp",
                               "divislab","dixon","dlf","drreddy","eichermot","escorts",
                               "exideind","federalbnk","fsl","gail","glenmark","gmrinfra",
                               "gnfc","godrejcp","godrejprop","granules","grasim","gspl",
                               "gujgasltd","hal","havells","hcltech","hdfc","hdfcamc",
                               "hdfcbank","hdfclife","heromotoco","hindalco","hindcopper",
                               "hindpetro","hindunilvr","honaut","ibulhsgfin","icicibank",
                               "icicigi","icicipruli","idea","idfc","idfcfirstb","iex",
                               "igl","indhotel","indiacem","indiamart","indigo","indusindbk",
                               "industower","infy","ioc","ipcalab","irctc","itc","jindalstel",
                               "jkcement","jswsteel","jublfood","kotakbank","l&tfh","lalpathlab",
                               "lauruslabs","lichsgfin","lt","lti","ltts","lupin","m&m","m&mfin",
                               "manappuram","marico","maruti","mcdowell-n","mcx","metropolis",
                               "mfsl","mgl","mindtree","mothersumi","mphasis","mrf",
                               "muthootfin","namindia","nationalum","naukri","navinfluor",
                               "nbcc","nestleind","nmdc","ntpc","oberoirlty","ofss","ongc",
                               "pageind","pel","persistent","petronet","pfc","pfizer",
                               "pidilitind","piind","pnb","polycab","powergrid","pvr",
                               "rain","ramcocem","rblbank","recltd","reliance","sail",
                               "sbicard","sbilife","sbin","shreecem","siemens","srf",
                               "srtransfin","star","sunpharma","suntv","syngene","tatachem",
                               "tatacomm","tataconsum","tatamotors","tatapower","tatasteel",
                               "tcs","techm","titan","torntpharm","torntpower","trent",
                               "tvsmotor","ubl","ultracemco","upl","vedl","voltas","whirlpool",
                               "wipro","zeel",
                               "Aartiind","Abbotindia","Abcapital","Abfrl","Acc","Adanient",
                               "Adaniports","Alkem","Amarajabat","Ambujacem","Aplltd","Apollohosp",
                               "Apollotyre","Ashokley","Asianpaint","Astral","Atul","Aubank",
                               "Auropharma","Axisbank","Bajaj-Auto","Bajajfinsv","Bajfinance",
                               "Balkrisind","Balramchin","Bandhanbnk","Bankbaroda","Bataindia",
                               "Bel","Bergepaint","Bharatforg","Bhartiartl","Bhel","Biocon",
                               "Boschltd","Bpcl","Britannia","Bsoft","Cadilahc","Canbk",
                               "Canfinhome","Chamblfert","Cholafin","Cipla","Coalindia",
                               "Coforge","Colpal","Concor","Coromandel","Crompton","Cub",
                               "Cumminsind","Dabur","Dalbharat","Deepakntr","Deltacorp",
                               "Divislab","Dixon","Dlf","Drreddy","Eichermot","Escorts",
                               "Exideind","Federalbnk","Fsl","Gail","Glenmark","Gmrinfra",
                               "Gnfc","Godrejcp","Godrejprop","Granules","Grasim","Gspl",
                               "Gujgasltd","Hal","Havells","Hcltech","Hdfc","Hdfcamc",
                               "Hdfcbank","Hdfclife","Heromotoco","Hindalco","Hindcopper",
                               "Hindpetro","Hindunilvr","Honaut","Ibulhsgfin","Icicibank",
                               "Icicigi","Icicipruli","Idea","Idfc","Idfcfirstb","Iex","Igl",
                               "Indhotel","Indiacem","Indiamart","Indigo","Indusindbk",
                               "Industower","Infy","Ioc","Ipcalab","Irctc","Itc","Jindalstel",
                               "Jkcement","Jswsteel","Jublfood","Kotakbank","L&Tfh",
                               "Lalpathlab","Lauruslabs","Lichsgfin","Lt","Lti","Ltts",
                               "Lupin","M&M","M&Mfin","Manappuram","Marico","Maruti",
                               "Mcdowell-N","Mcx","Metropolis","Mfsl","Mgl","Mindtree",
                               "Mothersumi","Mphasis","Mrf","Muthootfin","NamIndia",
                               "Nationalum","Naukri","Navinfluor","Nbcc","Nestleind",
                               "Nmdc","Ntpc","Oberoirlty","Ofss","Ongc","Pageind",
                               "Pel","Persistent","Petronet","Pfc","Pfizer",
                               "Pidilitind","Piind","Pnb","Polycab","Powergrid","Pvr",
                               "Rain","Ramcocem","Rblbank","Recltd","Reliance","Sail",
                               "Sbicard","Sbilife","Sbin","Shreecem","Siemens","Srf",
                               "Srtransfin","Star","Sunpharma","Suntv","Syngene",
                               "Tatachem","Tatacomm","Tataconsum","Tatamotors",
                               "Tatapower","Tatasteel","Tcs","Techm","Titan",
                               "Torntpharm","Torntpower","Trent","Tvsmotor","Ubl",
                               "Ultracemco","Upl","Vedl","Voltas","Whirlpool","Wipro","Zeel",])

def price(message):
    fstock=(message.text).replace('/','')
    today = date.today()
    data = get_history(symbol=fstock, start=today - timedelta(days=2), end=date.today())
    data.drop(
        [ "Series", "Open", "High", "Low", "%Deliverble", "Trades", "Turnover", "Volume", "Prev Close",
         "Last"], axis=1, inplace=True)
    data.rename(
        columns={'Deliverable Volume': 'delv vol :','Symbol': 'Name    :', 'Close': 'close     :', 'Date': 'Date:', 'VWAP': 'VWAP    :'},
        inplace=True)

    data.transpose()
    text = str(data.transpose())
    bot.send_message(message.chat.id, text)
bot.polling()
