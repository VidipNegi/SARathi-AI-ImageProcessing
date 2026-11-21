# SARathi

A prototype that denoises a SAR (Synthetic Aperture Radar) satellite image, marks likely water with a simple threshold, and writes a short text summary with GPT-2. It is a single Python script, `sarathi.py`.

## What the script does

1. Reads the first band of a SAR GeoTIFF with rasterio.
2. Reduces speckle noise with Non-Local Means denoising from scikit-image.
3. Normalises the denoised image and marks pixels below a fixed value of 0.3 as water.
4. Saves a side-by-side picture (original and detected water) as `sarathi_water_detection.png` in the folder you run it from, and tries to open it.
5. Generates a short text insight with GPT-2 from a fixed prompt.

## Tech stack

- Python
- rasterio and NumPy for reading and handling the GeoTIFF
- scikit-image for Non-Local Means denoising
- matplotlib for the output picture
- transformers and PyTorch for the GPT-2 text step

## Files in this repo

- `sarathi.py`: the script
- `README.md`: this file

Planned, not in the repo yet: `requirements.txt`, a sample input image, an example output image and project notes.

## Getting started

1. Clone the repository: `git clone https://github.com/VidipNegi/SARathi-AI-ImageProcessing`
2. Install the packages listed under Tech stack yourself (there is no `requirements.txt` yet).
3. Open `sarathi.py` and change the `sar_file` path near the top to your own GeoTIFF. See Limits.
4. Run `python sarathi.py`.

## Limits

- No measured results yet. Nothing here has been scored against reference data.
- No licence has been added.
- The input path in `sarathi.py` is hardcoded to a folder on the author's Windows machine. The script exits if that file is missing, so change it before running.
- The water threshold (0.3) is a fixed demo value, not tuned or validated.
- The GPT-2 text comes from a fixed prompt and does not read the image, so it is not an analysis of the result.
