import os
import gdown

def main():
    models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    # Models folder Google Drive URL (from README)
    url = "https://drive.google.com/drive/folders/1BsvU_4uSxTSvKv2ysKovJufq0Lyeqqq2?usp=sharing"
    
    print(f"Downloading models to {models_dir}...")
    try:
        # gdown's folder download feature
        gdown.download_folder(url, output=models_dir, quiet=False, use_cookies=False)
        print("Models downloaded successfully!")
    except Exception as e:
        print(f"Error downloading models: {e}")

if __name__ == "__main__":
    main()
