path = '' 
filename = 'haberman.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet,

data = df.iloc[:,[0,1,2]] # x attributes
survival = df.iloc[:,[3]] #y attributes
x_train, x_test, y_train, y_test = train_test_split(data,survival, test_size=0.3, random_state=42) #splitting the data into train and test, random state ensures the same split each time
dt2 = tree.DecisionTreeClassifier(max_depth = 12, max_leaf_nodes=200,min_samples_leaf=1)
dt2 = dt2.fit(data, survival)
dt_score_train = dt2.score(x_train, y_train)
dt_score_test = dt2.score(x_test, y_test)
print("Decision tree training set accuracy:","{:.2%}".format(dt_score_train))
print("Decision tree test set accuracy:","{:.2%}".format(dt_score_test))