# play_wav
## 可以指定 device, 播放 wav file. 
## parameter
| parameter | example | remark |
|---|---|---|
| f: wav_file_path| "f:c:\aaa\aaa.wav" |   |
| d: device name |  "d:omni" , "d:Realtek"|  |



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
  you must compiler python code to exe file and run it by 01:run
  or 13:run dos with new process (start)
  otherwise UAC audio output device will not available
  
  
  
```
itts example scrip1
```
     <Item> 
       <Text> </Text> 
       <Description> run exe</Description> 
       <ItemType> 2</ItemType> 
       <Skip> 1</Skip> 
       <ItemSection1> DLL</ItemSection1> 
       <ItemSection2> EXECUTE</ItemSection2> 
       <ItemCommand> ITTS_RUN_AP.dll</ItemCommand> 
       <FailAction> </FailAction> 
       <FieldName> </FieldName> 
       <FieldNumber> </FieldNumber> 
       <ErrorCode> </ErrorCode> 
       <RetryTimes> 0</RetryTimes> 
       <RetryDelay> 0</RetryDelay> 
       <Process> ;</Process> 
       <FieldType> </FieldType> 
       <Parameter> 
         <i1>
           <Content></Content>
           <Description>Min</Description>
         </i1>
         <i2>
           <Content></Content>
           <Description>Max</Description>
         </i2>
         <i3>
           <Content>01:RUN AP</Content>
           <Description>P3 command</Description>
         </i3>
         <i4>
           <Content>play_wav.exe</Content>
           <Description>P4 FileName</Description>
         </i4>
         <i5>
           <Content>f:4900.wav d:omni</Content>
           <Description>P5 parameter</Description>
         </i5>
         <i6>
           <Content>['&testplanpath']</Content>
           <Description>P6 Path</Description>
         </i6>
         <i7>
           <Content></Content>
           <Description>P7 show</Description>
         </i7>
         <i8>
           <Content></Content>
           <Description>P8</Description>
         </i8>
         <i9>
           <Content></Content>
           <Description>P9</Description>
         </i9>
         <i10>
           <Content>Debug</Content>
           <Description>P10</Description>
         </i10>
       </Parameter> 
     </Item> 

```
itts example scrip2

```
     <Item> 
       <Text> </Text> 
       <Description> run dos working with another process</Description> 
       <ItemType> 2</ItemType> 
       <Skip> 1</Skip> 
       <ItemSection1> DLL</ItemSection1> 
       <ItemSection2> EXECUTE</ItemSection2> 
       <ItemCommand> ITTS_RUN_AP.dll</ItemCommand> 
       <FailAction> </FailAction> 
       <FieldName> </FieldName> 
       <FieldNumber> </FieldNumber> 
       <ErrorCode> </ErrorCode> 
       <RetryTimes> 0</RetryTimes> 
       <RetryDelay> 0</RetryDelay> 
       <Process> path</Process> 
       <FieldType> </FieldType> 
       <Parameter> 
         <i1>
           <Content></Content>
           <Description>Min</Description>
         </i1>
         <i2>
           <Content></Content>
           <Description>Max</Description>
         </i2>
         <i3>
           <Content>13:RUN AP</Content>
           <Description>P3 command</Description>
         </i3>
         <i4>
           <Content>cmd</Content>
           <Description>P4 FileName</Description>
         </i4>
         <i5>
           <Content>["/C start """" "+'&testplanpath'"play_wav.exe f:noise0.8.wav d:omni"]</Content>
           <Description>P5 parameter</Description>
         </i5>
         <i6>
           <Content></Content>
           <Description>P6 resultfile</Description>
         </i6>
         <i7>
           <Content>2000</Content>
           <Description>P7 timeout</Description>
         </i7>
         <i8>
           <Content>['&testplanpath']</Content>
           <Description>P8 </Description>
         </i8>
         <i9>
           <Content></Content>
           <Description>P9</Description>
         </i9>
         <i10>
           <Content>debug</Content>
           <Description>P10</Description>
         </i10>
       </Parameter> 
     </Item> 

```

### history
- 2024/12/3:  Remove adjust volume feature. 