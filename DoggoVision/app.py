# AUTOGENERATED! DO NOT EDIT! File to edit: ../AppNotebook.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% ../AppNotebook.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../AppNotebook.ipynb 3
learn = load_learner('model_dogs.pkl')

# %% ../AppNotebook.ipynb 5
categories = ('Chihuahua',
 'Japanese_spaniel',
 'Maltese_dog',
 'Pekinese',
 'Shih',
 'Blenheim_spaniel',
 'papillon',
 'toy_terrier',
 'Rhodesian_ridgeback',
 'Afghan_hound',
 'basset',
 'beagle',
 'bloodhound',
 'bluetick',
 'black',
 'Walker_hound',
 'English_foxhound',
 'redbone',
 'borzoi',
 'Irish_wolfhound',
 'Italian_greyhound',
 'whippet',
 'Ibizan_hound',
 'Norwegian_elkhound',
 'otterhound',
 'Saluki',
 'Scottish_deerhound',
 'Weimaraner',
 'Staffordshire_bullterrier',
 'American_Staffordshire_terrier',
 'Bedlington_terrier',
 'Border_terrier',
 'Kerry_blue_terrier',
 'Irish_terrier',
 'Norfolk_terrier',
 'Norwich_terrier',
 'Yorkshire_terrier',
 'wire',
 'Lakeland_terrier',
 'Sealyham_terrier',
 'Airedale',
 'cairn',
 'Australian_terrier',
 'Dandie_Dinmont',
 'Boston_bull',
 'miniature_schnauzer',
 'giant_schnauzer',
 'standard_schnauzer',
 'Scotch_terrier',
 'Tibetan_terrier',
 'silky_terrier',
 'soft',
 'West_Highland_white_terrier',
 'Lhasa',
 'flat',
 'curly',
 'golden_retriever',
 'Labrador_retriever',
 'Chesapeake_Bay_retriever',
 'German_short',
 'vizsla',
 'English_setter',
 'Irish_setter',
 'Gordon_setter',
 'Brittany_spaniel',
 'clumber',
 'English_springer',
 'Welsh_springer_spaniel',
 'cocker_spaniel',
 'Sussex_spaniel',
 'Irish_water_spaniel',
 'kuvasz',
 'schipperke',
 'groenendael',
 'malinois',
 'briard',
 'kelpie',
 'komondor',
 'Old_English_sheepdog',
 'Shetland_sheepdog',
 'collie',
 'Border_collie',
 'Bouvier_des_Flandres',
 'Rottweiler',
 'German_shepherd',
 'Doberman',
 'miniature_pinscher',
 'Greater_Swiss_Mountain_dog',
 'Bernese_mountain_dog',
 'Appenzeller',
 'EntleBucher',
 'boxer',
 'bull_mastiff',
 'Tibetan_mastiff',
 'French_bulldog',
 'Great_Dane',
 'Saint_Bernard',
 'Eskimo_dog',
 'malamute',
 'Siberian_husky',
 'affenpinscher',
 'basenji',
 'pug',
 'Leonberg',
 'Newfoundland',
 'Great_Pyrenees',
 'Samoyed',
 'Pomeranian',
 'chow',
 'keeshond',
 'Brabancon_griffon',
 'Pembroke',
 'Cardigan',
 'toy_poodle',
 'miniature_poodle',
 'standard_poodle',
 'Mexican_hairless',
 'dingo',
 'dhole',
 'African_hunting_dog') 

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

# %% ../AppNotebook.ipynb 7
image = gr.inputs.Image(shape=(128,128))
label = gr.outputs.Label()
examples = ['dog.jpg']

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)