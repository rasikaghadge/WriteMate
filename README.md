# WriteMate - Text to Handwriting
## Tech-A-Thon Project at D Y Patil Institute of Technology, Pimpri.

In a world where technology has made typing the primary means of communication, the art of handwriting has been lost to some extent. While typing is undoubtedly efficient, it can lack the personal touch and authenticity that handwritten notes and letters possess.
Our typed text to handwriting converter web app aims to bridge the gap between the convenience of typing and the authenticity of handwriting. With our app, you can now convert typed text into beautiful, personalized handwriting styles that look like they were written by hand.
Whether you want to add a personal touch to a greeting card, create a handwritten letter, or simply enjoy the aesthetics of handwritten text, our app is the perfect solution. Our advanced handwriting recognition technology accurately converts typed text to realistic handwriting in a variety of styles and fonts.
We believe that our app has the potential to revolutionize the way we communicate and bring back the beauty of handwritten text in a digital age.

## Live app
https://writemate.streamlit.app/

## User Guide:
Uploading Text: To use the app, simply click on the browse files you want to convert on the app's homepage. The app supports file size upto 200MB, from a single word to a long document.
Choosing a Handwriting Style: You can change the handwriting style from the side menu. There are 5 different styles available right now.
Converting Text to Handwriting: Once you've selected your preferred handwriting style and made any desired customization, click on the "Convert" button to convert your typed text into handwritten text. The pdf with converted text will be downloaded.

## Technical Documentation:
The typed text to handwriting converter web app has been implemented using Python for the backend and Streamlit for the frontend.

### Backend Implementation:
Processing: The app processes the handwriting styles and fonts by mapping each character with the corresponding alphabet style
PDF Generation: The app writes the generated handwriting to a PDF file using the PyPDF2 library.

### Frontend Implementation:
User Interface: The app uses Streamlit to create a simple and intuitive user interface. The user interface allows users to upload their text, choose a handwriting style, customize the font thickness and color, preview the converted handwriting, edit the converted handwriting, and export the converted handwriting.
Integration with Backend: The frontend of the app integrates seamlessly with the backend, allowing users to convert their typed text into personalized handwriting with just a few clicks.

## Future Work:
1.	Language Support: Adding support for additional languages beyond English to expand the app's user base
2.	Handwriting Customization: Expanding the app's handwriting customization options to allow users to upload and use their own handwriting styles and fonts.
3.	Multiple backgrounds: Allowing users to change the backgrounds from plain white to ruled pages


