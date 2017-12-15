# Comparison of MobileNet, ResNet50, and InceptionV3 in Keras

This is a simple example of using ResNet, MobileNet and InceptionV3 from Keras to do object detection and classification tasks.

### Demo

![][image1]

|   Models  |          MobileNet          |          ResNet50         |           InceptionV3          |
|:---------:|:---------------------------:|:-------------------------:|:------------------------------:|
| 1st guess | 'traffic_light', 0.99999177 |  'nematode', 0.090073794  |      'traffic_light', 1.0      |
| 2nd guess |    'pole', 6.4110359e-06    | 'dishwasher', 0.042908493 |    'maillot', 8.7838531e-10    |
| 3rd guess |  'flagpole', 4.8521628e-07  |   'cleaver', 0.026148975  | 'walking_stick', 5.6997368e-10 |

In this case, both MobileNet and InceptionV3 successfully recognize the traffic light, but the ResNet50 seems to be confused by it.

**Papers**

* MobileNet: [Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/pdf/1704.04861.pdf)
* ResNet50: [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
* InceptionV3:[Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)

### 1. Model Comparison

|    Model    |  Size | Parameters | Depth |
|:-----------:|:-----:|:----------:|:-----:|
|  MobileNet  | 17 MB |  4,253,864 |   88  |
|   ResNet50  | 99 MB | 25,636,712 |  168  |
| InceptionV3 | 92 MB | 23,851,784 |  159  |

### 2. How to run the code:

1. Select the network by changing the `choice` value in `main.py`:
```sh
# 1: MobileNet, 2: ResNet50, 3: InceptionV3
choice = 1
```

2. Run the `main.py`:

```sh
python  main.py
```

### 3. Requirements: 
* keras>=2.0.8
* tensorflow>=1.3.0 or tensorflow-gpu>=1.3.0
* numpy>=1.13.1
* python >= 3.5



[//]: # (Image Reference)
[image1]: ./light1.jpg
