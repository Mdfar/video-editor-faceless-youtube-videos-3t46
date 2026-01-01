import os from movie_engine.generator import VideoGenerator from movie_engine.assets import AssetManager

def main(): script_text = """ In a world where technology moves faster than ever, automation is the key to staying ahead. Let's explore how. """

# Initialize managers
asset_manager = AssetManager(api_key=os.getenv("PEXELS_API_KEY"))
generator = VideoGenerator()

print("🚀 Starting Automated Video Production...")

# 1. Generate Voiceover (Placeholder for ElevenLabs API)
audio_path = "assets/audio/narration.mp3"

# 2. Fetch Assets based on script keywords
keywords = ["technology", "innovation", "future"]
video_clips = asset_manager.fetch_stock_videos(keywords)

# 3. Assemble Video
output_file = "outputs/final_youtube_video.mp4"
generator.assemble(video_clips, audio_path, output_file)

print(f"✅ Video rendered successfully: {output_file}")


if name == "main": main()