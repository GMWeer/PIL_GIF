#!/usr/bin/env python
# coding: utf-8

# In[16]:


from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(size, text):
    img = Image.new('RGB', (500, 60), "#50C878")
    draw = ImageDraw.Draw(img)
    draw.text((size[0], size[1]), text, font=fnt, fill="black")
    return img

frames = []

def roll(text):
    for i in range(len(text) + 1):
        new_frame = create_image_with_text((0, 0), text[:i])
        frames.append(new_frame)

# Customize font and text below
fnt = ImageFont.truetype(r'C:\USERS\GAYAN_10386\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\FMBINDUMATHI X.TTF', 40)
all_text = """ ,nkakd jQ kj jir 
 nÿ nr wvqfjk 
 iqn kj jirla fõjd'' ææ    
 2024''' 2024''' 2024''' """.splitlines()


# Display font information
print(f"Using font: {fnt.getname()}")

# Generate frames
[roll(text) for text in all_text]


# Display the number of frames generated
print(f"Number of frames generated: {len(frames)}")

# Save frames as a GIF
frames[0].save('new_year_jpg.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=80, loop=0)

# Display a message indicating successful completion
print("GIF creation complete.")


# In[ ]:




