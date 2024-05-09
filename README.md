# audioTextureDatasets

This repository has two functions;
 1. To act as a database for audio texture datasets with and without control parameters, for use in machine learning models.
 2. To provide useful functionalities for manipulating audio texture datasets for machine learning models.

A repository holding a collection of audio texture datasets for training machine learning model, with a stadardised approach.

## Datasets

### Audio Texture Datasets
- UrbanSound8K, https://urbansounddataset.weebly.com/urbansound8k.html 
- BBC Sound Effects, https://sound-effects.bbcrewind.co.uk/
- FreeSound, https://freesound.org/
- ESC-50, https://github.com/karolpiczak/ESC-50 
- DCASE, https://dcase.community/challenge2023/task-foley-sound-synthesis

### Audio Texture Datasets with control parameters
- SynTex, https://syntex.sonicthings.org/ 
- Parameterized Sound Set database, https://sonicthings.org:9999/
- Boreilly dataset, https://animatedsound.com/datasets/

## Functionalities
Curerntly scripts exist for loading data and manipulating in the following ways;

### File formatting
Scripts exist for manipulating audio files in a number of ways;

#### Audio length
Any length of audio can be split into any arbitrary length 

#### Sample Rate
Audio can be re-sampled to;
 - 44kHz
 - 22kHz
 - 16kHz
 - 8kHz

#### Bit depth
Bit depth of Audio clips can be changed to;
 - 16 bit
 - 32 bit

### Audio representations
Scripts exist for manipulating audio files in the time domain into a number of different representations for machine learning;

 - Granulating waveform
 - Spectrograms
 - Mel Frequency Spectrograms
 - Cepstral Coefficients
 - Mel Freq Cepstral Coefficients

