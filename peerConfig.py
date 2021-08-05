import argparse,json
from runningConfig import *

def fileGenerate(location,content):
    with open(location,"w") as f:
        f.write(content)

def getTemplate(configLoc):
    with open(configLoc,"r") as f:
        content = f.read()
    return content

def logWrite(content):
    with open("./log","w+") as f:
        f.write(content)


def wgConfig(outputDir :str, templateFile :str, peer :Peer):
    configContent = getTemplate(template["wgconfig"])
    rules = peer.wgReplaceRule()
    for key in rules.keys():
        configContent.replace(key,rules[key])
    fileGenerate(outputDir+peer.peername+".conf",configContent)
    pass

def birdConfig(outputDir :str, templateFile :str, peer :Peer):
    configContent = getTemplate(template["birdconfig"])
    rules = peer.birdReplaceRule()
    for key in rules.keys():
        configContent.replace(key,rules[key])
    fileGenerate(outputDir+peer.peername+".conf",configContent)
    pass


def main():
    parser = argparse.ArgumentParser
    parser.add_argument("mode",help="change jsonfile read mode and ")

    arg = parser.parse_args()
    print(arg)

if __name__ == "__main__":
    main()