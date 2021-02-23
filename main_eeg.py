# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:20:12 2020

@author: MAS
"""

import socket
import json
import time
from datetime import datetime

#Experiment duration
duration = 60*40 # seconds

outfile="data_eeg.csv";
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13854) #Default mindwave port
sock.connect(server_address)
command = "{\"enableRawOutput\": false, \"format\": \"Json\"}\n"

def collect_data():
    sent = sock.send(command.encode('ascii'))
    data = sock.recv(2048)
    poorSignalLevel=blinkStrength=mentalEffort=familiarity=attention=meditation=delta=theta=lowAlpha=highAlpha=lowBeta=highBeta=lowGamma=highGamma=0
    #Example data:
    #{"eSense":{"attention":91,"meditation":41},"eegPower":{"delta":1105014,"theta":211310,"lowAlpha":7730,"highAlpha":68568,"lowBeta":12949,"highBeta":47455,"lowGamma":55770,"highGamma":28247},"poorSignalLevel":0}
    start_time = time.perf_counter()
    while time.perf_counter() - start_time < duration:        
        try:
            data = sock.recv(2048).decode('utf-8')
            eeg = json.loads(data)
        except:
            print("Invalid json format!!!")
            continue
        timestamp = str(datetime.today())
        blinkStrength = mentalEffort = familiarity = 0
        if 'blinkStrength' in eeg:
            blinkStrength = eeg['blinkStrength']

        if 'mentalEffort' in eeg:
            mentalEffort = eeg['mentalEffort']

        if 'familiarity' in eeg:
            familiarity = eeg['familiarity']            
    
        if 'poorSignalLevel' in eeg:
            poorSignalLevel = eeg['poorSignalLevel']
            
        if 'eSense' in eeg:
            attention = eeg['eSense']['attention']
            meditation = eeg['eSense']['meditation']
          
        if 'eegPower' in eeg:
            delta = eeg['eegPower']['delta']
            theta = eeg['eegPower']['theta']
            lowAlpha = eeg['eegPower']['lowAlpha']
            highAlpha = eeg['eegPower']['highAlpha']
            lowBeta = eeg['eegPower']['lowBeta']
            highBeta = eeg['eegPower']['highBeta']
            lowGamma = eeg['eegPower']['lowGamma']
            highGamma = eeg['eegPower']['highGamma']
            
        if poorSignalLevel > 0:
            print("Signal is poor!!!")
            
        outputstr = timestamp+","+str(poorSignalLevel)+","+str(blinkStrength)+","+str(mentalEffort)+","+str(familiarity)
        outputstr = outputstr+","+str(attention)+","+str(meditation)
        outputstr = outputstr+","+str(delta)+","+str(theta)+","+str(lowAlpha)+","+str(highAlpha)
        outputstr = outputstr+","+str(lowBeta)+","+str(highBeta)+","+str(lowGamma)+","+str(highGamma)
        writeFile(outputstr)
        time.sleep(0.2)
    sock.close()

def writeFile(outputstr):
    outfptr = open(outfile,'a');
    outfptr.write(outputstr+"\n");
    outfptr.close()

if __name__ == "__main__":
    collect_data()