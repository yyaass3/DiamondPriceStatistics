import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sb

Data = pd.read_csv(r"F:\py.ex\work\diamonds.csv\diamonds.csv")

# data cleaning
missingValues = Data.isnull().mean()

# correlation
matrix = pd.DataFrame(Data, columns=['carat', 'depth', 'table', 'price', 'x', 'y', 'z']).corr()

# correlation heatmap
plt.imshow(matrix, cmap='Blues')
plt.colorbar()
col = matrix.columns
plt.xticks(range(len(matrix)), col)
plt.yticks(range(len(matrix)), col)
plt.show()

# regression
regg = sb.regplot(x=Data['x'], y=Data['carat'], data=Data)
plt.show()

# swarm plot
swarm = sb.swarmplot(x=Data['carat'].head(100), y=Data['price'].head(100), data=Data.head(100))
plt.show()

# scatter plot
Data2 = pd.DataFrame(Data.head(200), columns=['carat', 'depth', 'table', 'x', 'y', 'z'])
scatt = px.scatter(Data2)
scatt.show()

# line chart
line = sb.lineplot(data=Data, x='carat', y='price')
plt.show()

# bar chart
bar = sb.barplot(data=Data, x='cut', y='price')
plt.show()

# pie chart
pie = px.pie(Data, values='price', names='cut')
pie.show()

# histogram
histogram = px.histogram(Data, x='cut', histnorm='percent', nbins=50)
histogram.show()

# probability distribution

Data3 = pd.DataFrame(Data, columns=['carat', 'depth', 'table', 'price', 'x', 'y', 'z'])

histogram2 = px.histogram(Data, x='price', histnorm='percent', nbins=50)
histogram2.show()
plot = sb.kdeplot(Data, x='price')
plt.show()
skew = Data3.skew()
kurt = Data3.kurt()
print(skew, kurt)

# descriptive statistics

# 1: mean
mean = Data3.mean()
print(mean)

# 2: std
STD = Data3.std()
print(STD)

# 3: mode
mode = Data3.mode()
print(mode)

# 4: max and min
MAX = Data3.max()
MIN = Data3.min()
print(MAX, MIN)

# 5: in total
describe = Data3.describe()
print(describe)
