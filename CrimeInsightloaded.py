from joblib import load 
import pandas as pd
loaded=load("CrimeInsight-pre.joblib")

cities_names={'Agra':0, 'Ahmedabad':1, 'Bangalore':2, 'Bhopal':3, 'Chennai':4, 'Delhi':5,
              'Faridabad':6, 'Ghaziabad':7, 'Hyderabad':8, 'Indore':9, 'Jaipur':10,
              'Kalyan':11, 'Kanpur':12, 'Kolkata':13, 'Lucknow':14, 'Ludhiana':15, 'Meerut':16,
              'Mumbai':17, 'Nagpur':18, 'Nashik':19, 'Patna':20, 'Pune':21, 'Rajkot':22,
              'Srinagar':23, 'Surat':24, 'Thane':25, 'Varanasi':25, 'Vasai':26, 'Visakhapatnam':27}

crimes_index={0:'ARSON', 1:'ASSAULT', 2:'BURGLARY' , 4:'COUNTERFEITING', 5:'CYBERCRIME',
              6:'DOMESTIC VIOLENCE', 7:'DRUG OFFENSE', 8:'EXTORTION',
              9:'FIREARM OFFENSE', 10:'FRAUD', 11:'HOMICIDE', 12:'IDENTITY THEFT',
              13: 'ILLEGAL POSSESSION', 14:'KIDNAPPING',15:'PUBLIC INTOXICATION',
              16:'ROBBERY', 17:'SEXUAL ASSAULT', 18:'SHOPLIFTING', 19:'TRAFFIC VIOLATION',
              20:'VANDALISM', 21:'VEHICLE - STOLEN'}
if __name__=="__main__":
   for name,index in cities_names.items():
       print(f"[{index}]{name}")
   print("please enter the  city index")
   inp_city=int(input(">]]"))
   print("Please  enter the age")
   inp_age=int(input(">]]"))
   print("please choose the gender")
   inp_gender=int(input("0 for female or 1 or male or 2 for x >]]"))
   print("please enter  the time")
   inp_time=input("2:00 in 24 hrs format>>]")
   hours,minutes=map(int,inp_time.split(":"))
   total_min=hours*60+minutes
    
   data=pd.DataFrame([[inp_city,inp_age,inp_gender,total_min]],columns=["City","Victim Age","Victim Gender","Time"])
   final_data=loaded.predict(data)
   print(f"According to data you can be victim of {crimes_index["final_data"}")
