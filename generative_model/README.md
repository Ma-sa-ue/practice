# Generative Model

Here I uploaded codes mainly about generative model.  

## Importance weighted auto encoder

Importance weighted autoenocder in Tensorflow

This code is strongly inspired by this page.(https://jmetzen.github.io/2015-11-27/vae.html)

In that page,there is a good "VAE" code written by Jan Hendrik Metzen.

I've changed some points. The main differences are as follows.

* Use batch normalization
* Make it possible to sample many times.
* Use importance weighted sampling.(See the papaer written by Y.Burda https://arxiv.org/abs/1509.00519 in detail)