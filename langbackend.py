from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from googletrans import Translator
from fastapi.responses import JSONResponse

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware to allow cross-origin requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins (use specific URLs in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Create a Translator instance
translator = Translator()

# API endpoint to handle translation
@app.get("/translate")
async def translate(message: str, language: str):
    try:
        # Translate the message to the target language
        translated = translator.translate(message, dest=language)
        return JSONResponse(content={"translatedMessage": translated.text})
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

# For local development
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# Handler for Vercel
from mangum import Adapter
handler = Adapter(app)
