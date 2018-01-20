a=[1,2,4,3,5]
b=[1,3,3,2,5]

import numpy as np



mean_of_x=sum(a)/len(a)
mean_of_y=sum(b)/len(b)
centroid=(mean_of_x,mean_of_y)
print(centroid)



def slope(x,y):
    numerator=[]
    denominator=[]

    for i,j in zip(x,y):
        numerator.append((i-mean_of_x)*(j-mean_of_y))



    for i in x:
        denominator.append((i-mean_of_x)**2)

    return float("{0:.4f}".format(sum(numerator)/sum(denominator)))


def y_intercept(x,y,z):
    return float("{0:.4f}".format(x-(y*z)))



print("line equation is y = {}x {}".format(slope(a,b),y_intercept(mean_of_y,slope(a,b),mean_of_x)))



def predicted_values(x):
    predicted_value=[]
    for i in x:

        predicted_value.append(slope(a, b)*i+y_intercept(mean_of_y, slope(a, b), mean_of_x))
    return predicted_value
print(predicted_values(a))



def Error(predicted,observed):
    error=[]
    for i,j in zip(predicted,observed):
        error.append((i-j)**2)
    return error

print(sum(Error(predicted_values(a),b)))   #our aim is to minimize this value


print(np.array([1, 2, 3])*np.array([ 2.12867713])+np.array([-0.85235667])-np.array([1, 2, 3]))

# (3.0, 2.8)
# line equation is y = 0.8x 0.4
# [1.2000000000000002, 2.0, 3.6, 2.8000000000000003, 4.4]
# 2.4
# [ 0.27632046  1.40499759  2.53367472]
