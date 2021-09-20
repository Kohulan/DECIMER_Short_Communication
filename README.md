[![License](https://img.shields.io/badge/License-MIT%202.0-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-blue.svg)](https://GitHub.com/Kohulan/DECIMER_Short_Communication/graphs/commit-activity)
[![GitHub issues](https://img.shields.io/github/issues/Kohulan/DECIMER_Short_Communication.svg)](https://GitHub.com/Kohulan/DECIMER_Short_Communication/issues/)
[![GitHub contributors](https://img.shields.io/github/contributors/Kohulan/DECIMER_Short_Communicationr.svg)](https://github.com/Kohulan/DECIMER_Short_Communication/graphs/contributors/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5155037.svg)](https://doi.org/10.5281/zenodo.5155037)
[![DOI](https://zenodo.org/badge/391955095.svg)](https://zenodo.org/badge/latestdoi/391955095)

# Performance of chemical structure string representations for chemical image recognition using transformers

- The use of molecular string representations for deep learning in chemistry has been steadily increasing in recent years. The complexity of existing string representations, and the difficulty in creating meaningful tokens from them, lead to the development of new string representations for chemical structures. In this study, the translation of chemical structure depictions in the form of bitmap images to corresponding molecular string representations was examined. An analysis of the recently developed DeepSMILES and SELFIES representations in comparison with the most commonly used SMILES representation is presented where the ability to translate image features into string representations with transformer models was specifically tested. The SMILES representation exhibits the best overall performance whereas SELFIES guarantee valid chemical structures. DeepSMILES perform in between SMILES and SELFIES, InChIs are not appropriate for the learning task. All investigations were performed using publicly available datasets and the code used to train and evaluate the models has been made available to the public.


[![GitHub Logo](https://github.com/Kohulan/DECIMER_Short_Communication/blob/main/Abstract_S.png?raw=true)](https://github.com/Kohulan/DECIMER_Short_Communication)


## Usage
-  To use scripts available here, please clone the repository in your local hard disk and you can continue working with it.
-  The datasets are available in zenodo as SMILES, you can use the provided [SMILES Depictor](https://github.com/Kohulan/DECIMER_Short_Communication/blob/main/src/Java/SmilesDepictor.java) java code to generate the image files.

##### We recommend to use DECIMER inside a Conda environment to facilitate the installation of the dependencies.
- Conda can be downloaded as part of the [Anaconda](https://www.anaconda.com/) or the [Miniconda](https://conda.io/en/latest/miniconda.html) plattforms (Python 3.7). We recommend to install miniconda3. Using Linux you can get it with:
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```

### More on using the model to train and evaluate please refer to our [DECIMER Image Transformer](https://github.com/Kohulan/DECIMER-Image_Transformer) repository

## License:
- This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/Kohulan/DECIMER_Short_Communication/main/LICENSE?token=AHKLIF2YYNOXJELXZL5GNYTBJLTU6) file for details

## Citation

- Rajan K, Steinbeck C, Zielesny A. Performance of chemical structure string representations for chemical image recognition using transformers. ChemRxiv. Cambridge: Cambridge Open Engage; 2021;  This content is a preprint and has not been peer-reviewed.

## Acknowledgement
- We are grateful for the company @Google making free computing time on their TensorFlow Research Cloud infrastructure available to us. 

## Author: [Kohulan](https://kohulanr.com)

[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/raw/master/assets/DECIMER.gif)](https://decimer.ai)

## Project Website: [DECIMER](https://decimer.ai)

## Research Group
[![GitHub Logo](https://github.com/Kohulan/DECIMER-Image-to-SMILES/blob/master/assets/CheminfGit.png)](https://cheminf.uni-jena.de)
