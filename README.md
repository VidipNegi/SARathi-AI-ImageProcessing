# SARathi 
AI-powered Satellite Image Analysis Project  

---

##  Overview  
SARathi is a **Python-based AI-driven image preprocessing pipeline** for satellite imagery.  
It focuses on **noise reduction, feature enhancement, and intelligent preprocessing** of geospatial images.  
The project uses **computer vision + AI techniques** to make raw satellite data cleaner and more usable for real-world applications like:  
- **Disaster management** 
- **Urban planning** 
- **Environmental monitoring** 

---

##  Tech Stack  
- **Python 3.12**  
- **OpenCV** – image transformations & enhancements  
- **scikit-image** – denoising & sigma estimation  
- **Pillow (PIL)** – image handling & saving  
- **NumPy** – numerical operations  

---

##  Features  
✅ Satellite image denoising (Non-Local Means algorithm)  
✅ Image sharpening & contrast enhancement  
✅ Preprocessing for ML/AI-based geospatial models  
✅ Simple & modular Python code  

---

##  Project Structure  
SARathi/
│── sarathi.py              # Your main script (core SAR processing pipeline)
│── requirements.txt        # List of Python dependencies
│── README.md               # Project description (we already made this)
│── data/                   # (Optional) Put sample SAR images here
│   └── sample_input.png
│── output/                 # Generated results (denoised / segmented images)
│   └── result_example.png
│── docs/                   # Documentation, project notes, references
│   └── project_notes.md
│── .gitignore              # Ignore unnecessary files (e.g., __pycache__)
