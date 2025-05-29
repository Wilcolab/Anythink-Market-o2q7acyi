import base64
import io
import pytest
from PIL import Image
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def create_test_image():
    """Create a simple RGB image for testing purposes."""
    img = Image.new("RGB", (10, 10), color=(128, 128, 128))
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)
    return buf

def test_black_white_filter():
    # Upload the image
    img_buf = create_test_image()
    response = client.post("/upload", files={"image": ("test.jpg", img_buf, "image/jpeg")})
    assert response.status_code == 200
    # Extract image_id from the response HTML
    html = response.text
    start = html.find('name="image_id" value="') + len('name="image_id" value="')
    end = html.find('"', start)
    image_id = html[start:end]
    assert image_id

    # Apply the Black & White filter
    response = client.post("/api/apply-filter", data={"image_id": image_id, "selected_filter": "black_white"})
    assert response.status_code == 200
    data = response.json()
    assert "image_data" in data
    assert data["filter_name"] == "Black & White (binary)"

    # Decode and check the result is binary
    img_data = data["image_data"].replace("data:image/jpeg;base64,", "")
    img_bytes = base64.b64decode(img_data)
    img = Image.open(io.BytesIO(img_bytes)).convert("L")
    pixels = list(img.getdata())
    # All pixels should be either 0 or 255
    assert all(p in (0, 255) for p in pixels) 