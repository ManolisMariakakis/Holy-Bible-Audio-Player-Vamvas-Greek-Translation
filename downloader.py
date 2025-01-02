import yt_dlp
import csv

def download_youtube_as_mp3(video_id, output_filename):
    try:
        # Define the output folder
        output_folder = r"C:\vamvas"

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_folder}\\{output_filename}',  
            'cookiefile': f'c:\\vamvas\\cookies.txt',
            'ffmpeg_location': r'C:\ffmpeg',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Use yt-dlp to download and convert
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

        print(f"MP3 saved as {output_folder}\\{output_filename}.mp3")

    except Exception as e:
        print(f"An error occurred: {e}")

def process_links_file(file_path):
    try:
        # Open the tab-separated file
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                video_id = row['link']
                output_filename = row['file']
                download_youtube_as_mp3(video_id, output_filename)
    except Exception as e:
        print(f"Failed to process the file: {e}")

# Example usage
process_links_file(r"C:\vamvas\links.txt")
