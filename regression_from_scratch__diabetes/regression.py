# Copyright @ AspectDev ( Yashar Chogan )

def calc_mean(x):
    if (len(x) == 0):
        raise ValueError("empty list detected")
    return sum(x)/len(x)

def calc_slope(x_list, y_list):
    xy_total = 0
    x_total = 0
    x_mean = calc_mean(x_list)
    y_mean = calc_mean(y_list)
    for x,y in zip(x_list,y_list):
        xy_total += ((x-x_mean)*(y-y_mean))
        x_total += pow((x-x_mean), 2)
    if (xy_total == 0 or x_total == 0): 
        raise ValueError("All X,Y values are same or empty lists are fitted inside the model")
    return xy_total/x_total   

class LinearRegression:
    def __init__(self):
        self.x_list = []
        self.y_list = []
        self.slope = 0
        self.intercept = 0
        
    def fit(self, x, y):
        self.x_list = x
        self.y_list = y
        x_mean = calc_mean(self.x_list)
        y_mean = calc_mean(self.y_list)
        
        self.slope = calc_slope(self.x_list, self.y_list)
        self.intercept = y_mean - (self.slope*x_mean)
        
    def predict(self, x):
        return self.intercept + (self.slope*x)
        
x = [1,2,3,4,5]
y = [3,5,7,9,11]
    
model = LinearRegression()
model.fit(x, y)

print(f"a: {model.intercept}")    
print(f"b: {model.slope}")    
print(f"y: {model.predict(22)}")   



