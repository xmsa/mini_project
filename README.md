# Script

## text_file_translator

### install pakage

`pip install translators==5.7.0`

### run script

`python text_file_translator.py file_name [new_file_name]`

## goedel_number

Goedel number calculator

### run script

#### encoding <x,y>:z

`python goedel_number.py x y`

#### decoding z:<x,y>

`python goedel_number.py z `

## file downloader

download file with textfile and url

### run script

#### download file with url

`python download_file_with_textfile.py url`

#### decdownload file with txtfile

`python download_file_with_textfile.py file_name.txt`

#### decdownload file with txtfile and compress all file download in zip file

`python download_file_with_textfile.py -s file_name.txt`

## youtube video downloader

download youtube video with textfile and url

### run script

#### download file with url

`python youtube_downloader.py url`

#### decdownload file with txtfile

`python youtube_downloader.py file_name.txt`

## Network manager

Network manager

#### change DNS

`python network_manage.py --dns`

#### change Mode

`python network_manage.py --mode`

#### change Port

`python network_manage.py --port`

#### Run V2ray-ng

[Downlod v2ray core](https://github.com/v2fly/v2ray-core/) and extract to $HOME/.local/etc/

run with directory path config (Defult:"$HOME/Config_v2ray")

` python managenetwork.py --vpn [--config_dir dir_path ]`

run with config file path (Defult:$HOME/Config_v2ray/config.json)

` python manage\ network.py --vpn [--config file_path ]`

## Rename file on directory

remove multispace and befor or after . in file name

### run script

` python rename_file.py`

#### Run script with multi directory

` python rename_file.py dir1 [dir2 ,...]`

## Subtitle LTR to RTL

fixed RTL Problem on subtitle

### run script

#### with Directory

` python Subtitle_ltr_to_rtl.py <Directory>`

#### with SRT file

` python Subtitle_ltr_to_rtl.py <SRT file>`

## 🧾 Thesis File Merger for Similarity Checking

This script is designed to **preprocess and merge multiple LaTeX files** of an academic thesis into a single, clean text file — ideal for uploading to similarity detection platforms such as **Hamanandjoo** (همانندجو), which often require a flattened document for accurate analysis.

🔗 You can find this script inside the thesis template directory:
[**Thesis Isfahan template**](https://github.com/xmsa/TexTemplate/tree/main/Thesis%20Isfahan%20template)

---

### ✨ Features:

- Recursively expands LaTeX `\input{}` and `\include{}` directives.
- Ignores content after `\appendix` to limit analysis to main body chapters.
- Removes LaTeX comments (`% ...`) while preserving escaped symbols (e.g., `\%`).
- Outputs a clean `.txt` file ready for similarity/plagiarism check tools.

---

### ⚠️ Important Notes:

- 📂 **Backup First:** Make sure to **create a backup of your thesis files** before running the script. It doesn’t modify existing files, but it's always good practice to back up before preprocessing.
- 📄 **Appendices are excluded** from the output by design, as they are often not required for similarity checks.

---

### ▶️ Example Usage

```bash
cd "Thesis Isfahan template"
python thesis_builder.py Thesis.tex -o cleaned_output.txt
```

> Make sure Python is installed and your working directory includes the full thesis project.

## 🧾 Easy Downloader for Batch Video Files

This script is designed to **download multiple video files in batch** based on an input text file specifying a folder name followed by pairs of filenames and their corresponding URLs. It uses **aria2c** for fast, multi-connection downloads and handles already existing files as well as failed downloads by keeping separate logs.

---

### 🔗 Installation

Make sure to install **aria2** before running the script:

```bash
sudo apt install aria2
```

---

### ✨ Features

* Reads an input text file where:

  * The **first line** is the folder name to save files in.
  * Subsequent lines are **pairs**: filename (without extension) and URL.
* Creates the specified folder if it doesn’t exist.
* Skips files that already exist and logs them to a separate "exist" file.
* Attempts to download each file as an `.mp4`.
* If the download fails or is interrupted (Ctrl+C), logs failed entries to a "failed" file.
* Supports resuming incomplete downloads by logging failed URLs for re-download.

---

### ⚠️ Input File Format

Your input `.txt` file must follow this format:

```
folder_name
filename1
url1
filename2
url2
...
```

* The **first line** specifies the folder where all downloaded `.mp4` files will be saved.
* Each subsequent pair of lines specifies the filename and the download URL.

---

### ▶️ Example Usage

```bash
python easy_downloader.py download_list.txt
```

Where `download_list.txt` might look like:

```
MyVideos
video1
https://example.com/video1.mp4
video2
https://example.com/video2.mp4
```

---

### 📝 What happens during execution?

* If a file like `MyVideos/video1.mp4` exists, it skips downloading and logs this in `exist_download_list.txt`.
* If downloading `video2.mp4` fails, it logs it in `failed_download_list.txt`.
* Pressing **Ctrl+C** interrupts the process, and all unfinished downloads from the current point on are saved to the failed list for retry later.

---

### 💡 Notes

* The script automatically appends `"exist_"` or `"failed_"` prefixes to your input filename when creating log files for existing or failed downloads.
* The script requires Python 3.x.
* Make sure `aria2c` is installed and available in your system's PATH.


---

## MOC Player State Manager

This is a Bash script to manage **MOC (Music on Console)** playback, allowing you to save, load, and resume the last played track along with its playback position. It also provides convenient commands to control MOC from the terminal.

### Features

* Save the current track, playback position, and state (play/pause) when stopping MOC.
* Automatically load and resume the last saved track when starting MOC.
* Control MOC playback directly via script commands: next, previous, toggle play/pause.
* Works entirely from the command line.

### Usage

```bash
./moc_manager.sh {start|stop|next|previous|toggle|save|load}
```

#### Options

* **start**
  Starts the MOC server if it’s not running, loads the last saved track and position, and opens the MOC console.
  If MOC is already running, it just opens the MOC console.

* **stop**
  Stops the MOC server. If a track is playing or paused, the script saves the current track, playback position, and state before stopping.
  If no track is playing, the saved state file is removed.

* **next**
  Skips to the next track in the playlist.

* **previous**
  Returns to the previous track in the playlist.

* **toggle**
  Toggles between play and pause for the current track.

* **save**
  Manually saves the current track, playback position, and state to a file (`~/.mocp_state`).

* **load**
  Loads the last saved track and resumes playback from the saved position.

### State File

* The script stores the last track, position, and playback state in:

  ```
  ~/.mocp_state
  ```
* This file is automatically created when saving the state and removed if no valid track is found.

### Requirements

* [MOC (Music on Console)](https://moc.daper.net/)
* Bash shell
