import pandas as pd 
facebook = pd.read_csv("C:/Users/Jake/Desktop/Facebook.csv") 
facebook["Company"] = "Facebook" 
apple = pd.read_csv("C:/Users/Jake/Desktop/Apple.csv") 
apple["Company"] = "Apple" 
amazon = pd.read_csv("C:/Users/Jake/Desktop/Amazon.csv") 
amazon["Company"] = "Amazon" 
netflix = pd.read_csv("C:/Users/Jake/Desktop/Netflix.csv") 
netflix["Company"] = "Netflix" 
google = pd.read_csv("C:/Users/Jake/Desktop/Google.csv") 
google["Company"] = "Google"
faang = pd.concat([facebook, apple, amazon, netflix, google]) 
faang["Date"] = pd.to_datetime(faang["Date"]) 
faang["Year"] = faang["Date"].dt.year 
yearly_performance = faang.groupby(["Company", "Year"]).agg({"Close" : "mean"}) 
faang["Daily_Swing"] = faang["High"] - faang["Low"] 
volatility = faang.groupby(["Company"]).agg({"Daily_Swing" : "mean"}) 

volatility.reset_index().to_csv("C:/Users/Jake/Desktop/volatility.csv", index=False)

yearly_performance.reset_index().to_csv("C:/Users/Jake/Desktop/yearly_performance.csv", index=False)