# REAL-TIME-EMOTION-RECOGNITION-FROM-EEG-SIGNALS-USING-ONE-ELECTRODE-DEVICE
REAL-TIME EMOTION RECOGNITION FROM EEG SIGNALS USING ONE ELECTRODE DEVICE


For real-time demo, link: https://www.youtube.com/watch?v=1Mv0UXeWDyM

For stimulus video, link: https://www.youtube.com/watch?v=GjQLhCBZt5g

Please cite that paper:
https://ieeexplore.ieee.org/abstract/document/7960390

@inproceedings{sarikaya2017emotion,
  title={Emotion recognition from EEG signals through one electrode device},
  author={Sar{\i}kaya, Mehmet Ali and {\.I}nce, G{\"o}khan},
  booktitle={2017 25th Signal Processing and Communications Applications Conference (SIU)},
  pages={1--4},
  year={2017},
  organization={IEEE}
}

# DATA COLLECTION

Simple Json Collector to read from Mindwave driver:
https://github.com/sarikayamehmet/MindwaveJsonCollector

Or simple use as python code:

import sys
import imp
import math
import socket
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13854) #Default mindwave port
sock.connect(server_address)
command = "{\"enableRawOutput\": false, \"format\": \"Json\"}\n"
sent = sock.send(command)

data = sock.recv(2048)
#Example data:
#{"eSense":{"attention":91,"meditation":41},"eegPower":{"delta":1105014,"theta":211310,"lowAlpha":7730,"highAlpha":68568,"lowBeta":12949,"highBeta":47455,"lowGamma":55770,"highGamma":28247},"poorSignalLevel":0}

eeg = json.loads(data)

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
  

