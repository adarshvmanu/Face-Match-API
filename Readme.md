# Face Matching API 

## Description
This Flask API provides an endpoint `/verify_faces` for performing face verification. It accepts two image files as input via a POST request, performs face verification using the DeepFace library, and returns the verification result as JSON.

## Setup
1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the Flask server by running the script:
   ```bash
   python app.py
   ```

2. Send a POST request to the `/verify_faces` endpoint with two image files as form-data.

### Sample cURL Request
```bash
curl -X POST -F "image1=@path/to/image1.jpg" -F "image2=@path/to/image2.jpg" http://127.0.0.1:5000/verify_faces
```

### Endpoint
- `/verify_faces` (POST): Accepts two image files as input and performs face verification using DeepFace library.

### Request Parameters
- `image1`: First image file (required).
- `image2`: Second image file (required).

### Response
The server returns the verification result as JSON:

```json
{
    "verified": true
}
```

## Configuration
- `UPLOAD_FOLDER`: Specifies the directory where uploaded image files will be saved temporarily. Default value: `uploads`.

## Notes
- Ensure that the `uploads` directory exists in the project directory to store uploaded images.
- The uploaded files will be deleted after the verification process is complete.
