import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import pyarrow
from bs4 import BeautifulSoup

lyrics_pd = pd.read_feather(
  'C:/Users/antfe/OneDrive/Unstructured Analytics/complete_lyrics_2025.feather'
)

GBA = lyrics_pd.iloc[127]
GBA_lyrics = GBA['lyrics']

GBA_lyrics_clean = BeautifulSoup(GBA_lyrics, 'html.parser').get_text()

GBA_list = GBA_lyrics_clean.splitlines()

GBA_pd = pd.DataFrame(GBA_list, columns=['lyrics'])

GBA_pd['lyrics'] = (
    GBA_pd['lyrics']
    .str.replace(r'(\[.*?\])', '', regex=True)  
    .str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True)  
)

GBA_pd
