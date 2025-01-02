
# Holy Bible Audio Player in Greek - Vamvas Translation

This repository contains programs designed to process YouTube video sources of the Vamvas translation from the YouTube channel [@ekxeradio](https://www.youtube.com/@ekxeradio). The Python programs convert the videos into MP3 files and split them into individual Bible chapters. The HTML program serves as a web-based MP3 player for these chapters. The audio version of the Holy Bible (Greek Vamvas Edition) is available on the web page [Vamvas audio](https://ebible.gr/mp3player.html).

**The repository also contains the converted MP3 files, which are located in the `mp3` folder**.

- The first three characters of each file name indicate the book name.
- The number following the book name represents the chapter number.

---

## Program 1: YouTube to MP3 Converter `downloader.py`

This program downloads and converts YouTube videos to MP3 files using the `link.txt` input file containing the video IDs and desired MP3 filenames. The `link.txt` file includes all chapters of the Holy Bible Vamvas Greek Edition, sourced from the YouTube channel [@ekxeradio](https://www.youtube.com/@ekxeradio).

### How It Works:
1. **Input File Format**: A tab-separated file (`links.txt`) with two columns:
   - `link`: YouTube video ID.
   - `file`: Desired MP3 filename.

2. **Conversion Steps**:
   - Uses the `yt-dlp` library to download videos as audio.
   - Converts the audio to MP3 format with high quality (192 kbps).

3. **Key Features**:
   - Outputs MP3 files to a specified directory.
   - Uses a cookie file to bypass YouTube restrictions.

### Requirements:
- `yt-dlp`
- FFmpeg installed for handling MP3 files.

---

## Program 2: MP3 Splitter `psalms-splitter.py`

This program splits MP3 files into Bible chapters based on an `input.txt` file, which specifies the start and end points for each segment. It is used to convert the 29 Psalm MP3 files into 150 MP3 files, each corresponding to a specific chapter.

### How It Works:
1. **Input File Format**: A comma-separated file (`input.txt`) with three columns:
   - Input filename: Name of the MP3 file to split.
   - End time: Time to stop the segment (`mm:ss.ss` or `999999` for the end of the file).
   - Output filename: Name of the resulting MP3 file.

2. **Splitting Process**:
   - Reads the MP3 file using `pydub`.
   - Extracts segments based on start and end times.
   - Saves the extracted segments to the specified output directory.

3. **Dynamic Start Time**:
   - Automatically calculates the start time based on the previous segment’s end.

### Requirements:
- `pydub`
- FFmpeg installed for handling MP3 files.

---

## Program 3: Web-Based MP3 Player `mp3player.html`

This program provides a responsive web interface for playing Bible chapters in MP3 format, with options for searching, filtering, and playlist management.

### Features:
1. **MP3 Listing**:
   - Displays MP3 chapters categorized by book and searchable by chapter title.

2. **Player Controls**:
   - Play, stop, random play, and playlist playback.
   - Displays the current playing track.

3. **Playlist Management**:
   - Add/remove tracks to/from a playlist.
   - Save playlist in `localStorage` for persistence.

4. **Search and Filter**:
   - Filter by book or search by chapter name.

5. **Responsive Design**:
   - Works seamlessly across desktop, tablet, and mobile devices.

### How to Use:
1. Place the MP3 files in the designated folder (`mp3`).
2. Ensure `mp3/books.csv` contains metadata for Holy Bible books (book id,book name).
3. Ensure `mp3/mp3chapters.csv` contains metadata for MP3 files (number, title, book id, filename).
4. Open the `index.html` file in a browser to access the player.

---

