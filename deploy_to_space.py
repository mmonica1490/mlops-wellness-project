
import os
from huggingface_hub import HfApi, create_repo

HF_USERNAME = "MonicaLenin"
SPACE_NAME = "wellness-tourism-space"  # you can rename if you want

SPACE_REPO_ID = f"{HF_USERNAME}/{SPACE_NAME}"

api = HfApi()

# 1. Create Space repo with Docker SDK
create_repo(
    repo_id=SPACE_REPO_ID,
    repo_type="space",
    private=False,
    exist_ok=True,
    space_sdk="docker"
)

print(f"✅ Space repo ready: https://huggingface.co/spaces/{SPACE_REPO_ID}")

# 2. Local file paths
base_dir = "tourism_project/deployment"
dockerfile_path = os.path.join(base_dir, "Dockerfile")
requirements_path = os.path.join(base_dir, "requirements.txt")
app_path = os.path.join(base_dir, "app.py")

# 3. Upload Dockerfile
api.upload_file(
    path_or_fileobj=dockerfile_path,
    path_in_repo="Dockerfile",
    repo_id=SPACE_REPO_ID,
    repo_type="space"
)

# 4. Upload requirements.txt
api.upload_file(
    path_or_fileobj=requirements_path,
    path_in_repo="requirements.txt",
    repo_id=SPACE_REPO_ID,
    repo_type="space"
)

# 5. Upload app.py
api.upload_file(
    path_or_fileobj=app_path,
    path_in_repo="app.py",
    repo_id=SPACE_REPO_ID,
    repo_type="space"
)

print("✅ Deployment files uploaded to Hugging Face Space.")
print(f"🚀 Your app will be available at: https://huggingface.co/spaces/{SPACE_REPO_ID}")
