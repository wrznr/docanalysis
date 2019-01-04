import os.path
from xml.dom import minidom
import ocrolib

__all__ = [
    'parseXML',
    'write_to_xml'
    'print_info',
]

def print_info(*objs):
    print("INFO: ", *objs, file=sys.stdout)

def parseXML(fpath, Input):
    input_files = []
    xmldoc = minidom.parse(fpath)
    nodes = xmldoc.getElementsByTagName('mets:fileGrp')
    for attr in nodes:
        if attr.attributes['USE'].value == Input:
            childNodes = attr.getElementsByTagName('mets:FLocat')
            for f in childNodes:
                input_files.append(f.attributes['xlink:href'].value)
    return input_files


def write_to_xml(fpath, mets, Output, OutputMets, work):
    xmldoc = minidom.parse(mets)
    subRoot = xmldoc.createElement('mets:fileGrp')
    subRoot.setAttribute('USE', Output)

    for f in fpath:
        basefile = ocrolib.allsplitext(os.path.basename(f))[0]
        child = xmldoc.createElement('mets:file')
        child.setAttribute('ID', 'CROP_'+basefile)
        child.setAttribute('GROUPID', 'P_' + basefile)
        child.setAttribute('MIMETYPE', "image/png")

        subChild = xmldoc.createElement('mets:FLocat')
        subChild.setAttribute('LOCTYPE', "URL")
        subChild.setAttribute('xlink:href', f)

        subRoot.appendChild(child)
        child.appendChild(subChild)

    xmldoc.getElementsByTagName('mets:fileSec')[0].appendChild(subRoot)

    if not OutputMets:
        metsFileSave = open(os.path.join(
            work, os.path.basename(mets)), "w")
    else:
        metsFileSave = open(os.path.join(work, OutputMets if OutputMets.endswith(
            ".xml") else OutputMets+'.xml'), "w")
    metsFileSave.write(xmldoc.toxml())
