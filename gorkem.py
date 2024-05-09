import requests
import xml.etree.ElementTree as ET
import time 

def get_external_xml(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
    
def write_to_xml(data, filename):
    root = ET.fromstring(data)
    tree = ET.ElementTree(root)
    tree.write(filename)

if __name__ == "__main__":
    external_url = "http://88.250.204.138:4545/status.xml" // bu siteden al 
    local_xml_file = "status.xml" // bu dosyaya yazdır 

    while True:
        external_data = get_external_xml(external_url)
        if external_data:
            write_to_xml(external_data, local_xml_file)
        else:
            print("Dış ıp üzerinden veri alınamadı")

        time.sleep(30)
 
