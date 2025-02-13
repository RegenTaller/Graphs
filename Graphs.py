
import matplotlib.pyplot as plt
import numpy as np

def plot_from_txt(filepath, plot_title="Graphs from TXT Data", x_label="Index", y_label="Y Value", legend_labels=("Graph 1", "Graph 2", "Graph 3")):
  
    try:
        # Read the data from the text file
        data = np.loadtxt(filepath, delimiter=',')  #Using numpy is more efficient

        # Check if the data has the expected number of columns
        if data.shape[1] != 3:
            raise ValueError("The text file must contain three columns of data.")

        # Extract the y-coordinates for each graph
        y1 = data[:, 0]
        y2 = data[:, 1]
        y3 = data[:, 2]

        # Create the x-coordinates (index of the data points)
        x = np.arange(len(y1))  # or simply, x = range(len(y1))

        # Plot the graphs
        plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
        plt.plot(x, y1, label=legend_labels[0])
        plt.plot(x, y2, label=legend_labels[1])
        plt.plot(x, y3, label=legend_labels[2])

        # Add labels and title
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(plot_title)

        # Add a legend
        plt.legend()

        # Add a grid (optional, but improves readability)
        plt.grid(True)

        # Show the plot
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
if __name__ == "__main__":
    # Create a dummy data file for testing
    dummy_data = """-12,7,9
0,9,25
0,3,10
-12,4,5
-12,7,55"""

    with open("dummy_data.txt", "w") as f:
        f.write(dummy_data)

    # Call the function to plot the data from the dummy file
    plot_from_txt("dummy_data.txt",
                  plot_title="My Awesome Graphs",
                  x_label="Data Point Index",
                  y_label="Amplitude",
                  legend_labels=("Curve A", "Curve B", "Curve C")) #Example with custom titles.