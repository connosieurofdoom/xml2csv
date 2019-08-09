from xml2csvmk4 import *
src = 'D:/pr/books.xml'
dest = 'D:/pr/otp2.csv'

tags = isol(src) 
print(tags)

import pandas as pd
df = xmltocsvconv(src,dest,tags[2],tags[3:])
print(df)