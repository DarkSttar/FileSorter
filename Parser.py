import sys
from pathlib import Path
# iMAGES
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
# VIDEO
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
# DOCUMENTS
DOC_DOCUMENTS = []
DOCX_DOCUEMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
# AUDIO
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
#OTHER
OTHER_FILES = []
#ARCHIVES
ARCHIVES_ZIP = []
ARCHIVES_GZ = []
ARCHIVES_TAR = []


REGISTER_EXTENTION = {
    'JPEG' : JPEG_IMAGES, 'JPG' : JPG_IMAGES, 'PNG' : PNG_IMAGES, 'SVG' : SVG_IMAGES,
    
    'AVI': AVI_VIDEO, 'MP4': MP4_VIDEO, 'MOW': MOV_VIDEO, 'MKV': MKV_VIDEO,
    
    'DOC': DOC_DOCUMENTS, 'DOCX': DOCX_DOCUEMENTS, 'TXT': TXT_DOCUMENTS, 'PDF': PDF_DOCUMENTS, 'XLSX': XLSX_DOCUMENTS,'PPTX': PPTX_DOCUMENTS,
    
    'MP3':MP3_AUDIO,'OGG':OGG_AUDIO,'WAV':WAV_AUDIO,'AMR': AMR_AUDIO,
    
    'OTHER':OTHER_FILES,
    
    'ZIP':ARCHIVES_ZIP, 'GZ': ARCHIVES_GZ, 'TAR': ARCHIVES_TAR,

}

FOLDERS = []
EXTENTIONS = set()
UNCNOWN = set()

def get_extention(name: str) -> str:
    return Path(name).suffix[1:].upper()

def scan_directory(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in('archives', 'video','audio','documents','images' 'OTHER_FILES'):
                FOLDERS.append(item)
                scan_directory(item)
            continue
        extention = get_extention(item.name)
        full_name = folder / item.name
        if not extention:
            OTHER_FILES.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENTION[extention]
                ext_reg.append(full_name)
                EXTENTIONS.add(extention)
            except KeyError:
                UNCNOWN.add(extention)
                OTHER_FILES.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan_directory(Path(folder_process))
    

    
    