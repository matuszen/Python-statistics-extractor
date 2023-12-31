# Python-statistics-extractor

The project is a Python class called `ExtractStatistics` that provides methods to extract data from PDF files and perform various operations on the extracted data.

## Prerequisites

- Python 3.10 or higher
- Required Python packages installed (pandas, tabula-py)

## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/matuszen/Python-statistics-extractor.git
   ```

2. Install the required dependencies by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

To use the ExtractStatistics class, follow these steps:

Create an instance of the ExtractStatistics class by providing the path to the PDF file:

```python
file_path = "path/to/your/file.pdf"
extract_stats = ExtractStatistics(file_path)
```

Use the methods and properties of the ExtractStatistics class to extract and manipulate the data:

```python
# Get the shape of the extracted data

shape = extract_stats.shape
print(f"Data shape: {shape}")

# Get the column names of the extracted data

columns = extract_stats.columns
print(f"Columns: {columns}")

# Change the column names

extract_stats.columns = ["Column 1", "Column 2", "Column 3"]

# Get the data types of the extracted data

data_types = extract_stats.data_types
print(f"Data types: {data_types}")

# Change the data types

extract_stats.data_types = [int, str, float]

# Print the extracted data as a string

print(extract_stats)

# Access a specific column as a string

column_data = extract_stats["Column 1"]
print(column_data)
```

Customize the behavior of the ExtractStatistics class by providing optional parameters during instantiation:

```python
extract_stats = ExtractStatistics(
    file_path,
    pages="all",
    area=None,
    password=None,
    date_format="%d-%m-%Y %H:%M:%S",
    log=False
)
```

## Contributing

Contributions to this project are welcome. Here are some ways you can contribute:

Report bugs or suggest features by opening an issue.
Submit your own improvements to the project by creating a pull request.
When contributing to this repository, please first discuss the change you wish to make via the issue tracker before making a pull request.

## License

This project is licensed under the MIT License.
