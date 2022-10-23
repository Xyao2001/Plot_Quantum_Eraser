#! /usr/bin/env python3
import pandas as pd
import numpy as np
import re

class MissingInfo(Exception):
    def __init__(self,msg):
        self.msg = msg


class WeatherSystem:
    global temp
    temp = pd.DataFrame(columns =['id', 'time', 'location', 'temperature'])
    
    global humid
    humid=pd.DataFrame(columns =['id', 'time', 'location', 'humidity'])

    def __init__(self):
        self
        

    def receive_message(self, message):
        
        self.msg=message.split(",")
        
        print(self.msg)
        if "TEMP" in self.msg:
            temp.loc[len(temp)] = self.msg[1:5]
        
        if "HUMID" in self.msg:
            humid.loc[len(humid)] = self.msg[1:5]
        

    
    #returns the most recent temperature and humidity measurements at the given location as a pair of integers
    def current_stats(self, location):
        
        if (location in temp.values) and (location in humid.values) :
            #return the dataframe that match location==location
            temp_val=temp.loc[temp['location'] == location]
            humid_val=humid.loc[humid['location'] == location]
            la_temp=temp_val.iloc[-1][3]
            la_humid=humid_val.iloc[0][3]
            tuple1=(int(la_temp),int(la_humid))



            return(tuple1)
        else:
            raise MissingInfo("info is missing")
    

    # and returns the last temperature measurement at that location that happened at the given time or earlier, as an integer.

    def temperature_history(self,location: str, time: str) :
        temp_val=temp.loc[temp['location'] == location]
        time_val=temp_val.loc[temp_val['time'] <= time]
        if time_val['time'].empty:
            raise MissingInfo("info is missing")
        max_time=max(time_val['time'])
    #find a list of all the values of time for that location and compare the current time to the maximum time recorded
        if (location in temp.values) and (time >=max_time):
            la_temp=time_val.iloc[-1][3]
            return(int(la_temp))
        

        else:
            raise MissingInfo("info is missing")
    #return a list with moving averages of temperature measurements at the given location. The first element of the output list should be the mean of the first k measurements
    def average_temps(self,location: str, k: int):
        temp_val=temp.loc[temp['location'] == location]
        n=temp_val[temp_val.columns[0]].count()
        i=0
        moving_averages = []
        window_size=k
        #var_temp=temp_val["temperature"].astype('int64')
        var_temp=temp_val['temperature'].to_numpy()
        var_temp=list(map(int, var_temp))
        
        var_temp.remove(max(var_temp))
        var_temp.remove(min(var_temp))
        if n<k:
            raise MissingInfo("info is missing")
        while i <len(var_temp)- window_size + 1:
             window = var_temp[i : i + window_size]
              # Calculate the average of current window
             window_average = round(sum(window) / window_size, 2)
             moving_averages.append(window_average)
             
             i += 1
        
        

        return moving_averages


        
        

            
        
        


if __name__ == "__main__":
    # Test average_temps
    def close(a, b):
        return all(abs(aa - bb) < 1e-5 for aa, bb in zip(a, b))

    ws = WeatherSystem()
    ws.receive_message("TEMP,1,00:00:01,Somewhere,1")
    ws.receive_message("TEMP,2,00:00:05,Somewhere,3")
    ws.receive_message("TEMP,3,00:00:15,Somewhere,8")
    ws.receive_message("TEMP,4,00:00:20,Somewhere,7")
    assert close(ws.average_temps("Somewhere", 3), [3, 7])
    assert close(ws.average_temps("Somewhere", 4), [5])
    try:
        ws.average_temps("Somewhere", 10)
        print("Did not raise a MissingInfo exception!")
    except MissingInfo:
        pass
