#!/usr/bin/env python3
"""
WAV file player for specific audio output devices.

Syntax: play_wav.py "f:<wav_file_path>" ["d:<UAC_device_name>"]

If no parameters provided:
  - Default device: "Realtek"
  - Default file: "noise0.8.wav"
"""

import sounddevice as sd
import soundfile as sf
import sys
from typing import Optional, Tuple


def parse_arguments(args: list[str]) -> tuple[str, str]:
    """Parse command-line arguments to extract file path and device name.
    
    Args:
        args: Command-line arguments (excluding script name)
    
    Returns:
        Tuple of (wav_file_path, device_name)
    """
    wav_file_path = ""
    device_name = ""
    
    for arg in args:
        print(arg)
        try:
            colon_index = arg.index(':')
            prefix = arg[:colon_index].upper()
            value = arg[colon_index + 1:]
            
            if prefix == "F":
                wav_file_path = value
                print(f"file name: {wav_file_path}")
            elif prefix == "D":
                device_name = value
                print(f"UAC Out device name: {device_name}")
        except ValueError:
            print(f"Warning: Skipping invalid argument format: {arg}")
    
    # Set defaults if not provided
    if not device_name:
        device_name = "Realtek"
    
    return wav_file_path, device_name


def find_audio_device(output_name: str, input_name: str = "BEHRINGER") -> Tuple[Optional[int], Optional[int]]:
    """Find audio device indices matching the specified names.
    
    Args:
        output_name: Name pattern to match for output device
        input_name: Name pattern to match for input device
    
    Returns:
        Tuple of (output_device_id, input_device_id), None if not found
    """
    output_idx = None
    input_idx = None
    
    print("Available audio devices:")
    devices = sd.query_devices()
    
    for idx, device in enumerate(devices):
        print(f"{idx}: {device['name']} ({device['max_input_channels']} in, "
              f"{device['max_output_channels']} out) Host API: {device['hostapi']}")
        
        # Check for DirectSound (hostapi == 1) devices
        if device['hostapi'] != 1:
            continue
            
        # Check for input device
        if device['max_input_channels'] > 1 and input_name in device['name']:
            print(f"{idx}: DirectSound Input")
            input_idx = idx
        
        # Check for output device
        if device['max_output_channels'] > 1 and output_name in device['name']:
            print(f"{idx}: DirectSound Output")
            output_idx = idx
    
    return output_idx, input_idx


def play_wav_file(file_path: str, device_id: int) -> bool:
    """Play a WAV file on the specified audio device.
    
    Args:
        file_path: Path to the WAV file
        device_id: Device index to use for playback
    
    Returns:
        True if playback succeeded, False otherwise
    """
    try:
        data, fs = sf.read(file_path, dtype='float32')
        sd.play(data, samplerate=fs, device=device_id)
        sd.wait()
        return True
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error playing file: {e}")
        return False


def main():
    """Main entry point."""
    # Parse command-line arguments (skip script name)
    wav_file_path, device_name = parse_arguments(sys.argv[1:])
    
    # Find audio devices
    output_device_id, _ = find_audio_device(device_name)
    
    # Use default file if none specified
    if not wav_file_path:
        wav_file_path = 'noise0.8.wav'
    
    # Play the file if output device was found
    if output_device_id is not None:
        success = play_wav_file(wav_file_path, output_device_id)
        sys.exit(0 if success else 1)
    else:
        print("未找到適合的輸出設備。")
        sys.exit(1)


if __name__ == "__main__":
    main()
