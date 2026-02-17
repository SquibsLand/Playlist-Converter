
from init import init
from pathlib import Path
from songs import parsePlaylist, convertSongs

args = init()
inputDir = Path(args.input)

if(inputDir.is_dir()):
    for child in inputDir.iterdir():

        print(child.suffix)
        if(child.suffix == ".m3u"): 
            songs = child.read_text().split('\n')
            filtered = [x for x in songs if x.strip()]
            songs = parsePlaylist(args.output, args.input, filtered)
            convertSongs(args, songs, child.name)
        else: 
            print("Only m3u playlists are supported")
            

