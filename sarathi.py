import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
from skimage.restoration import denoise_nl_means, estimate_sigma
from transformers import pipeline
import torch
import warnings
import os
import webbrowser

# Suppress noisy warnings from skimage
warnings.filterwarnings("ignore", category=UserWarning)

# -------------------------------
# 1. Load SAR Data (GeoTIFF)
# -------------------------------
sar_file = r"C:\Users\USER\Documents\GenAI_Hackathon\sentinel1_sample.tif"

if not os.path.exists(sar_file):
    print(f"❌ SAR file not found: {sar_file}")
    exit()

try:
    with rasterio.open(sar_file) as src:
        sar_data = src.read(1)  # First band
        profile = src.profile
    print("✅ SAR Data Loaded | Shape:", sar_data.shape, "| CRS:", profile.get("crs"))
except Exception as e:
    print("❌ Error loading SAR file:", e)
    exit()

# -------------------------------
# 2. Preprocessing – Speckle Noise Reduction
# -------------------------------
try:
    sigma_est = np.mean(estimate_sigma(sar_data, channel_axis=None))
    denoised = denoise_nl_means(
        sar_data,
        h=1.15 * sigma_est,
        fast_mode=True,
        patch_size=5,
        patch_distance=3,
        channel_axis=None
    )
    print("✅ Denoising complete. Sigma estimate:", round(sigma_est, 4))
except Exception as e:
    print("❌ Error during denoising:", e)
    exit()

# -------------------------------
# 3. Feature Extraction – Water Detection
# -------------------------------
sar_norm = (denoised - np.min(denoised)) / (np.max(denoised) - np.min(denoised) + 1e-8)
water_mask = sar_norm < 0.3  # threshold tuned for demo
print("✅ Water detection mask generated.")

# -------------------------------
# 4. Visualization (Save Instead of Show)
# -------------------------------
try:
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    show(sar_data, ax=ax[0], cmap="gray")
    ax[0].set_title("Original SAR Data")

    ax[1].imshow(water_mask, cmap="Blues")
    ax[1].set_title("Detected Water Bodies")

    plt.tight_layout()
    output_path = os.path.join(os.getcwd(), "sarathi_water_detection.png")
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"✅ Visualization saved at: {output_path}")
    webbrowser.open(output_path)
except Exception as e:
    print("❌ Error during visualization:", e)

# -------------------------------
# 5. GenAI Insights (HuggingFace LLM)
# -------------------------------
try:
    # Use a lightweight text generator
    insight_gen = pipeline("text-generation", model="gpt2", device=0 if torch.cuda.is_available() else -1)
    prompt = "The SAR satellite image shows water bodies detected in blue. Generate an analytical insight in 2 lines."
    insight = insight_gen(prompt, max_new_tokens=40, pad_token_id=50256)[0]['generated_text']

    print("\n--- 💡 Automated Insight ---\n", insight.strip())
except Exception as e:
    print("❌ Error generating GenAI insight:", e)
