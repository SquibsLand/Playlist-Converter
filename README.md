# Playlist Converter

This project is a python script that converts all the songs in one or more playlists to a desired format, while maintaining the the folder structure, and playlists. This allows you to convert only the songs that you listen to, and not your whole library.

## Arguments

| Name                      | Command                | Required | Values               | Default   |
| ------------------------- | ---------------------- | -------- | -------------------- | --------- |
| Input                     | input                  | X        | directory            | `/input`  |
| Output                    | output                 | X        | directory            | `/output` |
| Overwrite                 | overwrite              | X        | boolean              | `false`   |
| Replay Gain               | replay_gain            | X        | boolean              | `false`   |
| Output Audio Type         | output_type            | X        | mp3, wav, etc        | `wav`     |
| Output Playlist Structure | out_playlist_structure | X        | windows, posix, auto | `auto`    |

### Input

Input folder of the music and m3u files. The m3u must be in the root of the folder, but songs can be deeper

### Output

Output folder for the converted music, only including the m3u playlists and converted songs.

### Overwrite

Choice to overwrite existing files in the output, if a file with the same name already exists. Warning: Enabling overwriting could result in longer conversion time as if a song is in two playlists, it will replace it twice

### Replay Gain

Apply the gain from the tags to the songs. Only tested with the MP3 (TXXX) `replaygain_track_gain` tag, other format may or may not work.

### Output Audio Type

This is the converted audio format that all tracks will be. Currently you can not set it to retain the existing format.

### Output PLaylist Structure

This determines if the playlist entries will be formatted as posix, windows, or automatic based on what it was previously. This feature is still under testing.
