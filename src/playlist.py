from pathlib import Path

from init import MyNamespace

def convertPlaylist(args: type[MyNamespace], playlistName:str, songs:list[Path]):
    print("Look Here")
    def changeSuffix(song: Path):
        suffix = args.output_type
        if not suffix.startswith("."):
                    suffix = "." + suffix
        return str(song.with_suffix(suffix))
    newSongs = list(map(changeSuffix, songs))
    outputPlaylist = Path(args.output) / Path(playlistName)
    outputPlaylist.write_text("\n".join(newSongs))
    
    
    