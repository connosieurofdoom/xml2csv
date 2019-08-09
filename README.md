# xml2csv
Converts xml to csv


Contains two functions :  </br>
 1.isol(src)  : Returns a list of all tags in the xml. Uses expat parser.  </br>
 2.xmltocsvconv(src,dest,parent,tags) :Returns a pandas dataframe object while also writing csv to the dest file.  </br>
 
 Here :  </br>
 1.src is the source xml file.  </br>
 2.dest is the destination csv file.  </br>
 3.parent is the name of the parent tag.  </br>
 4.tags is a list of all column headers that come under the parent tag.  </br>
 
 
 NOTE: This assumes that the xml column tags do not have further nested children tags to be processed. Under a condition that such a tag is experienced, they would be treated as plain text.
 
