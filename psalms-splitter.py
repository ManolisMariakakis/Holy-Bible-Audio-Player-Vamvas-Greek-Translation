import os
from pydub import AudioSegment

def time_to_seconds(time_str):
    """
    Converts a time string in the format mm:ss.ss to total seconds.

    Args:
        time_str (str): Time string in the format mm:ss.ss.

    Returns:
        float: Time in seconds.
    """
    try:
        minutes, seconds = time_str.split(":")
        return int(minutes) * 60 + float(seconds)
    except ValueError:
        raise ValueError(f"Invalid time format: {time_str}")

def cut_mp3(input_file, start_time, end_time, output_file):
    """
    Cuts an MP3 file from start_time to end_time and saves the output.

    Args:
        input_file (str): Path to the input MP3 file.
        start_time (float): Start position in seconds.
        end_time (float): Stop position in seconds.
        output_file (str): Path to save the cut MP3 file.
    """
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(input_file)

        # Convert start and end time to milliseconds
        start_time_ms = int(start_time * 1000)
        end_time_ms = int(end_time * 1000) if end_time != 999999 else len(audio)

        # Check if times are valid
        if start_time_ms < 0 or end_time_ms > len(audio):
            raise ValueError("Start or end time is out of bounds.")

        if start_time_ms >= end_time_ms:
            start_time_ms = 0.0 #next mp3 file

        # Extract the segment
        cut_audio = audio[start_time_ms:end_time_ms]

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Export the cut segment
        cut_audio.export(output_file, format="mp3")
        print(f"Segment saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

def process_input_file(input_file_path, input_folder, output_folder):
    """
    Processes a text file containing MP3 cutting parameters.

    Args:
        input_file_path (str): Path to the input text file.
        input_folder (str): Folder containing input MP3 files.
        output_folder (str): Folder to save output MP3 files.
    """
    try:
        with open(input_file_path, "r") as file:
            lines = file.readlines()

        previous_end = 0.0  # Initialize previous end position

        for line in lines:
            # Parse the line
            params = line.strip().split(",")
            if len(params) != 3:
                print(f"Invalid line format: {line.strip()}")
                continue


            input_filename, stop_time_str, output_filename = params
            
            # Check if stop_time_str is 999999
            if stop_time_str == "999999":
                stop_time = 999999  # Use a special value for further handling
            else:
                stop_time = time_to_seconds(stop_time_str)  # Convert to seconds if not 999999

            # Calculate start position dynamically
            start_pos = round(previous_end, 2) if previous_end != 0.0 else 0.0

            # Construct full paths
            input_path = os.path.join(input_folder, input_filename.strip())
            output_path = os.path.join(output_folder, output_filename.strip())

            # If end position is 999999, get the total duration of the MP3
            audio = AudioSegment.from_mp3(input_path)
            if stop_time == 999999:
                stop_time = len(audio) / 1000.0

            # Perform the cut
            cut_mp3(input_path, start_pos, stop_time, output_path)

            # Update previous end position
            previous_end = stop_time

    except Exception as e:
        print(f"Error processing input file: {e}")

if __name__ == "__main__":
    # Input and output folders
    input_folder = r"C:\\psa"
    output_folder = r"C:\\psa\\output"

    # Input text file path
    input_file_path = os.path.join(input_folder, "input.txt")

    # Process the input file
    process_input_file(input_file_path, input_folder, output_folder)
