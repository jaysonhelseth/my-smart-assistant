# My Smart Assistant

## Introduction
A voice command application that uses https://picovoice.ai technology for wake word and intent processing. Wake words and itents are built online and then the processing model is downloaded to the machine. The pico voice libraries will work with the model offline to process with audio from the microphone.

## Environment
I use a env.json file for my environment settings. I have not checked mine in, but here is a sample.
```json
{
    "access_key": "pico_key_here",
    "context_path": "path_to_rhino_file.rhn"
}
```

## Devices
The PvRecorder needs to know what device out of its list you should use. I currently have mine hardcoded to 1, but I don't know what will work on your machine. I have this snippet commented out, that can be used to find the device you want.
```python
devices = PvRecorder.get_audio_devices()
print(devices)
```