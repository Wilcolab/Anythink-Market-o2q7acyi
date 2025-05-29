import base64
import io
from PIL import Image, ImageChops
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

def test_glitch_filter():
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

    # Apply the Glitch filter
    response = client.post("/api/apply-filter", data={"image_id": image_id, "selected_filter": "glitch"})
    assert response.status_code == 200
    data = response.json()
    assert "image_data" in data
    assert data["filter_name"] == "Glitch effect"

    # Decode and check the result is visually altered
    img_data = data["image_data"].replace("data:image/jpeg;base64,", "")
    img_bytes = base64.b64decode(img_data)
    filtered_img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    # Compare with original
    original_img = Image.open(create_test_image()).convert("RGB")
    diff = ImageChops.difference(filtered_img, original_img)
    # There should be at least some difference
    assert diff.getbbox() is not None 