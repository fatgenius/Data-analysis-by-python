# Data-analysis-by-python
Use python code to analysis data on the internet also get data out of internet

login.py will be the code for auto login a website can use code to instead of the mouse 
          but the login.py file do not have the function to handle the captcha 
          need use the opencv or other method to handle that 



first start the project scrapy :    scrapy projectname
                build the spider:   scrapy genrate projectname
                                    scrapy genrate projectname + domain name 
        
       
       
use the css or the xpatch to find the iteams;
scrapy shell:
fetch('website name ') 

running the scrapy project using :scrapy crawl projectname
save the jasonfile: scrapy crawl --set FEED_URI= filename.JL

using pipline to process the image: image p
first install pillow 
in the setting must enable the pipline to process image 
also set the pic location 
##readlink -f to check the file path 
