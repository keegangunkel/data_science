import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# to explore the data, which has three input x values and one output y value,
# we can plot each pair of (input, output) as three sub-plots:
data_frame = pd.read_csv('advertising.csv')
sns.pairplot(data_frame,
             x_vars = ['TV','radio','newspaper'],
             y_vars = 'sales',
             height = 7, aspect = 0.7)
#plt.show()

# split our data frame into inputs (x) and output (y)
x = data_frame [['TV','radio','newspaper']]
y = data_frame ['sales']



### TV, RADIO, AND NEWSPAPER ### 


# Create the model object and fit it to our x and y data:
model = LinearRegression()
linear_model = model.fit(x,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x)
print("\nr2 score of TV, radio, and newspaper:", r2_score(y, linear_model_predict))


### TV AND RADIO COMBINATION ###

x_1 = data_frame [['TV','radio']]
# Create the model object and fit it to our x and y data:
model_tv_radio = LinearRegression()
linear_model = model_tv_radio.fit(x_1,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_1)
print("\nr2 score of TV and radio:", r2_score(y, linear_model_predict))



### TV AND NEWSPAPER ###


x_2 = data_frame [['TV','newspaper']]
# Create the model object and fit it to our x and y data:
model_tv_newspaper = LinearRegression()
linear_model = model_tv_newspaper.fit(x_2,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_2)
print("\nr2 score of TV and newspaper:", r2_score(y, linear_model_predict))



### RADIO AND NEWSPAPER ###


x_3 = data_frame [['radio','newspaper']]
# Create the model object and fit it to our x and y data:
model_radio_newspaper = LinearRegression()
linear_model = model_radio_newspaper.fit(x_3,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_3)
print("\nr2 score of radio and newspaper:", r2_score(y, linear_model_predict))


### R2 SCORE FOR EACH SEPERATE ###

x_4 = data_frame [['radio']]
# Create the model object and fit it to our x and y data:
model_radio_newspaper = LinearRegression()
linear_model = model_radio_newspaper.fit(x_4,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_4)
print("\nr2 score of radio:", r2_score(y, linear_model_predict))


x_5 = data_frame [['newspaper']]
# Create the model object and fit it to our x and y data:
model_radio_newspaper = LinearRegression()
linear_model = model_radio_newspaper.fit(x_5,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_5)
print("\nr2 score of newspaper:", r2_score(y, linear_model_predict))



x_6 = data_frame [['TV']]
# Create the model object and fit it to our x and y data:
model_radio_newspaper = LinearRegression()
linear_model = model_radio_newspaper.fit(x_6,y)
# have the model predict y for all inputs, so we can evaluate r2:
linear_model_predict = linear_model.predict(x_6)
print("\nr2 score of TV:", r2_score(y, linear_model_predict), "\n")


