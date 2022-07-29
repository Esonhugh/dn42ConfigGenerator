# DN42 config generator

# Demo
```
 py main.py hand -s '{"name": "esonhugh", "asn": "4242422239", "dn42_ipv4": "172.20.42.193", "dn42_ipv6": "fe80::2239", "wg_public_key": "this is public key", "public_ip": "kali.esonhugh.me"}'

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
                                                                    
[*] Generate Peering Object ...
[+] Generate Success! 
[*] wireguard config generator init ...
[+] wireguard config generate successfully
[+] flie at  ./output/esonhugh_wg.conf
[*] bird config generator init ...
[+] bird config generate successfully
[+] flie at  ./output/esonhugh_bird.conf
```

# Usage

1. change the config.py file with your flavour
2. change the config template file with you personal infomation
3. get peer's json file which contains his infomation

```
usage: peerConfiger.py [-h] [-d DIR] [-f FILE] [-n NAME] [--asn ASN] [--pub-ip PUB_IP] [--pub-key PUB_KEY] [--dn42-ipv4 DN42_IPV4] [--dn42-ipv6 DN42_IPV6] [-s JSON_STR] [-v]
                       {file,hand}

positional arguments:
  {file,hand}           change jsonfile read mode and

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     config output dir,at default it will add a new folder at this repos output dir
  -f FILE, --file FILE  [file mode] json format config file
  -n NAME, --name NAME  [hand mode 1] peer name
  --asn ASN             [hand mode 1] peer asn
  --pub-ip PUB_IP       [hand mode 1] peer public ip allow the domain
  --pub-key PUB_KEY     [hand mode 1] peer wg public key
  --dn42-ipv4 DN42_IPV4
                        [hand mode 1] peer dn42 ipv4
  --dn42-ipv6 DN42_IPV6
                        [hand mode 1] peer dn42 ipv6
  -s JSON_STR, --json-str JSON_STR
                        [hand mode 2] json strings contains all info above.
  -v, --output-json     print the config json only

```
