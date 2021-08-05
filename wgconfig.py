import argparse

path = "./"
privateKey = ""
template = {
    "privatekey":   "./secret/privatekey",
    "wgconfig":     "./config/wgconfig.conf",
    "birdconfig":   "./config/birdconfig.conf"
}

def fileGenerate(location,content):
    with open(location,"w") as f:
        f.write(content)

def getTemplate(configLoc):
    with open(configLoc,"r") as f:
        content = f.read()
    return content

def getPrivateKey(location):
    with open(location,"r") as f:
        key = f.read()
    return key

def wgConfig(outputDir :str, filename :str,):
    privateKey = getPrivateKey(template["privatekey"])



    fileGenerate("")

    pass

def main():
    parser = argparse.ArgumentParser
    parser.add_argument("")


if __name__ == "__main__":
    main()