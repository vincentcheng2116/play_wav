import sounddevice as sd
import soundfile as sf

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

    return DUT_output_idx, DUT_input_idx  # Return the selected indices

# Function to play a WAV file on a selected audio device
def play_wav_file(file_path, device_id):
    try:
        # Load the audio file
        data, fs = sf.read(file_path, dtype='float32')  # Reads the WAV file
        # Play the audio data on the specified device
        sd.play(data, samplerate=fs, device=device_id)
        sd.wait()  # Wait until the sound has finished playing
    except Exception as e:
        print(f"Error playing file: {e}")

# Main execution
if __name__ == "__main__":
    # List all available audio devices and get selected indices with custom names
    selected_device_id_out, selected_device_id_in = list_audio_devices(DUT_output_name="BEHRINGER", DUT_input_name="BEHRINGER")
    
    wav_file_path = 'noise0.8.wav'  # Path to your WAV file
    
    # Play the WAV file using the selected output device if it was found
    if selected_device_id_out is not None:
        play_wav_file(wav_file_path, selected_device_id_out)
    else:
        print("未找到適合的輸出設備。")

    # Print available host APIs
    host_apis = sd.query_hostapis()
    for api in host_apis:
        print(f"Host API: {api['name']}, Devices: {api['devices']}")