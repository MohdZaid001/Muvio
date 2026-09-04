import edge_tts
import asyncio
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" 

import pygame

async def speaking(text):
    voice = "hi-IN-MadhurNeural" 
    
    communicate = edge_tts.Communicate(text, voice, rate="+30%", pitch="+25Hz")
    await communicate.save("output.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.quit()
    os.remove("output.mp3")

def speak(text):
    asyncio.run(speaking(text))
