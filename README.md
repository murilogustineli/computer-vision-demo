# Computer Vision Demo

Computer Vision demo for the [DataHour webinar series](https://www.analyticsvidhya.com/blog/2022/02/introducing-the-webinar-series-the-datahour/) using `PyTorch`.

**Run the Computer Vision Demo in a colab notebook**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/murilogustineli/computer-vision-demo/blob/main/cv_demo.ipynb)

⚠ _Colab provides a temporary environment: anything you do will be deleted after a while, so make sure you download any data you care about._

## Important documentation:

- [PyTorch](https://pytorch.org/)
- [Fashion MNIST GitHub repo](https://github.com/zalandoresearch/fashion-mnist)
- [Deep Learning with Python, Second Edition](https://www.manning.com/books/deep-learning-with-python-second-edition)

### Presentation slides

- [Google Slides](https://docs.google.com/presentation/d/1dm_KjBm-qY55v8wjmrtgRgqP2azxYjkmfaKipXbDtac/edit?usp=sharing)

## Project Setup Guide

To ensure our project runs smoothly on your local machine, we'll set up a dedicated Python environment and install the necessary packages.

### Prerequisites

- Python (we're using Python 3 for this project)
- pip (Python package installer)
- Either `virtualenv` or `conda` (based on your preference)

### Setup Instructions

#### 1. Setting up a virtual environment

##### Using Conda:
First, [install Anaconda or Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) based on your operating system.

Then, create a new environment:

```
conda create --name myenv python=3.8
```

Activate the environment:

```
conda activate myenv
```

##### Using virtualenv:
You can skip this step if you completed the previous step using Conda.
###### Windows:
```
pip install virtualenv
virtualenv myenv
.\myenv\Scripts\activate
```

###### Mac & Linux:
```
pip3 install virtualenv
virtualenv myenv
source myenv/bin/activate
```

#### 2. Installing the required packages

There is a `requirements.txt` file that lists all the necessary packages for this demo.

If you're using Conda, while most of the packages are available directly through pip, some might have better support or performance when installed through Conda channels:

```
conda install --file requirements.txt
```

Otherwise, install the packages using pip:

```
pip install -r requirements.txt
```

### That's it!

Your environment is now set up with all the necessary packages. You can proceed with running or developing the project.
