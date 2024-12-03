# play_wav
## 可以指定 device, 播放 wav file. 
## parameter
| parameter | example | remark |
|---|---|---|
| f: wav_file_path| "f:c:\aaa\aaa.wav" |   |
| d: device name |  "d:omni" , "d:Realtek"|  |
| v: volume |  95| max 100 (100%) |


example:
```
D:/Program Files/Python313/python.exe d:/data/python/UAC/play_wav/play_wav.py d:Realtek f:noise0.8.wav
```

library you need:
```
pip install sounddevice
pip install soundfile

```


## important notice
```
  when you want to use itts to run this python code.
  you must compiler python code to exe file 
  otherwise UAC audio output device will not available
  
  
  
```  