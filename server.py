import asyncio
import os
import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from diffusers import StableDiffusionUpscalePipeline
from PIL import Image
import torch
import io
import uvicorn
import base64

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Fix Windows event loop issue
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Initialize the pipeline
model_id = "stabilityai/stable-diffusion-x4-upscaler"
logger.info(f"Attempting to load model: {model_id}")
try:
    pipeline = StableDiffusionUpscalePipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32
    )
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    exit(1)

# Move pipeline to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
logger.info(f"Moving pipeline to device: {device}")
try:
    pipeline = pipeline.to(device)
    logger.info("Pipeline moved to device successfully")
except Exception as e:
    logger.error(f"Failed to move pipeline to device: {str(e)}")
    exit(1)

@app.get("/test")
async def test():
    logger.info("Test endpoint accessed")
    return {"message": "Server is running"}

@app.post("/enhance")
async def enhance_image(file: UploadFile = File(...), prompt: str = "Coastal scene, vibrant colors, detailed, 8k"):
    logger.info(f"Received image upload: {file.filename}")
    try:
        # Read and process the uploaded image
        contents = await file.read()
        try:
            low_res_img = Image.open(io.BytesIO(contents)).convert("RGB")
            logger.info(f"Image opened successfully: {file.filename}")
        except Exception as e:
            logger.error(f"Invalid image format: {str(e)}")
            return {"error": "Invalid image format. Please upload a JPEG or PNG image."}

        # Validate image size
        if low_res_img.size[0] > 512 or low_res_img.size[1] > 512:
            logger.warning(f"Image dimensions too large: {low_res_img.size}")
            return {"error": "Image dimensions must be 512x512 or smaller"}

        # Upscale the image
        logger.info("Starting image upscaling")
        upscaled_image = pipeline(
            prompt=prompt,
            image=low_res_img,
            num_inference_steps=20,
            guidance_scale=7.5
        ).images[0]
        logger.info("Image upscaling completed")

        # Convert image to base64
        buffered = io.BytesIO()
        upscaled_image.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        logger.info("Image converted to base64")

        return {"image_base64": f"data:image/png;base64,{img_base64}"}
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    logger.info("Starting Uvicorn server on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug", timeout_keep_alive=600)