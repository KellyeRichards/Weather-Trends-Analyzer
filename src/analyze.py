import matplotlib.pyplot as plt
import pandas as pd

#Imports the matplotlib.pyplot module for plotting graphs and the pandas library for data manipulation. These libraries are fundamental for analyzing and visualizing data.

def plot_temperature(data):     #Defines a function plot_temperature that takes a dictionary data as an argument. This function is responsible for plotting temperature trends over time.
    df = pd.DataFrame(data)     #Converts the input dictionary data into a pandas DataFrame.
    plt.figure(figsize=(10, 5)) #Initializes a new figure for plotting, with the specified size of 10 inches by 5 inches.
    plt.plot(df['date'], df['temp'], marker='o')    # Plots data from the DataFrame. It takes date as the x-axis and temp (temperature) as the y-axis. marker='o' specifies that each data point should be marked with a circle.
    plt.title('Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Celsius)')
    plt.grid(True)

    # These lines add a title to the plot, label the x-axis and y-axis, and enable a grid on the plot for better readability of the graph.

    plt.show()  #Displays the plot. Without this line, the plot would not be visible to the user.

if __name__ == "__main__":      #Ensures that the following block of code is executed only if the script is run directly.
    # Assume data is fetched and cleaned
    data = {'date': ['2021-01-01', '2021-01-02'], 'temp': [15, 16]}
    plot_temperature(data)
        #This code block is executed if the script is run directly. It sets up some sample data and calls the plot_temperature function to plot this data.


