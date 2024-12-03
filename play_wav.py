import sounddevice as sd
import soundfile as sf
import sys


#  syntax  :     paly_wav "f:wav_file_path" ["d:UAC device name"] 
#  if there is no prarmeter attached   device name will be "Realtek"   wev file name will be noise0.8.wav


wav_file_path1=""
device_name =""
n = len(sys.argv)
for p0 in range(1, n):   # skip first exe name
    s = sys.argv[p0]
    print(s)
    colon_index = s.index(':')
    s0 = s[:colon_index]
    if s0 == "f" or s0 == 'F':  # show,save image or not
        wav_file_path1=  s[colon_index + 1:]
        print(f"file name: {wav_file_path1}")
    if s0 == "d" or s0 == 'D':   # device name
        device_name = s[colon_index + 1:]
        print("UAC Out device name: ", device_name)

if device_name=="": device_name="Realtek"
 
# Function to list available audio devices
def list_audio_devices(**kwargs):
    DUT_output_name = kwargs.get("DUT_output_name", "BEHRINGER")
    DUT_input_name = kwargs.get("DUT_input_name", "BEHRINGER")
    
    DUT_output_idx = None
    DUT_input_idx = None
    
    print("Available audio devices:")
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        print(f"{idx}: {device['name']} ({device['max_input_channels']} in, {device['max_output_channels']} out) Host API: {device['hostapi']}")
        
        # Check for DirectSound input devices
        if (device['hostapi'] == 1) and (device['max_input_channels'] > 1) and (DUT_input_name in device['name']):
            print(f"{idx}: DirectSound Input")
            DUT_input_idx = idx
            
            
        # Check for DirectSound output devices
        if (device['hostapi'] == 1) and (device['max_output_channels'] > 1) and (DUT_output_name in device['name']):
            print(f"{idx}: DirectSound Output")
            DUT_output_idx = idx
            break

    return DUT_output_idx, DUT_input_idx  # Return the selected indices

# Function to play a WAV file on a selected audio device
def play_wav_file(file_path, device_id):
    try:
        # Load the audio file
        data, fs = sf.read(file_path, dtype='float32')  # Reads the WAV file
        # Play the audio data on the specified device
        sd.play(data, samplerate=fs, device=device_id)
        #sd.play(data, samplerate=fs, device=25) # hot core 25
        sd.wait()  # Wait until the sound has finished playing
    except Exception as e:
        print(f"Error playing file: {e}")

# Main execution
if __name__ == "__main__":
    # List all available audio devices and get selected indices with custom names
    selected_device_id_out, selected_device_id_in = list_audio_devices(DUT_output_name=device_name, DUT_input_name="BEHRINGER")
    wav_file_path=wav_file_path1
    if wav_file_path=="" :
        wav_file_path = 'noise0.8.wav'  # Path to your WAV file
    
    # Play the WAV file using the selected output device if it was found
    if selected_device_id_out is not None:
        play_wav_file(wav_file_path, selected_device_id_out)
    else:
        print("未找到適合的輸出設備。")

"""
    # Print available host APIs
    host_apis = sd.query_hostapis()
    for api in host_apis:
        print(f"Host API: {api['name']}, Devices: {api['devices']}")
"""        
