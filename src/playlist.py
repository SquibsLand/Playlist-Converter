from pathlib import Path, WindowsPath, PosixPath

from init import MyNamespace

def convertPlaylist(args: type[MyNamespace], playlistName:str, songs:list[Path]):
    print("Look Here")
    def changeSuffix(song: Path):
        suffix = args.output_type
        if not suffix.startswith("."):
                    suffix = "." + suffix
        newPath = song.with_suffix(suffix)
        print(args.out_playlist_structure)
        if args.out_playlist_structure == "windows":
            return str(newPath)  # native Windows format (\ on Windows)
        elif args.out_playlist_structure == "posix":
            return newPath.as_posix()  # forward slashes
        elif args.out_playlist_structure == "other":
              return str(newPath)
    newSongs = list(map(changeSuffix, songs))
    outputPlaylist = Path(args.output) / Path(playlistName)
    outputPlaylist.write_text("\n".join(newSongs))
    
    
    