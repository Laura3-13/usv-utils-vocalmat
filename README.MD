# USV-Utils (VocalMat): Mouse USV Analysis Library

A Python tool for processing and analyzing mouse ultrasonic vocalizations (USVs) detected using **VocalMat** software, an open-source framework for automated USV detection and classification. This library automatically processes USV data into meaningful statistics, such as **USV duration** and **calls per minute**, and performs **statistical comparisons** between two experimental groups.


---


## 🎯 **Key Features**
- 📃 **USV Data Classification**: Removes calls labeled as noise, and calculates USV duration and calls per minute (CPM).
- 📊 **Statistical Analysis**: Performs automated statistical tests between two groups.
- 📂 **File Management**: Automatically reads USV Excel files from specified folders.
- ⚙️ **Automation Ready**: Minimal setup - just provide the path and run the main script.


---


## 💻 **Installation Guide**

### **Option 1. Clone the Repository Using Git (Recommended)**
1. **Clone the Repository**
```bash
git clone https://github.com/Laura3-13/usv-utils-vocalmat.git
cd usv-utils-vocalmat # This is the folder created after cloning
```

2. **Create a Conda Environment**
``` bash
conda create -n usv-utils python=3.10
```

3. **Activate the Environment**
``` bash
conda activate usv-utils
```

4. **Install Required Libraries**
``` bash
pip install -r requirements.txt
```

---


### **Option 2. Download the Repository as a ZIP File**
1. **Download the Repository**
- Visit the [USV-Utils GitHub Repository](https://github.com/Laura3-13/usv-utils-vocalmat).
- Click the green **Code** button.
- Select **Download ZIP**.

2. **Extract the ZIP File**
- Extract the contents to a folder on your computer.

3. **Navigate to the Extracted Folder**
```bash
cd path_to_extracted_folder/usv-utils-vocalmat # Replace "path_to_extracted_folder" with your actual folder path
```

4. **Create a Conda Environment**
```bash
conda create -n usv-utils python=3.10
```

5. **Activate the Environment**
```bash
conda activate usv-utils
```

6. **Install Required Libraries**
```bash
pip install -r requirements.txt
```


---


## 📦 **How to Use**
### **1. Organize Your Data Files**
The script is designed to compare **two groups**. By default, the groups are:
- **WT** (Wild-type)
- **KO** (Knockout)

However, you can replace **WT** and **KO** with other group names (e.g., `GroupA` and `GroupB`), as long as the files follow this structure:
- Each group name must be consistent and followed by **numbers**.

### **File Naming Rules**
Your files must follow this naming convention:
- `GroupName1.xlsx`, `GroupName2.xlsx`...

**Example:**

- For **WT** and **KO**:
```bash
WT1.xlsx, WT2.xlsx, WT3.xlsx, KO1.xlsx, KO2.xlsx, KO3.xlsx
```
- For other groups, such as **GroupA** and **GroupB**:
```bash
GroupA1.xlsx, GroupA2.xlsx, GroupA3.xlsx, GroupB1.xlsx, GroupB2.xlsx, GroupB3.xlsx
```
Ensure all **USV Excel files** are stored in a single folder.

### **2. Add Your File Path in `__main__vocalmat.py`**
Open the `__main__vocalmat.py` file and change the variable `root` to point to your folder containing the USV files:
```python
# Get your USV files from your path of choice
root = "INTRODUCE YOUR PATH HERE"

# Change group names here if needed
kosnames = utils.get_excel_file_names(root, "KO") # Replace "KO" with your group name
wtsnames = utils.get_excel_file_names(root, "WT") # Replace "WT" with your group name
```
If you change `KO` and `WT` to other names (e.g., `GroupA` and `GroupB`), make sure your filenames match this new naming scheme.

### **3. Run the Main Script**
Run the following command in your terminal:
```bash
python src/__main__vocalmat.py
```
### **4. Output**
The script will perform the following tasks:
1. **Read** and **process** the USV files for both groups.
2. **Remove** the calls labeled as noise by the VocalMat software.
3. **Generate summary data:**
    - **USV duration** (mean and SEM).
    - **Calls per minute** (CPM).
4. **Print the summaries** to the terminal for both groups.
5. **Provide comparisons** (Group1 vs Group2) with statistical analysis.
6. **Save results** as files in a folder called `Python_files`:
    - **Excel files:** Summary data for each group and combined results.
    - **Statistical Results:** A **text file** containing the statistical test results.
    - **Bar graphs:** two **bar graph images** (one for **USV duration** and one for **Calls per minute**).

### **Notes**
- The script assumes a **3-minute recording duration** to calculate "calls per minute (CPM)".
- To analyze recordings of a different duration, modify the value of `RECORDING_DURATION_MINUTES` in the `CPM()` function of `data_workflow_vocalmat.py`.


---


## 📄 **Expected Input Data Format**
- **VocalMat** output files in Excel (``.xlsx``) format.


---


## 📑 **Project Structure**
```bash
usv-utils-vocalmat/
│
├── src/                            # Main source code
│   ├── __init__.py                 # Marks this directory as a Python package
│   ├── __main__vocalmat.py                 # RUN THIS FILE
│   ├── data_workflow_vocalmat.py            # Data processing and summary generation
│   ├── statistical_analysis.py      # Statistical tests (t-test, Mann-Whitney, etc.)
│   ├── plotting.py                 # Plotting functions for barplots
│   └── utils.py                    # Utility functions to fetch file names
│
├── requirements.txt                # Required libraries for the project
├── citation.ris                    # Citation file for importing into reference managers
├── README.md                       # Project documentation and setup guide
└── .gitignore                      # Files and directories to ignore in Git
```


---


## 🖋️ **Citation**

If you use this repository in your research or projects, please cite it appropriately!

On the right side of this GitHub page, you'll find a **Cite this repository** section where you can copy citations in:
- **APA** format
- **BibTeX** format (for LaTeX users)

For other reference managers, such as **EndNote**, **Zotero**, or **Mendeley**, download the `citation.ris` file directly from the repository.


---


## 🙏 Acknowledgments

This repository processes mouse USV detections generated by **VocalMat**, an open-source framework for automated USV detection and classification.

If you use VocalMat-generated data in your research, please also cite the original VocalMat publication:

Fonseca, A.H.O., Santana, G.M., Bosque Ortiz, G.M., et al. (2021). *Analysis of ultrasonic vocalizations from mice using computer vision and machine learning.* eLife, 10:e59161. DOI: [10.7554/eLife.59161](https://doi.org/10.7554/eLife.59161)

The original VocalMat software is available at: [VocalMat GitHub Repository](https://github.com/ahof1704/VocalMat)


---


## 🐭 **How It Works**
1. **Load USV Files:** Extract USV data from VocalMat Excel files and remove calls labeled as noise.
2. **Process Data:** Calculate USV duration and calls per minute (CPM).
3. **Perform Statistical Analysis:**
    - **Compare two groups:** Automatically calculates mean, standard deviation, and performs significance tests.


---


## 🔬 **About the Project**
This library was developed for **neuroscience research** involving the analysis of mouse ultrasonic vocalizations (USVs). It supports efficient batch processing, automatic statistical tests, and data visualization for **behavioral experiments**.


---