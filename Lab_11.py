import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# load cancer dataset from scikit learn
from sklearn.datasets import load_iris
iris = load_iris()
# cancer dataset contains .data (the X features) and .target (the Y labels)
# Here we want to just analyze the X features with PCA
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# extract all the data into a 2D array for further processing
X = df.values
print("X shape:", X.shape)

# PCA requires scaled data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
Xscaled = scaler.transform(X)
print("Xscaled shape:", Xscaled.shape)

# Do PCA for 30 features
from sklearn.decomposition import PCA
pca = PCA(n_components=4, random_state=42)
pca.fit(Xscaled)
Xpca = pca.transform(Xscaled)
print("Xpca shape:", Xpca.shape)

# Analyze how much each transformed feature explains the variability of the data
xvr = pca.explained_variance_ratio_
print("PCA variance ratios:")
top_2_var=0
i=0
for ix, v in enumerate(xvr[:]):
    if i<2:
        top_2_var+=v
        i+=1
    print("  ", ix, ":", v)
    
top_2_var*=100
print("Top 2 features account for "+str(top_2_var)+"% of variance")

# Use the cumulative sum to see how much of the data's variance (in total) is
# explained as we add more PCA features
csum = np.cumsum(xvr)
plt.plot(csum)
plt.xlabel("PCA Components")
plt.ylabel("Explained Variance")
plt.title("PCA for Iris Dataset")
plt.show()
plt.clf()
# Finally, plot the top two PCA features, properly color-coded
sns.scatterplot(x=Xpca[:, 0], y=Xpca[:, 1], hue=iris.target)
plt.savefig("Top_features_iris_dataset.png")
