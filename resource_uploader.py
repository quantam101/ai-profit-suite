import os
import shutil
import uuid
from urllib.parse import urlparse


def upload_resource(resource_path_or_url: str, shared_dir: str = "shared_resources") -> str:
    """Save a local file or URL into the shared directory.

    If `resource_path_or_url` is a path to a local file, the file is copied
    to `shared_dir` using a unique name while preserving the original
    extension.

    If it's a URL, the URL is stored in a text file with a `.url` extension.

    Returns the path to the stored resource.
    """

    os.makedirs(shared_dir, exist_ok=True)

    parsed = urlparse(resource_path_or_url)
    if parsed.scheme in {"http", "https"}:
        # Treat as URL. Save the link in a file.
        filename = f"{uuid.uuid4().hex}.url"
        dest_path = os.path.join(shared_dir, filename)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(resource_path_or_url)
        return dest_path

    if os.path.isfile(resource_path_or_url):
        # Copy file to shared directory with unique name
        _, ext = os.path.splitext(resource_path_or_url)
        filename = f"{uuid.uuid4().hex}{ext}"
        dest_path = os.path.join(shared_dir, filename)
        shutil.copy(resource_path_or_url, dest_path)
        return dest_path

    raise FileNotFoundError(f"No such file or unsupported URL: {resource_path_or_url}")
