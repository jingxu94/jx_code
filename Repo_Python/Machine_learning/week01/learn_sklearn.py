from sklearn.datasets import load_boston,load_iris

boston = load_boston()
print(boston.data.shape)

iris = load_iris()
print(iris.data.shape)
print(iris.target.shape)
print(list(iris.target_names))