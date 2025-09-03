# SARathi 
SARathi: AI-Powered Satellite Image Analysis
# Overview

SARathi is a powerful and efficient Python-based pipeline for intelligent preprocessing of Synthetic Aperture Radar (SAR) imagery. Built to bridge the gap between raw geospatial data and practical, real-world applications, this project leverages a combination of computer vision and AI techniques to deliver clean, actionable insights from satellite data. SARathi is designed for reliability and speed, making it an ideal tool for use in critical fields such as disaster management, urban planning, and environmental monitoring.
Key Differentiators

    Cloud-Independent Operation: Unlike traditional aerial or optical imagery, SAR data is not affected by cloud cover or weather conditions, making it a reliable source for continuous monitoring.

    Actionable Intelligence: SARathi doesn't just process data; it uses Generative AI to provide a concise, human-readable summary, transforming complex analysis into immediate, actionable insights.

    Modular & Scalable: The pipeline is built with a modular architecture, allowing it to be easily adapted for future applications like crop classification, land-use mapping, and seasonal analysis.

# Features

    Noise Reduction: Applies a robust Non-Local Means (NL-Means) algorithm to effectively denoise SAR images, ensuring feature clarity and accuracy for downstream analysis.

    Image Enhancement: Optimizes images through contrast enhancement and sharpening to highlight key features like water bodies and land boundaries.

    AI-Driven Insights: Integrates a lightweight Generative AI model (GPT-2) to automatically generate two-line summaries of the processed images, providing quick, intelligent interpretations.

    Streamlined Pipeline: A simple and modular Python-based pipeline that is easy to understand, modify, and integrate into larger systems.

# Tech Stack

    Python 3.12: The core programming language for the pipeline.

    rasterio: For efficient reading and manipulation of geospatial data formats like GeoTIFF.

    scikit-image: Utilized for advanced image processing, including the Non-Local Means denoising algorithm.

    transformers: Enables the integration of pre-trained Generative AI models for automated text generation.

    Pillow (PIL): Used for general image handling and saving the processed output.

    NumPy: Provides essential numerical operations for data manipulation.

# Project Structure
```
SARathi/
│── sarathi.py              # The core SAR processing and analysis pipeline
│── requirements.txt        # List of all Python dependencies
│── README.md               # Comprehensive project documentation (this file)
│── data/                   # (Optional) Directory for sample SAR images
│   └── sample_input.tif
│── output/                 # Directory for storing generated results (denoised/analyzed images)
│   └── sar_water_detection.png
│── docs/                   # Contains documentation, project notes, and references
│   └── project_notes.md
│── .gitignore              # Specifies files to be ignored by Git
```


# Getting Started

To get a local copy of the project up and running, follow these steps:

    Clone the repository:

    git clone (https://github.com/VidipNegi/SARathi-AI-ImageProcessing)

    Navigate to the project directory:

    cd SARathi

    Install the dependencies:

    pip install -r requirements.txt

    Run the main script:

    python sarathi.py

This will execute the pipeline, process the sample data, and save the results in the output/ directory.
