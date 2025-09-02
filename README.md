# SARathi-AI-ImageProcessing

SARathi is an AI-driven project focused on **denoising and enhancing satellite/SAR (Synthetic Aperture Radar) images**.  
The system leverages **deep learning and computer vision techniques** to improve image quality, remove noise, and make features more interpretable for downstream analysis.

---

## Features
- AI-powered **non-local means denoising** and adaptive noise reduction.  
- **Contrast and sharpness enhancement** for better visibility of terrain features.  
- Modular pipeline using **Python, OpenCV, and scikit-image**.  
- Extensible framework for **integration with ML models** for classification and segmentation.  

---

## Tech Stack
- **Python 3.12**  
- **OpenCV** – image processing  
- **scikit-image** – denoising, restoration, enhancement  
- **NumPy / Matplotlib** – numerical operations and visualization  
- *(Optional future integration: PyTorch/TensorFlow for generative AI models)*  

---

## Project Workflow
1. Input raw satellite/SAR image.  
2. Apply **AI-driven denoising filters**.  
3. Perform **enhancement (contrast, edge sharpness)**.  
4. Output clean, high-quality image.  

---

## How to Run
```bash
# Clone this repository
git clone https://github.com/<your-username>/SARathi-AI-ImageRestoration.git
cd SARathi-AI-ImageRestoration

# Install dependencies
pip install -r requirements.txt

# Run the script
python SARathi_codeblock.py
