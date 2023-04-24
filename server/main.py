import streamlit as st
from PIL import Image
import pytesseract
from PIL import Image
from PIL import Image

from PIL import Image
BG = Image.open("myfont/bg.png")
sizeOfSheet =BG.width
gap, _  = 0,0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'
def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("myfont/%s.png"%char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95*(len(word)):
        gap = 0
        _ += 200
    for letter in word:        
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'            
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)
def worddd(Input):
    wordlist=Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')
if __name__ == '__main__':
    try:
        with open('sample.txt', 'r') as file:
            data = file.read().replace('\n', '')
        l=len(data)
        nn=len(data)//600
        chunks, chunk_size = len(data), len(data)//(nn+1)
        p=[ data[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        
        for i in range(0,len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('%doutt.png'%i)
            BG1= Image.open("myfont/bg.png")
            BG=BG1
            gap = 0
            _ =0
    except ValueError as E:
        print("{}\nTry again".format(E))

from fpdf import FPDF
from PIL import Image

imagelist=[]
for i in range(0,len(p)):
    imagelist.append('%doutt.png'%i)

#Converting images to pdf
#Source:https://datatofish.com/images-to-pdf-python/


def pdf_creation(PNG_FILE,flag=False):
    rgba = Image.open(PNG_FILE)
    rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
    rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
    rgb.save('final_output.pdf', append=flag)  #Now save multiple images in same pdf file

#First create a pdf file if not created
pdf_creation(imagelist.pop(0))

#Now I am opening each images and converting them to pdf 
#Appending them to pdfs
for PNG_FILE in imagelist:
    pdf_creation(PNG_FILE,flag=True)


def pdfToText(path):
    pdfreader = PyPDF2.PdfFileReader(path)
    no_of_pages = pdfreader.numPages
    with open('final_txt.txt', 'w') as f:
        for i in range(0, no_of_pages):
            pagObj = pdfreader.getPage(i)
            f.write(pagObj.extractText())
    with open('final_txt.txt', 'r') as f:
        text = f.read()
    if os.path.exists("final_txt.txt"):
        pass
        return text
    

style_name = st.sidebar.selectbox(
    'Select HandWriting',
    ("Style-1", "Style-2", "Style-3", "Style-4", "Style-5")
)
root_style = "./images/"
path_style = os.path.join(root_style, style_name+".jpg")
root_font = "./Fonts/"

# Upload text file functionality
img = None
uploaded_file = st.file_uploader(
    "Choose a text file...", type=["txt", "docx"])

show_file = st.empty()

# checking if user has uploaded any file
if not uploaded_file:
    show_file.info(
        "Please Upload the text/docx document (no .doc only .docx and .txt) ")


if uploaded_file is not None:

    if file is not None:
        try:
            text_data = pdfToText(file)
            st.write("text generated")
            with open('final_txt.txt', 'r') as file:
                data = file.read().replace('\n', '')

            st.write(data)
            l=len(data)
            nn=len(data)//600
            chunks, chunk_size = len(data), len(data)//(nn+1)
            p= [data[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
            print("value of p is ",p)
            for i in range(0,len(p)):
                worddd(p[i])
                writee('\n')
                BG.save('%doutt.png'%i)
                BG1= Image.open("myfont/bg.png")
                BG=BG1
                gap = 0
                _ =0
        except ValueError as E:
            print("{}\nTry again".format(E))

    ###########################
    file_details = {"Filename": uploaded_file.name,
                    "FileType": uploaded_file.type}
    st.write(file_details)

    if uploaded_file.type == "text/plain":
        raw_text = str(uploaded_file.read(), "utf-8")

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

        raw_text = docx2txt.process(uploaded_file)

    ###########################

    size = f' Input File Size in MegaBytes is {"{0:.4f}".format(uploaded_file.size / (1024 * 1024))}'
    st.markdown("%s" % size,
                unsafe_allow_html=True)

    name, _ = uploaded_file.name.split('.')

    convert_button = st.button("Convert To Text")

    # user presses convert
    if convert_button:

        lines = raw_text.split("\n")  # splitting text on the basis of new line

        dt.background = Image.open("./images/a4.jpg")

        dt.SheetWidth = dt.background.width
        dt.SheetHieght = dt.background.height

        dt.margin = 115
        dt.lineMargin = 115
        dt.allowedCharacters = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ
                                abcdefghijklmnopqrstuvwxyz
                                #:,.?-!()[]'<>=%^$@_;1234567890 "'''

        dt.wordsPerLine = 75
        dt.maxLenPerPage = 3349
        dt.pageNum = 1

        dt.FontType = os.path.join(root_font, style_name)

        dt.lineGap = 120
        dt.writing = style_name

        # Initializing x and y
        dt.x, dt.y = dt.margin + 20, dt.margin + dt.lineGap

        # Asking for the quality of the output
        dt.scale_percent = 30
        dt.images_list = []

        final_image = do_work(lines, name)

        path = name + '_' + style_name + '_output.pdf'

        with tempfile.TemporaryDirectory() as tmpdirname:

            final_path = os.path.join(tmpdirname, path)
            final_image.save(final_path)

            file_stats = os.stat(final_path)

            size_file = file_stats.st_size / (1024 * 1024)

            s = f'Output File Size in MegaBytes is {"{0:.2f}".format(size_file)}'
            st.markdown("%s" % s,
                        unsafe_allow_html=True)

            st.markdown(get_binary_file_downloader_html(
                final_path, file_label='File'), unsafe_allow_html=True)