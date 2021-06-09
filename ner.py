#Name entity recognization by using spacy
#studied from link- https://github.com/raaga500/YTshared/blob/master/V3_NamedEntityReco_3.ipynb
import spacy 
from spacy import displacy

Text= "Zee News is an Indian Hindi-language news channel owned by the Essel Group. It is associated with several other sister news channels which provide coverage in Hindi, English and several regional languages of India. Zee News was launched on 27 August 1999, as Zee Sports Ltd. The company was reincorporated on 27 May 2004, as Zee News Ltd. In 2013, Zee News Ltd changed its name to Zee Media Corporation Limited.[3] The Zee News channel is the flagship channel of the company."

nlp = spacy.load("en_core_web_sm") #core small versions of the English language library
doc = nlp(Text)

entities = []             #list to store entities

for ent in doc.ents:      #loop to run through the text
    entities.append(ent)  #appending (adding) entities
    
df = pd.DataFrame({'Entities':entities,}) #creating a data frame to print

print(df)