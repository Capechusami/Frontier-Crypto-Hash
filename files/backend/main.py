from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import hashlib

app = FastAPI(title="Hashing Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HashResponse(BaseModel):
    original: str
    original_hash: str
    modified: str
    modified_hash: str
    observation: str

def sha256_str(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

@app.get("/hash", response_model=HashResponse)
def get_hashes():
    original = "mydata123"
    modified = "mydata124"  # one-character change
    original_hash = sha256_str(original)
    modified_hash = sha256_str(modified)
    observation = (
        "Changing a single character causes a completely different SHA-256 hash "
        "(avalanche effect)."
    )
    return HashResponse(
        original=original,
        original_hash=original_hash,
        modified=modified,
        modified_hash=modified_hash,
        observation=observation,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)