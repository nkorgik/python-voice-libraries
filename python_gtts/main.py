"""This is just a simple example of using gTTS -- text to speech code example"""
import json
import logging
import os

from gtts import gTTS


class Text:
    def __init__(self, id: int, title: str, content: str) -> None:
        """Initialize Text object for further processing

        Args:
            id (int): id of the text for handling
            title (str): the title, there should be because it's human-friendly for id, but not identical
            content (str): the main content which must be processed
        """
        self.id = id
        self.title = title
        self.content = content

    def __repr__(self) -> str:
        return f"Text(id={self.id}, title='{self.title}')"
    

class TextList:
    def __init__(self, filename) -> None:
        """Initialize TextList object for further processing

        Args:
            filename (str): filename of the file-json
        """
        self.texts = [] # list of texts
        self.filename = filename # filename
        self.load_data() # load data from file-json 

    def load_data(self) -> None:
        """Load data from file-json

        Returns:
            None
        """
        try:
            with open(self.filename, 'r') as fd:
                data = json.load(fd) # data from file-json - that's python dictionary object
                for text in data:
                    self.texts.append(Text(text['id'], text['title'], text['content'])) # composition of text list
            
        except Exception as _ex:
            logging.error(f'Error was occured during opening JSON - {_ex}')
            
            
    def save_audio(self, title):
        """Save audio file

        Args:
            title (str): title of the audio file
        """
        try:
            for data in self.texts:
                if data.title == title:
                    tts = gTTS(text=data.content, lang='en')
                    tts.save(f'./audio/{title}.mp3')
                    logging.info(f'Audio saved to./audio/{title}.mp3')
                    break
                
                raise ValueError(f'There is no text-content with such a title - {title}')
        except Exception as _ex:
            logging.error(f'Error while saving audio - {_ex}')
        

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__)) # make sure

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: %(message)s",
        filemode='a',
        filename='logs.text'
    )
        
    try:
        text_list = TextList('texts.json')
        text_list.save_audio('Foo')
    except Exception as _ex:
        logging.error(_ex)
        

