import xml.etree.ElementTree as ET

def ids_by_message(xml, message):
    root = ET.fromstring(xml)

    result = []
    for index in range(len(root)):
        if root[index][0].text == message:
            result.append(int(root[index].attrib['id']))

    return result

xml = """<?xml version="1.0" encoding="UTF-8"?>
<log>
    <entry id="1">
        <message>Application started</message>
    </entry>
    <entry id="2">
        <message>Application ended</message>
    </entry>
</log>"""

print(ids_by_message(xml, 'Application ended'))