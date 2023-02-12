import subprocess

def parse_metadata_string(string: str) -> str:
    res = string.split()
    if len(res) > 2:
        return " ".join(res[2:])
    else:
        return None

def metadata(playerctl: str = "playerctl") -> dict:
    '''
    Get data about current playing track.
    Wrapper on: 
    playerctl metadata
    '''
    result_data = {}
    result_bash = subprocess.check_output([playerctl, "metadata"]).decode("utf-8").split("\n")
    result_data["length"] = int(parse_metadata_string(result_bash[0]))
    result_data["track_id"] = parse_metadata_string(result_bash[1]).replace("'", "")
    result_data["album"] = parse_metadata_string(result_bash[2])
    result_data["artist"] = parse_metadata_string(result_bash[3])
    result_data["title"] = parse_metadata_string(result_bash[4])
    return result_data

def play(playerctl: str = "playerctl") -> None:
    '''
    Continue playing track
    Wrapper on:
    playerctl stop
    '''
    subprocess.run([playerctl, "play"])

def pause(playerctl: str = "playerctl") -> None:
    '''
    Pause playing track
    Wrapper on:
    playerctl pause
    '''
    subprocess.run([playerctl, "pause"])

def toggle_play(playerctl: str = "playerctl") -> None:
    '''
    Toggle playing status
    play -> pause
    pause -> play
    Wrapper on:
    playerctl play-pause
    '''
    subprocess.run([playerctl, "play-pause"])

def stop(playerctl: str = "playerctl") -> None:
    '''
    Stop player
    Wrapper on:
    playerctl stop
    '''
    subprocess.run([playerctl], "stop")

def next(playerctl: str = "playerctl"):
    '''
    Start playing next track
    Wrapper on:
    playerctl next
    '''


if __name__ == "__main__":
    toggle_play()

