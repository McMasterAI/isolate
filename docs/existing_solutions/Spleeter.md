# Spleeter

[Github Repo](https://github.com/deezer/spleeter)

[Google Colab Demo](https://colab.research.google.com/github/deezer/spleeter/blob/master/spleeter.ipynb)


### Dataset used for training and testing

The models were trained on Deezer’s internal datasets (noteworthily the Bean dataset that was used in (Prétet et al., 2019)) using Adam (Kingma & Ba, 2014).  Training time took approximately a full week on a single GPU.


### Preprocessing of inputs

Module for building data preprocessing pipeline using the tensorflow data API. Data preprocessing such as audio loading, spectrogram computation, cropping, feature caching or data augmentation is done using a TensorFlow dataset object that output a tuple (input, output)
    where:
   * input is a dictionary with a single key that contains the (batched)
        mix spectrogram of audio samples
   * output is a dictionary of a spectrogram of the isolated tracks
        (ground truth)
        
### Methdologies

All songs are stereo and sampled at 44100Hz. They were resample them to 22050Hz to reduce computational complexity. All songs were split into segments of 11.88 seconds. For Catalog and
Bean, one random segment from each song in the training and validation sets was chosen, avoiding the intro (first 20s) and the outro (last 20s), where vocals are often missing.
Short Time Fourier Transform (STFT) was used to process data as input and output features for our network. The window size is
2048 and the step size is 512. 

### Evaluation metric performance
The models were tested on the standard musdb18 dataset (Rafii et al., 2017).

Standard source separation metrics are used for evaluation purposes(Vincent, Gribonval, & Fevotte, 2006)
* Signal to Distortion Ratio (SDR)
* Signal to Artifacts Ratio (SAR)
* Signal to Interference Ratio (SIR)
* Source Image to Spatial distortion Ratio (ISR)

Open-Unmix (Stöter, Uhlich, Liutkus, & Mitsufuji, 2019) and Demucs (Défossez, Usunier, Bottou, & Bach, 2019) are the only released system that performs near state-of-the-art performances. As can be seen, for most metrics Spleeter is competitive with Open-Unmix and especially on SDR for all instruments, and is almost on par with Demucs.
The Spleeter results were presented with soft masking and with multi-channel Wiener filtering (applied using Norbert (Liutkus & Stöter, 2019))

 ![metrics](https://user-images.githubusercontent.com/32804716/128948467-74bf6cea-1ef2-483f-bfc8-a158ed96af27.jpg)


### Model used/ Libraries used

It comes in the form of a Python Library based on Tensorflow, with the following pre-trained models.

Spleeter pre-trained models:
* vocals/accompaniment separation
* 4 stems separation as in SiSec (Stöter, Liutkus, & Ito, 2018) (vocals, bass, drums and other). 
* 5 stems separation with an extra piano stem (vocals, bass, drums, piano, and other)

The pre-trained models are U-nets (Jansson et al., 2017) and follow similar specifications as in (Prétet, Hennequin, Royo-Letelier, & Vaglio, 2019). 






