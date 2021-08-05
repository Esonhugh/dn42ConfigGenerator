path = "./"

template = {
    "privatekey":   "./secret/privatekey",
    "wgconfig":     "./config/wgconfig.conf",
    "birdconfig":   "./config/birdconfig.conf",
    "wg_output":    "./output/",
    "bird_output":  "./output/"
}

def banner():
    banner = '''
             ____  _   _ _  _  ____     ____             __ _       
            |  _ \| \ | | || ||___ \   / ___|___  _ __  / _(_) __ _ 
            | | | |  \| | || |_ __) | | |   / _ \| '_ \| |_| |/ _` |
            | |_| | |\  |__   _/ __/  | |__| (_) | | | |  _| | (_| |
            |____/|_| \_|  |_||_____|  \____\___/|_| |_|_| |_|\__, |
                                                              |___/ 
                  ____                           _             
                 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
                | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
                | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
                 \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                    '''
    print( banner)


def getPrivateKey():
    with open(template["privatekey"],"r") as f:
        key = f.read()
    return key.strip()

class Peer():
    def __init__(self,
                 asn :str, peer :str,
                 pubIP :str, pubkey :str,
                 dn42IPv4 :str, dn42IPv6 :str ):
        self.peername = peer
        self.asn = asn
        self.publicIP = pubIP
        self.publickey = pubkey
        self.dn42IPv4 = dn42IPv4
        self.dn42IPv6 = dn42IPv6

        # set dicts
        self.public = {
            "[YOUR_PUBLIC_KEY]": self.publickey,  # peer wg public key
            "[YOUR_IP]": self.publicIP,  # peer real world ip support domain like kali.esonhugh.me
        }
        self.dn42 = {
            "[YOUR_DN42_IPv4]": self.dn42IPv4,  # peer dn42 ipv4 addr
            "[YOUR_DN42_IPv6]": self.dn42IPv6,  # peer dn42 ipv6 addr
        }


    def wgReplaceRule(self):
        replaceRule = {
            "[MY_PRIVATEKEY]":              getPrivateKey(),
            "[PEER_NAME]":                  self.peername,  # peer network name
            "[LAST_5_DIGITS_OF_YOUR_ASN]":  self.asn[-5:],  # peer server listening port, normal is last 5 digits of here asn
        }
        replaceRule.update(self.dn42)
        replaceRule.update(self.public)
        return replaceRule

    def birdReplaceRule(self):
        replaceRule = {
            "[PEER_NAME]": self.peername,  # peer network name
            "[YOUR_ASN]": self.asn,  # peer network asn
        }
        replaceRule.update(self.dn42)
        return replaceRule

    # log usage
    @property
    def infoDict(self):
        info= {
            "[PEER_NAME]":                  self.peername, # peer network name
            "[YOUR_ASN]":                   self.asn, # peer network asn
            "[LAST_5_DIGITS_OF_YOUR_ASN]":  self.asn[-5:], # peer server listening port, normal is last 5 digits of here asn
        }
        info.update(self.dn42)
        info.update(self.public)
        return info

    # strings
    def __dict__(self):
        return self.infoDict
    def __str__(self):
        return self.infoDict.__repr__()
    def __repr__(self):
        return self.infoDict.__repr__()

if __name__ == "__main__":
    peer = Peer(asn="4242422239",peer="eson",
                pubIP="kali.esonhugh.me",pubkey="This is the pubkey",
                dn42IPv4="172.20.42.193",dn42IPv6="fe80:2239"
                )
    print(peer)
    print()
    print(peer.wgReplaceRule())
    print(peer.birdReplaceRule())