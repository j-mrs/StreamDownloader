# StreamDownloader

**StreamDownloader** is a Python application for downloading live streams using `streamlink`. It includes a GitHub Actions workflow to facilitate manual downloads. 

## Features

- Downloads a live stream from a provided URL.
- Saves the video with a unique filename based on the date (format: `stream_YYYY-MM-DD.mp4`).
- Manual execution of the download process through a GitHub Actions workflow.
- Stores the downloaded video as an artifact in GitHub Actions for manual retrieval.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [streamlink](https://streamlink.github.io/) for downloading streams.
- A GitHub account with access to GitHub Actions.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/j-mrs/StreamDownloader.git
    cd StreamDownloader
    ```

2. Install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

   Ensure `requirements.txt` includes `streamlink` as a dependency.

3. Set up GitHub authentication if using GitHub Actions.

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
    ```

## Manual Usage

### Running the Workflow

You can run the download process manually using GitHub Actions. To start the job:

1. Navigate to the **Actions** tab in your GitHub repository.
2. Select the **StreamDownloader** workflow.
3. Click on the **Run workflow** button.

### Manually Running the Script

You can also run `StreamDownloader.py` locally to download a stream by editing the stream URL in the file.

```bash
python StreamDownloader.py
