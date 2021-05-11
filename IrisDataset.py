# import load_iris function from datasets module
from sklearn.datasets import load_iris

# save "bunch" object containing iris dataset and iits attributes
iris = load_iris()
type(iris)

#print the iris dataset
# Each row represents the flowers and each column represents the length and width.
print (iris.data)
iris.data.shape

# print the names of the four features
print (iris.feature_names)

print (iris.target)

# print the encoding scheme for species; 0 = Setosa , 1=Versicolor, 2= virginica
print (iris.target_names)

# Check the types of the features and response
type('iris.data')
type('iris.target')

# Check the shape of the features 
#(first dimension = (ROWS) ie number of observations, second dimensions = (COLUMNS) ie number of features)
iris.data.shape

# Check the sape of the response (single dimension matching the number of observation)
iris.target.shape

# Extract the values for features and create a list called featuresAll
featuresAll=[]
features = iris.data[: , [0,1,2,3]]
features.shape

# Extract the values for targets
targets = iris.target
targets.reshape(targets.shape[0],-1)
targets.shape

# Every observation gets appended into the list once it is read. For loop is used for iteration process
for observation in features:
    featuresAll.append([observation[0] + observation[1] + observation[2] + observation[3]])
print (featuresAll)

# Plotting the Scatter plot
import matplotlib.pyplot as plt
plt.scatter(featuresAll, targets, color='red', alpha =1.0)
plt.rcParams['figure.figsize'] = [10,8]
plt.title('Iris Dataset scatter Plot')
plt.xlabel('Features')
plt.ylabel('Targets')

Text(0,0.5,'Targets')
