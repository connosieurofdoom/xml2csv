"""
Written by Shreyas Keelary
Call isol(src) to get a list of all tags in the xml doc
Call xmltocsvconv(src,dest,parent,tags) to convert the xml file at src to csv file at dest.
"""
def isol(src):
        import xml.parsers.expat
        import re
        tags = {}
        counter = 1

        def start_element(name, attrs):
                nonlocal counter,tags
                if name not in tags.values():
                        tags[counter]=name
                        counter += 1
                else:
                        pass

        def parse(src):

                parser = xml.parsers.expat.ParserCreate()
                parser.StartElementHandler = start_element
                #parser.EndElementHandler = end_element
                #parser.CharacterDataHandler = character_data
                parser.ParseFile(open(src,'rb'))
                print(tags)
        parse(src)
        
        return [tags[k] for k in tags.keys()]
    


try: 
    import pandas as pd
except ImportError as e:
    from pip._internal import main
    main(['install','pandas'])

import xml.etree.ElementTree as et


def xmltocsvconv(src,dest,parent,tags):
    import os
    def xmlpstr(src):
        import re
        
        cwd = os.getcwd()
        
        temp = cwd+'temp.xml'
        #src = str(input("source file:"))
        #otp = str(input("output file:"))
        f2 = open(temp,'w')
        with open(src) as f1:
            for i in f1:
                f2.write(re.sub('\s(\s+)|\n|\r','',i))
        return temp

    def conv(temp,dest,parent,tags):
        dict1 = dict()
        for i in tags:
            dict1[i]=[]
        xtree = et.parse(src)
        xroot = xtree.getroot()
        for node in xroot: 
            parent = node.attrib.get(parent)
            for j in tags:
                dict1[j].append(node.find(j).text)
        
        df = pd.DataFrame.from_dict(dict1)
        df.to_csv(dest)
        os.remove(temp)
        return df
    
    temp = xmlpstr(src)
    df = conv(temp,dest,parent,tags)

    return df


"""
src= 'D:/pr/books.xml'
dest = 'D:/pr/otp2.xml'


df = xmltocsvconv(src,dest,"book",["author","title","genre","price","publish_date","description"])
print(df)
"""