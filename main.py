
from transformers import pipeline

ocr = pipeline(task="image-to-text", model="microsoft/trocr-base-handwritten")

ocr(r"C:\Users\agreu\OCR-Project\images\Copy-of-Blog-Image-Template.png")

