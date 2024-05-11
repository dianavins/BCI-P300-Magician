import pandas as pd
import matplotlib.pyplot as plt
#*Best code I have for analyzing the data
def plot_line_graph(csv_file_path, title="Line Graph", x_label="Time", y_label="Values"):
    # Read CSV file into a pandas DataFrame, skipping the header rows with '#' at the beginning
    try:
        df = pd.read_csv(csv_file_path, comment='#')
    except pd.errors.ParserError as e:
        print(f"Error reading CSV file: {e}")
        return

    # Extract Time and Y-axis data columns
    time_data = df['Time']
    y_data_columns = ['LE', 'F4', 'C4', 'P4', 'P3', 'C3', 'F3', 'Pz']

    # Normalize the data using Min-Max scaling
    #! I took out the normalizing part of this because for this type of data, we should NOT be normalizing it
    df_normalized = df[y_data_columns]#.apply(min_max_scaling)

    # Create subplots with shared x-axis and y-axis
    fig, axes = plt.subplots(nrows=len(y_data_columns), sharex=True, sharey=True, figsize=(15, 2 * len(y_data_columns)))

    # Plot each column on a different subplot
    for i, column in enumerate(y_data_columns):
        axes[i].plot(time_data, df_normalized[column])

        # Set labels and title for each subplot
        axes[i].set_xlabel(x_label)
        axes[i].set_ylabel(y_label)
        axes[i].set_title(f"{title} - {column}", fontsize=8)

    # Adjust layout to decrease space between subplots
    plt.subplots_adjust(hspace=0, bottom=0.03, top=0.975)  # Adjust the hspace parameter

    # Show the plot
    plt.show()

# Example usage
csv_file_path = 'sample25.csv'  # Replace with the actual path to your CSV file

plot_line_graph(csv_file_path)
