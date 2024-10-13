from datetime import datetime
import subprocess
import time
import threading

max_retries = 5  # 5 try max
process = None

def download_stream(stream_url, output_path):
    global process
    retries = 0
    while retries < max_retries:
        try:
            command_download = ['streamlink', stream_url, 'best', '-o', output_path]
            process = subprocess.Popen(command_download, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            while True:
                output = process.stdout.readline()
                if output == b'' and process.poll() is not None: # If stream stops
                    break
                if output:
                    print(output.decode().strip())

            process.wait()
            exit_code = process.poll()

            if exit_code == 0:
                print("Download successful")
                break
            else:
                raise Exception(f"Streamlink failed {exit_code}")

        except Exception as e:
            retries += 1
            print(f"Error : {str(e)}. Reconnection ({retries}/{max_retries})...")
            if retries < max_retries:
                print("Waiting before retrying connection")
                time.sleep(30)
            else:
                print("Maximum number of attempts reached. Download stopped")
                break


def check_and_download_stream(stream_url, output_path):
    try:
        # Check Stream on live
        command_check = ['streamlink', '--json', stream_url]
        result = subprocess.run(command_check, capture_output=True, text=True)

        print("Start Downloading")
        download_thread = threading.Thread(target=download_stream, args=(stream_url, output_path))
        download_thread.start()

        download_thread.join()  # Wait end of download
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {str(e)}")


if __name__ == "__main__":
    time_of_day = datetime.now().strftime('%Y-%m-%d')
    stream_url = ""
    output_path = "stream_" + time_of_day + ".mp4"
    check_and_download_stream(stream_url, output_path)
