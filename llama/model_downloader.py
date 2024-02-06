import os
import requests
from pathlib import Path

# Function to download a file from a URL
def download_file(url, target_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check if the request was successful
    with open(target_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# Main script
def download_llama_model(presigned_url, target_folder):
    model_size = "7b"
    model_path = f"CodeLlama-{model_size}"
    shard = 0

    # Create target folder if it doesn't exist
    Path(target_folder).mkdir(parents=True, exist_ok=True)

    # Download LICENSE and Acceptable Usage Policy
    download_file(presigned_url.replace('*', "LICENSE"), os.path.join(target_folder, "LICENSE"))
    download_file(presigned_url.replace('*', "USE_POLICY.md"), os.path.join(target_folder, "USE_POLICY.md"))

    # Create model directory
    model_dir = os.path.join(target_folder, model_path)
    Path(model_dir).mkdir(exist_ok=True)

    # Download model files
    for i in range(shard + 1):
        file_name = f"consolidated.{i:02d}.pth"
        download_file(presigned_url.replace('*', f"{model_path}/{file_name}"), os.path.join(model_dir, file_name))

    # Download additional model files
    additional_files = ["params.json", "tokenizer.model", "checklist.chk"]
    for file in additional_files:
        download_file(presigned_url.replace('*', f"{model_path}/{file}"), os.path.join(model_dir, file))

# Example usage
if __name__ == "__main__":
    presigned_url = "<PRESIGNED_URL>"  # Replace <PRESIGNED_URL> with your actual presigned URL
    target_folder = "C:\\path\\to\\download\\folder"  # Update this path to where you want to download the files
    download_llama_model(presigned_url, target_folder)
