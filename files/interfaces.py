#!/usr/bin/env
import json
import sys
import re

def add_int_collection(hostname):
#variables
    hostpath = "/etc/ansible/roles/huawei-sw-facts_telnet/temp/"+hostname
    int_file = "/etc/ansible/roles/huawei-sw-facts_telnet/files/facts/"+hostname+".ansible_net_interfaces.json"

#Loading interface information
    with open(hostpath) as f:
        int = f.read()

#split each interface into a list and remove unwanted information
    int = int.split("Output bandwidth utilization : ")
    int = int[:-1]

#create each interface information into one JSON and pick it into a file
    with open(int_file, 'w') as outfile:
        for i in range(len(int)):
            int_temp = ""
            interface = re.findall('\w+', int[i].split(' current state')[0].split('\n')[-1])
            if len(interface) > 1:
                interface_temp = ""
                for int_no in range(len(interface)):
                    interface_temp+=interface[int_no]+"/"
                interface=interface_temp[:-1]
            if len(interface) == 1:
                interface=interface[0]
            int_temp+=("{\"interface\":\""+interface+"\",")
            operstatus = re.findall(': \w+', int[i])[0][2:]
            int_temp+=("\"operstatus\":\""+operstatus+"\",")
            lineprotocol = re.findall(': \w+', int[i])[1][2:]
            int_temp+=("\"lineprotocol\":\""+lineprotocol+"\",")
            type_var = re.findall('\n[A-z]+', int[i])[0]
            type_var = re.findall('\w+', type_var)[0]
            int_temp+=("\"type\":\""+type_var+"\",")
            if "thernet" not in interface:
                int_temp+=("\"macaddress\":null,")
                int_temp+=("\"duplex\":null,")
            else:
                try:
                    macaddress = re.findall('s \w+-\w+-\w+', int[i])[0][2:]
                    int_temp+=("\"macaddress\":\""+macaddress+"\",")
                except IndexError:
                    int_temp+=("\"macaddress\":null,")
                duplex = re.findall('x: \w+', int[i])[0][3:]
                int_temp+=("\"duplex\":\""+duplex+"\",")
            if ("Port Mode" in int[i] and "COPPER" in int[i]):
                mediatype = re.findall('Mode: \w+ \w+', int[i])[0][6:]
                int_temp+=("\"mediatype\":\""+mediatype+"\",")
            elif ("Port Mode" in int[i] and "Transceiver" in int[i]):
                mediatype = re.findall('Transceiver: \w+', int[i])[0][13:]
                int_temp+=("\"mediatype\":\""+mediatype+"\",")
            else:
                int_temp+=("\"mediatype\":null,")
            try:
                if int[i].find('escription') > 0:
                    description = re.findall('n:\w+.*', int[i])[0][2:]
                    int_temp+=("\"description\":\""+description+"\",")
            except IndexError:
                int_temp+=("\"description\":null,")
            if int[i].find('Internet address') > 0:
                address = re.findall("\d+.\d+.\d+.\d+",int[i])[0]
                subnet =  re.findall("/\d+",int[52])[0]
                subnet = re.findall("\d+",subnet)[0]
                int_temp+=("\"ipv4\":[{\"address\":\""+address+"\",\"subnet\":\""+subnet+"\"}],")
            else:
                pass
            try:
                mtu = re.findall("U is \d+",int[53])[0][-4:]
            except IndexError:
                mtu = "unknow"
            int_temp+=("\"mtu\":\""+mtu+"\",")
            bandwidth = "null"
            int_temp+=("\"bandwidth\":"+bandwidth+"}")
            #convert string int to json string(u')
            int_temp = int_temp.replace("\r", " ")
            int_temp = json.loads(int_temp)
            json.dump(int_temp, outfile)
    outfile.closed

if __name__ == '__main__':
    add_int_collection(sys.argv[1])
