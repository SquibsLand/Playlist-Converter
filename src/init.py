from pathlib import Path
import argparse
from typing import Literal

class MyNamespace(argparse.Namespace):

    input: str
    output: str
    overwrite:bool
    replay_gain: bool
    output_type:str
    out_playlist_structure: Literal["auto", "windows", "posix"]


def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str, default="/input")
    parser.add_argument("--output", type=str, default="/output")
    parser.add_argument("--overwrite", type=bool, default=False)
    parser.add_argument("--replay_gain", type=bool, default=False)
    parser.add_argument("--output_type", type=str, default="wav")
    parser.add_argument("--out_playlist_structure", type=str, default="auto")
    return parser.parse_args(namespace=MyNamespace)



def init():
    args = getArgs()
    paths = [args.input, args.output]
    for path in paths:
        obj = Path(path)
        try:
            obj.mkdir()
            print(f"Directory '{obj}' created successfully.")
        except FileExistsError:
            print(f"Directory '{obj}' already exists.")
                

    return args