# 📘 NumPy Environment Setup (piscine-ai)

## 🎯 Objective

This project aims to:

-   Create a clean Python virtual environment\
-   Install required libraries\
-   Run Jupyter Notebook\
-   Organize a proper project structure

------------------------------------------------------------------------

## 🗂️ Project Structure

    piscine-ai/
    └── numpy/
        └── ex00/
            ├── venv/
            ├── Notebook_ex00.ipynb
            └── requirements.txtV

------------------------------------------------------------------------

## 🛠️ Step 1: Create Project Directories

``` bash
mkdir piscine-ai
cd piscine-ai

mkdir numpy
cd numpy

mkdir ex00
cd ex00
```

------------------------------------------------------------------------

## 🐍 Step 2: Create Virtual Environment

``` bash
python3 -m venv venv
```

------------------------------------------------------------------------

## ▶️ Step 3: Activate Environment

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

## 📦 Step 4: Install Dependencies

``` bash
pip install numpy
pip install jupyter
```

------------------------------------------------------------------------

## 📄 Step 5: Generate requirements.txt

``` bash
pip freeze > requirements.txt
```

------------------------------------------------------------------------

## 🚀 Step 6: Launch Jupyter Notebook

``` bash
jupyter notebook --port=8891
```

------------------------------------------------------------------------

## 📓 Step 7: Create Notebook

Create a file named:

    Notebook_ex00.ipynb

------------------------------------------------------------------------

## ✍️ Step 8: Notebook Content

### Cell 1 (Markdown)

    # H1 TITLE
    ## H2 TITLE

### Cell 2 (Code)

``` python
print("Buy the dip ?")
```

------------------------------------------------------------------------

## 🧠 Learning Goals

-   Understand virtual environments\
-   Learn Jupyter Notebook usage\
-   Practice project organization\
-   Work in a professional Python workflow


