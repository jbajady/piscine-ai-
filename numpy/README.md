# NumPy Folder Overview

This folder is designed to help you understand practical NumPy usage through a sequence of exercises. NumPy is a core Python package for numerical computing and is used extensively in data science, machine learning, and the wider Python ecosystem.

## Why NumPy matters

- NumPy provides efficient, optimized array structures for numerical data.
- Many libraries such as scikit-learn, pandas, and TensorFlow rely on NumPy internally.
- NumPy helps speed up workflows by using vectorized operations instead of Python loops.
- It supports advanced features like broadcasting, slicing, random sampling, and statistical analysis.

## Learning Objectives

- Design efficient data structures using NumPy arrays for numerical computations.
- Implement array operations including slicing, broadcasting, and vectorization.
- Analyze real-world datasets using statistical functions and data manipulation methods.
- Use random number generation and distribution sampling for data science applications.
- Optimize memory usage and performance by choosing proper NumPy data types.

## Submission Structure

The expected structure for this folder is:

- `ex00/`
  - `requirements.txt`
  - `Notebook_ex00.ipynb`
- `ex01/`
  - `ex01.py` or `Notebook_ex01.ipynb`
- `ex02/`
  - `ex02.py` or `Notebook_ex02.ipynb`
- `ex03/`
  - `ex03.py` or `Notebook_ex03.ipynb`
- `ex04/`
  - `ex04.py` or `Notebook_ex04.ipynb`
- `ex05/`
  - `ex05.py` or `Notebook_ex05.ipynb`
- `ex06/`
  - `ex06.py` or `Notebook_ex06.ipynb`
- `ex07/`
  - `ex07.py` or `Notebook_ex07.ipynb`
- `ex08/`
  - `ex08.py` or `Notebook_ex08.ipynb`
  - `data/`
    - `winequality-red.csv`
    - `winequality.names`
- `ex09/`
  - `ex09.py` or `Notebook_ex09.ipynb`
  - `data/`
    - `model_forecasts.txt`

## Exercise Summary

### Exercise 0: Environment and libraries

- Set up a Python virtual environment using Python 3.x (>= 3.9 recommended).
- Install `numpy` and `jupyter`.
- Save installed packages to `requirements.txt`.
- Launch Jupyter Notebook or JupyterLab on port `8891`.
- Create `Notebook_ex00.ipynb`.
- In the notebook, add a first cell with `# H1 TITLE` and `## H2 TITLE`.
- In the second cell, run:

```python
print("Buy the dip ?")
```

### Exercise 1: Your first NumPy array

- Create a NumPy array containing: integer, float, string, dictionary, list, tuple, set, and boolean.
- Iterate over the array and print the type of each element using:

```python
for i in your_numpy_array:
    print(type(i))
```

### Exercise 2: Zeros

- Create a NumPy array of 300 zeros without filling it manually.
- Reshape it to `(3, 100)`.

### Exercise 3: Slicing

- Create a NumPy array containing integers from `1` to `100`.
- Create an array of all odd integers using slicing.
- Create an array of all even integers reversed.
- Set every third element (starting with the second) to `0` using array slicing.

### Exercise 4: Random

- Set the random seed to `888`.
- Generate a 1-D array of size `100` with a normal distribution.
- Generate an `8x8` array of random integers from `1` to `10`.
- Generate a `4x2x5` array of random integers from `1` to `17`.

### Exercise 5: Split, concatenate, reshape arrays

- Build arrays from `1` to `50` and `51` to `100`.
- Concatenate them to form `1` through `100`.
- Reshape the result to a `10x10` matrix.
- Print the created arrays.

### Exercise 6: Broadcasting and slicing

- Create a `9x9` array of ones with type `np.int8`.
- Use slicing to build a structured pattern with zeros inside the border.
- Use broadcasting to generate a multiplication result from two 1-D arrays.

### Exercise 7: NaN handling

- Create a grade matrix with missing values (`np.nan`) in the first exam.
- Use `np.where` to create a third column that selects the first exam grade when available, otherwise uses the second exam grade.
- Do this without loops or conditionals.

### Exercise 8: Wine dataset analysis

- Load the red wine dataset from `ex08/data/winequality-red.csv` using `np.genfromtxt` with delimiter `;`.
- Use `np.float32` to optimize memory.
- Display rows `2`, `7`, and `12` as a 2-D array.
- Check whether any wine has alcohol percentage greater than `20%`.
- Compute the average alcohol percentage excluding `np.nan`.
- Calculate pH statistics: min, max, 25th percentile, 50th percentile, 75th percentile, and mean.
- Compute the average quality of wines with the lowest `20%` of sulphate content.
- Compute mean values for the best-quality and worst-quality wines.

### Exercise 9: Football tournament

- Load the model forecast matrix from `ex09/data/model_forecasts.txt`.
- Use permutations from `itertools` and NumPy array operations to identify the most interesting matchups.
- The objective is to minimize the sum of squared score differences for paired teams.
- Generate the output pair matrix without using Python loops.

## Notes

- Exercise 0 must use a Jupyter notebook.
- Exercises 1–9 may be submitted as `.py` scripts or `.ipynb` notebooks.
- Prefer NumPy operations over Python loops for both speed and readability.
- Choose appropriate data types (`np.int8`, `np.float32`, etc.) to optimize memory.
- Handle missing values with NumPy utilities such as `np.isnan`, `np.nanmean`, and `np.where`.

## Recommended tools

- Python 3.x
- NumPy
- Jupyter or JupyterLab

## Recommended versions

- NumPy `1.18.1` was used in the exercise description.
- Use the latest stable NumPy version if possible.
