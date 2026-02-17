from pathlib import Path, PureWindowsPath, PosixPath
import ffmpeg
from typing import Optional
from pathlib import Path
from init import MyNamespace
from mutagen import File as mFile
from playlist import convertPlaylist

class PlaylistItem:
    def __init__(self, outputRoot: str, inputRoot: str, path: str):
        self.inputRoot = Path(inputRoot)
        self.outputRoot = Path(outputRoot)
        self.path = automaticPath(path)
        self.style = pathStyle(path)

        self.pathObj = self.inputRoot / self.path
        self.valid = self.getInputPath().exists()

    def getOutputPath(self, suffix: Optional[str] = None) -> Path:
            
            if suffix:
                output_path = self.outputRoot / self.getSuffixPath(suffix)
            else: 
                output_path = self.outputRoot / self.path
            return output_path
    def getSuffixPath(self, suffix:str):
        if not suffix.startswith("."):
            suffix = "." + suffix
        return self.path.with_suffix(suffix)
    def getInputPath(self) -> Path:
        return self.inputRoot / self.path

    
def automaticPath(path:str):
    style = pathStyle(path)
    if style == "windows":
        return PureWindowsPath(path)
    elif style == "posix": 
        return PosixPath(path)
    else:
        print("Unknown file path type")
        return Path(path)

def pathStyle(path: str):
    if "\\" in path:
        return "windows"
    if "/" in path:
        return "posix"
    return "unknown" 
   
def parsePlaylist(outputRoot:str, inputRoot:str, songs: list[str]):
    def toItem(path:str):
        return PlaylistItem(outputRoot, inputRoot, path)
    items =list(map(toItem, songs))
    
    def isValid(item:PlaylistItem):
        return item.valid
    filteredItems = list(filter(isValid, items))
    
    invalid = len(filteredItems) - len(items)

    if len(filteredItems) == 0:
        print("All songs are invalid, please check your paths")
    elif invalid == 0:
        print("All songs are valid")
    elif(invalid > 0):
        print(f"There are {invalid} song(s)")

    return filteredItems

def convertSongs(args: type[MyNamespace], songs:list[PlaylistItem], playlistName: str):
    fails = 0
    withReplayGain = 0
    newSongs =  []
    for song in songs:
        input = str(song.getInputPath())
        outputSong = song.getOutputPath(args.output_type)
        newSongs.append(song.getSuffixPath(args.output_type))
        output = str(outputSong)
        print(input, output)
        try: 
            af = None
            if(args.replay_gain):
                gain = parseReplayGain(input)
                if gain == None:
                    gain = 0.0
                else: 
                    withReplayGain+=1
                af = f"volume={gain}dB"
            outputSong.parent.mkdir(parents=True, exist_ok=True)
            ffmpeg.input(input).output(filename=output, af=af).run(overwrite_output=args.overwrite)
        except Exception as e:
            print(e)
            fails+=1
    if fails == 0:
        print(f"Converted all ({len(songs)}) songs")
    elif fails == len(songs):
        print(f"All ({fails}) songs failed to convert")
    else:
        print(f"{len(songs) - fails}/{len(songs)} where converted")   
    print("Generating new playlist...")
    convertPlaylist(args,playlistName, newSongs ) 

def parseReplayGain(inputPath:str):
    print("Look here")
    audio = mFile(inputPath)
    print
    if audio.mime[0] == "audio/mp3":
        name = "replaygain_track_gain"
        for frame in audio.tags.getall("TXXX"):
            if frame.desc.lower() == name.lower():
                return float(frame.text[0].replace(" dB", ""))
        return None
    tag_name = "replaygain_track_gain"
    val = audio.get(tag_name)
    if val:
        return float(val[0].replace(" dB", ""))
    return None
       

        