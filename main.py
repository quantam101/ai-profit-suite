import argparse
from resource_uploader import upload_resource


def main():
    parser = argparse.ArgumentParser(description="AI Profit Suite utility")
    subparsers = parser.add_subparsers(dest="command")

    upload_parser = subparsers.add_parser("upload", help="Upload a file or link")
    upload_parser.add_argument("path_or_url", help="Path to local file or URL")
    upload_parser.add_argument(
        "--dir",
        default="shared_resources",
        help="Directory to store uploaded resources",
    )

    args = parser.parse_args()

    if args.command == "upload":
        dest = upload_resource(args.path_or_url, args.dir)
        print(f"Resource saved to {dest}")
    else:
        print("AI Profit Suite Initialized.")


if __name__ == "__main__":
    main()
