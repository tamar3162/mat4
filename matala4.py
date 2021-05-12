# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:48:17 2021

@author: proled
"""
def distance_and_time_info(start_city,destenation,api_key):
    import requests
    url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" % (start_city,destenation,api_key)
    try:
        response = requests.get(url)
        if not response.status_code==200:
            print("error",response.status_code)
        else:
            try:
                data_of_city=response.json()
                dict_city=dict()
                dict_city['city']=data_of_city['destination_addresses']
                dict_city['distance']=data_of_city['rows'][0]['elements'][0]['distance']['text']
                dict_city['time']=data_of_city['rows'][0]['elements'][0]['duration']['text']
                time=dict_city['time']
                if "day" in time:
                    d=int(time.split(' ')[0])
                    h=int(time.split(' ')[2])
                    total=(d*24)+h
                    dict_city['time']=str(total)+" hours"
                return dict_city
            except:
                print("The file may not be in Json format")
    except:
        print("There is a problem with your request")

def calcul_lat_lng(destenation,api_key):
    import requests
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (destenation,api_key)
    try:
        response = requests.get(url)
        if not response.status_code==200:
            print("error",response.status_code)
        else:
            try:
                lines_data=response.json()
                dict_city=dict()
                dict_city['lat']=lines_data['results'][0]['geometry']['location']['lat']
                dict_city['lng']=lines_data['results'][0]['geometry']['location']['lng']
                return dict_city
            except:
                print("The file may not be in Json format")
    except:
        print("There is a problem with your request")

path = "C:/Users/proled/Desktop/python/mata4/dests.txt"
open_file = open(path,mode='r',encoding='utf-8')
read_file = open_file.read()
list_of_city=read_file.split('\n')
das_data=dict()
data_for_sort=dict()
api_key = 'AIzaSyDyTL5m1O3WPDwYhcc0S7rdX9s1yj4PcPo' 
start_city='תל אביב'
for city in list_of_city:
    answer=dict()
    answer=distance_and_time_info(start_city,city,api_key)
    name=answer['city'][0]
    geo_answer=dict()
    geo_answer=calcul_lat_lng(city,api_key)
    das_data[name]=(answer['distance'],answer['time'],geo_answer['lat'],geo_answer['lng'])
    data_for_sort[name]=(answer['distance'])


l_city=list()
for i in das_data:
    l_city.append(i)
for i in l_city:
    print("the city: "+i)
    print("distance from Tel Aviv: "+das_data[i][0])
    print("time from Tel Aviv: "+das_data[i][1])
    print("lat: ")
    print(das_data[i][2])
    print("lng: ")
    print(das_data[i][3])
    print('\n')

tmp_list=list()
for x,y in data_for_sort.items():
    tmp_list.append((y,x))
tmp_list=sorted(tmp_list,reverse=True)
print("The three cities with the largest distance from Tel Aviv are:")
for x,y in tmp_list[:3]:
    print(y,x)