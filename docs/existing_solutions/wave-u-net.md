# Wave-U-Net


## Model Structure
![Model Layers](./images/wun-model-layers.png)

This model is built off of the [U-Net](https://en.wikipedia.org/wiki/U-Net) architecture.

- CNN
- An *encoder*, followed by a *decoder*.
- Encoder
  - Successive downsampling to encode the input into feature representations of the original input.
- Decoder
  - Project the features back into a longer tensor (upscale).
-  What is the purpose of this method?
   -  To create a full size output generated from the features learned from the input.

---

![U-net demo](./images/wun-unet-images.png)

U-Net CNNs were proposed originally for biomedical image segmentation. In the reference paper, an unsegmented image of cells is used as input to the model *(a)*. This is passed through the encoder, creating features relating to the image segmentation. After decoding/upscaling, a segmentation mask is created from the model output *(c)*. Training is done by overlaying the ground truth/labelled image *(b)* with the segmentation mask *(d)*. A loss is calculated from the pixel differences between the two. 

This process has been reduced to a 1D implementation in Wave-U-Net, but the underlying principles are the same.

---

### Problems and Solutions
*Aliasing*

Distortions caused by trying to assemble audio from an insufficient number of samples (sampling frequency was low). In this case, it is trying to upscale and reconstruct the audio from a smaller number of features.

Similar approaches used *transposed strided convolutions*
- a convolution applied to feature maps (data) padded with zeros between the original data points.

To solve this, they used linear interpolation, ensuring temporal continuity and not inserting false data.


---

## Data Processing
- Performed data augmentation. 
  - Multiplied source tracks by factors between [0.7, 1] 
  - Stretches the data for training and to prevent over-fitting.
- Input mixture is the sum of all of the source signals.
- Conversion to mono audio (except for stereo models).
- Downsampling to 22050 Hz.

---

## Dataset
**Training**:
- 75 random tracks from the training portion of the [MUSDB](https://source-separation.github.io/tutorial/data/musdb18.html) database.
- [CCmixter](https://old.datahub.io/dataset/ccmixter-samples@2013-10-10T20:13:15.777986)

**Validation**:
- 25 remaining tracks from [MUSDB](https://source-separation.github.io/tutorial/data/musdb18.html).

**Evaluation**:
- 50 tracks from the test partition of the [MUSDB](https://source-separation.github.io/tutorial/data/musdb18.html) database.

## Evaluation Metrics & Performance

## Tools & Libraries 
- [PyTorch Implementation](https://github.com/f90/Wave-U-Net-Pytorch)
- [TensorFlow Implementation](https://github.com/satvik-venkatesh/Wave-U-net-TF2)
- [libsndfile](http://mega-nerd.com/libsndfile/)
- [ffmpeg](https://www.ffmpeg.org/)

#### Sources
- [Wave-U-Net Paper](https://arxiv.org/pdf/1806.03185.pdf)
- [U-Net](https://en.wikipedia.org/wiki/U-Net)