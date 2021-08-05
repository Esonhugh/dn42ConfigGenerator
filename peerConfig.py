import argparse,json
import os

from config import *

def fileGenerate(location,content):
    with open(location,"w") as f:
        f.write(content)

def getTemplate(configLoc):
    with open(configLoc,"r") as f:
        content = f.read()
    return content

def logWrite(content):
    with open("./log","w+") as f:
        f.write(str(content))


def wgConfig(outputDir :str, peer :Peer):
    configContent = getTemplate(template["wgconfig"])
    rules = peer.wgReplaceRule()
    for key in rules.keys():
        configContent = configContent.replace(key,rules[key])
    fileGenerate(loc := outputDir+peer.peername+"_wg.conf",configContent)
    print("[+] wireguard config generate successfully")
    print("[+] flie at ",loc)
    pass

def birdConfig(outputDir :str,  peer :Peer):
    configContent = getTemplate(template["birdconfig"])
    rules = peer.birdReplaceRule()
    for key in rules.keys():
        configContent = configContent.replace(key,rules[key])
    fileGenerate(loc := outputDir+peer.peername+"_bird.conf",configContent)
    print("[+] bird config generate successfully")
    print("[+] flie at ",loc)
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode",help="change jsonfile read mode and ",choices=["file","hand"])
    parser.add_argument("-d","--dir",help="config output dir,at default it will add a new folder at this repos output dir")

    parser.add_argument("-f","--file",help="[file mode] json format config file")
    parser.add_argument("-n","--name",help="[hand mode 1] peer name")
    parser.add_argument("--asn",help="[hand mode 1] peer asn")
    parser.add_argument("--pub-ip",help="[hand mode 1] peer public ip allow the domain")
    parser.add_argument("--pub-key",help="[hand mode 1] peer wg public key")
    parser.add_argument("--dn42-ipv4",help="[hand mode 1] peer dn42 ipv4")
    parser.add_argument("--dn42-ipv6",help="[hand mode 1] peer dn42 ipv6")
    parser.add_argument("-s","--json-str",help="[hand mode 2] json strings contains all info above.")
    parser.add_argument("-v","--output-json",help="print the config json only",action="store_true")
    arg = parser.parse_args()

    print( arg )

    if arg.mode == "file":
        if arg.file != None:
            peerinfo :dict = json.load(open(arg.file))
        else:
            print("No found file option")
            exit(1)

    else :
        if arg.json_str != None :
            peerinfo :dict = json.loads(arg.json_str)

        else :
            peerinfo = {
                'name': arg.name,
                'asn': arg.asn,
                'dn42_ipv4': arg.dn42_ipv4,
                'dn42_ipv6': arg.dn42_ipv6,
                'wg_public_key': arg.pub_key,
                'public_ip': arg.pub_ip
            }

    logWrite(peerinfo)
    if arg.output_json :
        print("[+] json output: ",json.dumps(peerinfo))
        return 0

    print("[*] Generate Peering Object ...")
    peer = Peer(asn=peerinfo["asn"],peer=peerinfo["name"],
                pubIP=peerinfo["public_ip"],
                pubkey=peerinfo["wg_public_key"],
                dn42IPv4=peerinfo["dn42_ipv4"],
                dn42IPv6=peerinfo["dn42_ipv6"]
                )
    print("[+] Generate Success ...")

    if not os.path.exists(template["wg_output"]) :
        os.mkdir(template["wg_output"])
    if not os.path.exists(template["bird_output"]):
        os.mkdir(template["bird_output"])

    wgConfig(template["wg_output"],peer)
    birdConfig(template["bird_output"],peer)



if __name__ == "__main__":
    main()