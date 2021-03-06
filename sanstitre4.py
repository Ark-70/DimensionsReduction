# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:47:49 2020

@author: julien
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import manifold, datasets, decomposition, discriminant_analysis
from mpl_toolkits.mplot3d import Axes3D
 
digits = datasets.load_digits()
X = digits.data
y = digits.target
n_samples, n_features = X.shape
 
cs = (y/10.)-0.1
cs1=cs
sorted(cs1, reverse = False)
def embedding_plot(X, title):
    x_min, x_max = np.min(X, axis=0), np.max(X, axis=0)
    X = (X - x_min) / (x_max - x_min)
 
    plt.figure()
    ax = plt.subplot(aspect='equal')
    sc = ax.scatter(X[:,0], X[:,1], lw=0, s=40, c=color)
    shown_images = np.array([[1., 1.]])

    for i in range(X.shape[0]):
        if np.min(np.sum((X[i] - shown_images) ** 2, axis=1)) < 1e-2: continue
        shown_images = np.r_[shown_images, [X[i]]]
        ax.add_artist(offsetbox.AnnotationBbox(offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r), X[i]))

    plt.xticks([]), plt.yticks([])
    plt.title(title)
 
def embedding_plot_3d(X, title):
    x_min, x_max = np.min(X, axis=0), np.max(X, axis=0)
    X = (X - x_min) / (x_max - x_min)
    
    plt.figure()
    ax = plt.subplot(111, projection='3d')
    sc = ax.scatter(X[:,0], X[:,1], X[:,2], lw=0, s=10, c=color)
    
    plt.title(title)

colors = ['mediumvioletred','indigo','blueviolet','navy','seagreen','darkgreen','yellowgreen','greenyellow','yellow','orangered']
color = [colors[i] for i in y]

	
X_pca = decomposition.PCA(n_components=2).fit_transform(X)
#embedding_plot_3d(X_pca, "PCA dans un espace réduit à trois dimensions")
embedding_plot(X_pca, "PCA dans un espace réduit à deux dimensions")
plt.show()


	
X_lda = discriminant_analysis.LinearDiscriminantAnalysis(n_components=2).fit_transform(X, y)
#embedding_plot_3d(X_lda, "LDA dans un espace réduit à trois dimensions")
embedding_plot(X_lda, "LDA dans un espace réduit à deux dimensions")
 
plt.show()