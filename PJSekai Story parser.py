import json
import os
from enum import Enum
from tkinter import filedialog as fd

class SnippetAction(int, Enum):
    NoAction = 0,
    Talk = 1
    CharacerLayout = 2
    InputName = 3
    CharacterMotion = 4
    Selectable = 5
    SpecialEffect = 6
    Sound = 7

class SpecialEffectType(int, Enum):
    NoEffect = 0
    BlackIn = 1
    BlackOut = 2
    WhiteIn = 3
    WhiteOut = 4
    ShakeScreen = 5
    ShakeWindow = 6
    ChangeBackground = 7
    Telop = 8
    FlashbackIn = 9
    FlashbackOut = 10
    ChangeCardStill = 11
    AmbientColorNormal = 12
    AmbientColorEvening = 13
    AmbientColorNight = 14
    PlayScenarioEffect = 15
    StopScenarioEffect = 16
    ChangeBackgroundStill = 17
    PlaceInfo = 18
    Movie = 19
    SekaiIn = 20
    SekaiOut = 21
    AttachCharacterShader = 22
    SimpleSelectable = 23
    FullScreenText = 24
    StopShakeScreen = 25
    StopShakeWindow = 26

Dict_JP_EN_Names = {
    "奏" : "Kanade",
    "まふゆ" : "Mafuyu",
    "絵名": "Ena",
    "瑞希": "Mizuki",
    "こはね": "Kohane",
    "彰人": "Akito",
    "杏": "An",
    "冬弥": "Toya",
    "ミク": "Miku",
    "ルカ": "Luka",
    "リン": "Rin",
    "レン": "Len",
    "MEIKO": "MEIKO",
    "KAITO": "KAITO",
    "雪平": "Yukihira",
    "二葉": "Futaba",
    "まふゆの母": "Mafuyu's Mother",
}

Dict_JP_EN_Location = {
    "宮益坂": "Miyamasuzaka",
    "まふゆの部屋" : "Mafuyu's Room",
    "絵画教室": "Painting Class"
}

bInJapanese = False

filelist = fd.askopenfilenames(title="Select File(s)")

def ScenarioParser(Scenario_FileName, Scenario_Output_FileName): 
    Scenario_JSON = json.load(open(Scenario_FileName, encoding='utf-8'))
    Scenario_Output_TextFile = open(Scenario_Output_FileName, "w")  
    Snippets = Scenario_JSON["Snippets"]
    ScenarioTalkData = Scenario_JSON["TalkData"]
    ScenarioSpecialEffectData = Scenario_JSON["SpecialEffectData"]

    for Snippet in Snippets:
        if Snippet["Action"] == SnippetAction.Talk:
            TalkData = ScenarioTalkData[Snippet["ReferenceIndex"]]
            DisplayName = Dict_JP_EN_Names[TalkData["WindowDisplayName"]] if bInJapanese and TalkData["WindowDisplayName"] in Dict_JP_EN_Names else TalkData["WindowDisplayName"]
            Body = TalkData["Body"].replace('\n',' ')
            Scenario_Output_TextFile.write("{name}: {text}\n".format(name = DisplayName, text = Body))
        elif Snippet["Action"] == SnippetAction.SpecialEffect:
            SpecialEffectData = ScenarioSpecialEffectData[Snippet["ReferenceIndex"]]
            if SpecialEffectData["EffectType"] == SpecialEffectType.Telop:
                Location = Dict_JP_EN_Location[SpecialEffectData["StringVal"]] if bInJapanese and SpecialEffectData["StringVal"] in Dict_JP_EN_Location else SpecialEffectData["StringVal"]
                Scenario_Output_TextFile.write(Location + "\n")

def VirtualLiveParser(VirtualLive_FileName, VirtualLive_Output_FileName): 
    VirtualLive_JSON = json.load(open(VirtualLive_FileName, encoding='utf-8'))
    Virtual_Output_TextFile = open(VirtualLive_Output_FileName, "w")  
    TalkEvents = VirtualLive_JSON["characterTalkEvents"]

    for TalkEvent in TalkEvents:
        TalkData = TalkEvent["Serif"].replace('\n',' ')
        Virtual_Output_TextFile.write(TalkData + '\n')

for file in filelist:
    Scenario_FileName = file
    Scenario_Output_FileName = os.path.splitext(file)[0] + ".txt"
    ScenarioParser(Scenario_FileName, Scenario_Output_FileName)

#VirtualLiveParser(Filename, output)