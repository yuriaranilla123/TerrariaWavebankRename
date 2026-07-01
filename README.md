# TerrariaWavebankRename

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Terraria](https://img.shields.io/badge/Terraria-1.4.5-394EA1)
![License](https://img.shields.io/badge/License-MIT-green)

Rename audio files extracted from Terraria's Wave Bank.xwb using their official in-game track names.

## Installation

Clone this repository or download it as a ZIP.

Place the scripts in the same folder as your extracted Terraria music files.

If using `TerrariaWavebankRenameGameDev.py`, install FFmpeg and ensure it is available in your system PATH.

## Acknowledgements

Official track names are © Re-Logic.

This project only uses the publicly documented names for file renaming purposes.

The official Terraria track names used by this project are based on
the MusicDisplay mod by GabeHasWon.

Track names are based on:

MusicDisplay/Localization/en-US_Mods.MusicDisplay.TrackNames.hjson

MusicDisplay:
https://github.com/GabeHasWon/MusicDisplay

Thank you to GabeHasWon for documenting the official Terraria music names.

## Features

- Renames extracted WAV files
- Renames extracted MP3 files
- Supports Terraria 1.4.5 and later (104 official music tracks, including Terraria: Otherworld and post-1.4.5 additions).
- Includes the Terraria: Otherworld soundtrack
- Includes Terraria 1.4.5 boss-exclusive music

## Included Scripts

### TerrariaWavebankRename.py

Renames extracted `.wav` and `.mp3` files while preserving their original format.

Recommended if you simply want the official Terraria music names without converting the audio.

### TerrariaWavebankRenameGameDev.py

Converts extracted audio to `.ogg` (Vorbis) using FFmpeg and applies the official Terraria track names.

Recommended for game development, mods, or engines that use OGG audio.

## Requirements

Requires Python 3.10+

### TerrariaWavebankRename.py

No additional dependencies.

### TerrariaWavebankRenameGameDev.py

Requires FFmpeg to be installed and available in your system PATH.

FFmpeg:
https://ffmpeg.org/

Before using either script, extract the contents of:

```text
SteamLibrary\steamapps\common\Terraria\Content\Wave Bank.xwb
```

into individual audio files (`.wav` or `.mp3`).

## Supported extraction tools

Examples include:

- foobar2000 + vgmstream
- vgmstream CLI
- Winamp + vgmstream
- XMPlay + vgmstream

## Tested extraction tools

- foobar2000 + vgmstream

## Supported input

- .wav
- .mp3

Output

TerrariaWavebankRename.py
- .wav
- .mp3

TerrariaWavebankRenameGameDev.py
- .ogg

## Example output

```
92.wav
↓
92 - The Destroyer.wav
```

Before

```
01.mp3
02.mp3
03.mp3
```

After

```
01 - Overworld Night.mp3
02 - Eerie.mp3
03 - Overworld Day.mp3
```
## License

This project is licensed under the GPL v3 License.

See the LICENSE file for details.