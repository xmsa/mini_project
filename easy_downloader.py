import argparse
import subprocess
import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

parser = argparse.ArgumentParser(
    description='Easy Downloader...')
parser.add_argument('input_file', type=str, help='Path to the input file')

args = parser.parse_args()
input_file = Path(args.input_file)

if not input_file.exists():
    raise FileExistsError(f"The input file {input_file} does not exist.")

print(f'Input file is: {input_file}')
base_name = input_file.stem  # filename without extension
suffix = input_file.suffix   # file extension, e.g. .txt

exist_path = input_file.parent / f"exist_{base_name}{suffix}"
failed_path = input_file.parent / f"failed_{base_name}{suffix}"

with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

folder_name = Path(lines[0])
folder_name.mkdir(exist_ok=True)

failed_entries = [] if not failed_path.exists() else [folder_name]
exist_entries = [] if not exist_path.exists() else [folder_name]
try:

    for i in range(1, len(lines), 2):
        filename = lines[i]
        url = lines[i + 1]
        filepath = folder_name / f"{filename}.mp4"

        if filepath.exists():
            print(f"The file '{filename}.mp4' already exists.")
            exist_entries.append(filename)
            exist_entries.append(url)
            continue

        print(f"Downloading '{filename}' ...")
        result = subprocess.run([
            "aria2c",
            "-x", "16",
            "-s", "16",
            "-d", str(folder_name),
            "-o", f"{filename}.mp4",
            url
        ])

        if result.returncode != 0 or not filepath.exists():
            print(
                f"Download of '{filename}' failed. Added to the failed list.")
            failed_entries.append(filename)
            failed_entries.append(url)
except KeyboardInterrupt:
    print("\nDownload interrupted by user (Ctrl+C). Saving failed downloads...")
    for text in lines[i:]:
        failed_entries.append(text)


if len(failed_entries) > 1:
    with open(failed_path, "a", encoding="utf-8") as f:
        for line in failed_entries:
            f.write(f"{line}\n")
    print(f"Failed downloads saved to: {failed_path}")

if len(exist_entries) > 1:
    with open(exist_path, "a", encoding="utf-8") as f:
        for line in exist_entries:
            f.write(f"{line}\n")
    print(f"Existing files saved to: {exist_path}")
