import sys
sys.path.append('../')

import os
import librosa
import soundfile as sf
import glob
import math

AUDIO_DIR = "/Users/adees/Code/neural_granular_synthesis/datasets/OceanWaves/full/"
SAVE_DIR = "/Users/adees/Code/audioTextureDatasets/data"
TARGET_SR = 16000
TARGET_LENGTH = 0.5
SAMPLE_SIZE = math.floor(TARGET_SR * TARGET_LENGTH)

if __name__ == "__main__":


    filepaths = glob.glob(AUDIO_DIR+"*.wav")

    # check that only holds .wav files
    print(filepaths)
    if len(filepaths)==0:
        raise ValueError("No wav files found in directory")
    
    signals = []
    filenames = []
    for i, v in enumerate(filepaths):
        orig_signal, sr = sf.read(filepaths[i])
        signal = librosa.resample(orig_signal, orig_sr=sr, target_sr=TARGET_SR)
        signals.append(signal)
        # remove the directory, and the extension (.wav)
        filename = filepaths[i][len(AUDIO_DIR):-4]
        filenames.append(filename)
    

    print(f"----- Audio Resampled to, {TARGET_SR}Hz -----")

    for i, v in enumerate(filenames):
        for j in range(signal.shape[0]//SAMPLE_SIZE):
            sample = signal[j*SAMPLE_SIZE:j*SAMPLE_SIZE+SAMPLE_SIZE]
            save_path = f'{SAVE_DIR}/{filenames[i]}_{j}.wav'
            sf.write(save_path, sample, TARGET_SR)
