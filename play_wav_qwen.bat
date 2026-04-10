@echo off
REM 輸出批處理文件名稱
echo Batch file name: %0

REM 輸出第一個參數
if "%~1"=="" (
    echo First parameter is missing.
) else (
    echo First parameter: %~1
)

REM 輸出第二個參數
if "%~2"=="" (
    echo Second parameter is missing.
) else (
    echo Second parameter: %~2
)

REM 輸出所有參數
echo All parameters: %*

python.exe play_wav_qwen.py "d:omni" "f:%*"


rem python.exe d:/data/python/UAC/play_wav/play_wav_qwen.py