# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("coba big data").getOrCreate()
df = spark.read.csv(path="train.csv", header=True, inferSchema=True)
df.show(500)
df.printSchema()

print(df.select('*'))
print(df.select('PassengerID','Survived'))
print(df.where(df['Age']>25))
print(df.where((df['Age']>25)&(df['Survived']==1)))

datadf = df.select('Age','PassengerId')
datadf.show()

df.createOrReplaceTempView('Titanic')
datasqlku = spark.sql('select Pclass, cabin,Sex from Titanic where Sex = "male"')
datasqlku.show()