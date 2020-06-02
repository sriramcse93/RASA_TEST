from gtts import gTTS
import os
mytext = "welcome to india"
language = 'en'
obj = gTTS(text=mytext,lang=language,slow=False)
obj.save("D:\\test1.mp3")
#os.system(['mpg321', 'test.mp3','--play-and-exit'])