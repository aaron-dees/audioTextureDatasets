# Segmented Audio Textures

This directory contains a script that allows the segmentation of audio files into smaller chunks. The script has a number of functionalaties, the main is that it accepts a directory as input, which should contain the audio files to be segmented. It will then segment these audio clips into clips of the target length.

The script uses a configuration file, which has the following params;
 - input_audio_directory: Path to the directory holding the audio files you wish to segment, currently this will need to contain only the .wav files.
 - output_audio_directory: Path to where you want the segmented audio files to be saved.
 - target_sr: Target samples rate, if this differs from the read sample rate the audio will be resampled. 
 - target_length: The segment length in seconds.
 - peak_amplitude_min: Minimum allowed peak amplitude in a segment, this is used to remove segments that are silent.
 - silence_length: Minimum length of non-silent audio acceptable in a segment, this is again used to remove segments. 
 - amplitude_norm: Normalise the amplitude between -1 and 1.
