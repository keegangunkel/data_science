from cmath import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
from sklearn.metrics import r2_score
from scipy.stats import linregress


########################### LAB 4 ###########################


path = '' 
filename = 'BodyFat.xls' #finding file
graph_data_frame = pd.read_excel(path + filename) #reading in the excel sheet


x_body_fat = graph_data_frame['BODYFAT'] # pulling bodyfat column to use as X
y_density = graph_data_frame['DENSITY'] # pulling density column to use as y

x_height = graph_data_frame["HEIGHT"] # pulling density column to use as x
y_weight = graph_data_frame["WEIGHT"] # pulling weight column to use as y



#linear regression function
def linear_regression(x, y):     
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    slope_num = ((x - x_mean) * (y - y_mean)).sum() 
    slope_den = ((x - x_mean)**2).sum()
    slope = slope_num / slope_den #slope equation
    
    y_int = y_mean - (slope*x_mean) #y-intercept equation
    
    r_val_num = ((x - x_mean) * (y - y_mean)).sum() 
    r_val_den = sqrt(((x - x_mean)**2).sum() * ((y - y_mean)**2).sum())
    r_val = r_val_num/r_val_den 
    r_val = r_val**2 #r-value equation

    reg_line = 'y = {}x + {}'.format(round(slope, 4), round(y_int, 4))
    
    return (y_int, slope,reg_line, r_val) #returning values

#prediction function
def predict(y_int, slope, new_x):  #predicting the y value on any given x 
    y = y_int + slope * new_x
    return y

y_int_body_fat, slope_body_fat, reg_line_body_fat, r_val_body_fat = linear_regression(x_body_fat, y_density) #assigning the return values using body fat and density to usuable variables


y_int_weight, slope_weight, reg_line_weight, r_val_weight = linear_regression(x_height, y_weight) #assigning the return values using weight and height to usuable variables


print("\nBody fat vs Denstiy")
print(reg_line_body_fat,"\n","r2 val:", np.round(r_val_body_fat, 4).real) 
print("Y prediction:",predict(y_int_body_fat, slope_body_fat, 254)) #predicting a y value of an x that doesn't have a data point in the excel file

print("\nHeight vs Weight")
print(reg_line_weight,"\n","r2 val:", np.round(r_val_weight, 4).real )
print("Y prediction:",predict(y_int_weight, slope_weight, 90)) #predicting a y value of an x that doesn't have a data point in the excel file


body_fat_density_graph= plt.plot(x_body_fat, y_density, 'o')
plt.plot(x_body_fat, slope_body_fat*x_body_fat+y_int_body_fat, label="Regression Line") #Regression line + label
leg = plt.legend(loc='upper center') #legend + location

plt.title('Body Fat vs Density')
plt.ylabel('Density')
plt.xlabel('Body Fat')

plt.show()


height_weight_graph = plt.plot(x_height, y_weight, 'o')
plt.plot(x_height, slope_weight*x_height+y_int_weight, label= "Regression Line")#Regression line + label
weight_leg = plt.legend(loc='upper center') #legend + location
plt.title('Weight vs Height')
plt.ylabel('Height')
plt.xlabel('Weight')

plt.show() #shows graph


########################### EVALUATION ###########################
# 
#
# Compared to Lab 3 excel results the python results appear to be 
# exactly the same when rounded off to the ten thousandth. I could
# just be imagining things but sometimes it seemed python rounded
# differently than excel does. This observation could be easily
# skewed as I noticed it in many decimal points beyond the ten
# ten thousandth
#
#
##################################################################



