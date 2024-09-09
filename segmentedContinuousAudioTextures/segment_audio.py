import sys
sys.path.append('../')

import os
import librosa
import soundfile as sf
import glob
import math
import json
import numpy as np


if __name__ == "__main__":


    # Read config
    with open("config.json", "r") as configfile:
        config = json.load(configfile)
    
    # Calc number of samples in segment.
    SAMPLE_SIZE = math.floor(config['target_sr'] * config['target_length'])

    filepaths = glob.glob(config['input_audio_directory']+"*.wav")

    # check that only holds .wav files
    if len(filepaths)==0:
        raise ValueError("No wav files found in directory")
    
    signals = []
    filenames = []

    for i, v in enumerate(filepaths):
        signal, sr = sf.read(filepaths[i])
        if len(signal.shape)>1:
            # convert to mono
            print("----- Converting audio to mono -----")
            signal = signal.swapaxes(1, 0)
            signal = librosa.to_mono(signal)
        if(sr != config['target_sr']):
            print(f"----- Audio Resampled from, {sr}Hz to, {config['target_sr']}Hz -----")  
            signal = librosa.resample(signal, orig_sr=sr, target_sr=config['target_sr'])
        
        signals.append(signal)
        # remove the directory, and the extension (.wav)
        filename = filepaths[i][len(config['input_audio_directory']):-4]
        filenames.append(filename)

    

    counter = 0
    n_rejected = 0
    reject = 0
    for i, v in enumerate(filenames):
        n_files = 0;
        for j in range(signals[i].shape[0]//SAMPLE_SIZE):
            counter+=1
            sample = signal[j*SAMPLE_SIZE:j*SAMPLE_SIZE+SAMPLE_SIZE]

            # Mean normalise the audio
            sample -= np.mean(sample)

            if config['peak_amplitude_min']!=0.0 and np.max(np.abs(sample))<config['peak_amplitude_min']:
                reject = 1 # peak amplitude is too low
            trim_pos = librosa.effects.trim(sample, top_db=60, frame_length=1024, hop_length=128)[1]
            if config['silence_length']!=0.0 and (trim_pos[1]-trim_pos[0])<config['silence_length'][1]*SAMPLE_SIZE:
                reject = 1 # non-silent length is too low
            
            if reject == 0:

                # Normalise amplitude between -1 and 1, i think it's better to do this in ML model.
                if config['amplitude_norm']:
                    sample /= np.max(np.abs(sample))
                    sample *= 0.9

                output_dir = config['output_audio_directory']
                save_path = f'{output_dir}{filenames[i]}_{n_files}.wav'
                sf.write(save_path, sample, config['target_sr'])
                n_files += 1
            else:
                n_rejected+=1

    print(f'----- {counter} audio segments found -----')
    print(f'----- {n_rejected} audio segments rejected -----')

