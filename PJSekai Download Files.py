import requests
from pathlib import Path

from tkinter import filedialog as fd

filelist = [
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_01.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_02.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_03.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_04.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_05.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_06.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_07.json",
    "https://assets.pjsek.ai/file/pjsekai-assets/ondemand/event_story/event_persona_2023/scenario/event_100_08.json",
]

directory = fd.askdirectory(title="Select Directory")

def Download_File(File_Url, Directory_Path):
    filename = ""
    response = requests.get(File_Url, allow_redirects=True)
    if File_Url.find('/'):
        filename = File_Url.rsplit('/', 1)[1]
    file_path = Path(Directory_Path, filename)
    open(file_path, 'wb').write(response.content)

for file in filelist:
    Download_File(file, directory)