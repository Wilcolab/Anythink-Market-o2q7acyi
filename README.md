# Image Filter App

A modern web application that allows you to upload images and apply various filters to them, all without saving anything to disk.

## Features

- Easy image upload with drag-and-drop support
- 12 different image filters including:
  - Grayscale
  - Blur
  - Emboss
  - Sharpen
  - Sepia tone
  - And more!
- Real-time side-by-side preview of filtered images
- Download functionality for processed images
- Modern responsive UI
- Zero disk storage (all operations happen in memory)

## Key Technical Aspects

- **Memory-Only Operation**: No images are saved to disk at any point
- **Real-Time Filtering**: All filters are applied instantly with side-by-side preview
- **Base64 Encoding**: Images are stored and transferred as base64-encoded strings
- **Optimized Image Processing**: Large images are automatically resized for better performance

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/image-filter-app.git
cd image-filter-app
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:

```bash
python main.py
```

2. Open your web browser and go to: http://localhost:8000
3. Upload an image by clicking the "Select Image" button or by dragging and dropping
4. Click on any filter to instantly see the result
5. Download the filtered image if desired

## Architecture

- **Frontend**: Modern HTML/CSS/JS with responsive design
- **Backend**: FastAPI with Jinja2 templating
- **Image Processing**: PIL/Pillow library for applying filters
- **Data Flow**:
  1. Images are uploaded and stored in memory (never on disk)
  2. Filters are applied to in-memory images
  3. Filtered images are sent to the browser as base64-encoded data
  4. Downloads are generated on-demand directly from memory

## Customization

You can easily add more filters by:

1. Adding a new entry to the `FILTERS` dictionary in `main.py`
2. Implementing the filter logic in the `api_apply_filter` function

Example for adding a new "Sepia" filter:

```python
# Add to FILTERS dictionary
"sepia": "Sepia tone effect"

# Add to filter logic
elif selected_filter == "sepia":
    # Your implementation here
```

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Pillow (PIL)
- **Templating**: Jinja2

## Python Code Standards

To ensure code quality and maintainability, follow these Python code standards:

- **Formatting:** Use [PEP 8](https://www.python.org/dev/peps/pep-0008/) as the base style guide. Use tools like `black` or `autopep8` for automatic formatting.
- **Naming:**
  - Variables, functions, and methods: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
- **Imports:**
  - Standard library imports first, then third-party, then local imports. Separate each group with a blank line.
  - Use absolute imports where possible.
- **Type Hints:** Use type hints for function signatures and variable declarations where practical.
- **Docstrings:**
  - Use triple double-quoted strings for module, class, and function docstrings.
  - Describe parameters, return values, and exceptions.
- **Error Handling:**
  - Use specific exception types.
  - Avoid bare `except:` clauses.
- **Testing:**
  - Use `pytest` or `unittest` for automated tests.
  - Name test files and functions clearly (e.g., `test_feature.py`, `def test_feature_behavior():`).
- **Best Practices:**
  - Keep functions small and focused.
  - Avoid global variables.
  - Use list comprehensions and generator expressions where appropriate.
  - Prefer f-strings for string formatting.

Adhering to these standards helps keep the codebase clean, readable, and easy to maintain.

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
