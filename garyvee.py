from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import time
import sqlite3
import datetime
import re
import fnmatch

class GaryVee:
    conn = sqlite3.connect('instagram2.db')

    c = conn.cursor()


    username = 'grizzlytreeservice'
    password = 'Cheerup22!'
    links = []
    hashtags = []
 
    visited = []
    comments = [
        'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
        'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
        'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing',
    ]


    price = 0.0
    


    def __init__(self):
        self.browser = webdriver.Firefox(executable_path="./geckodriver")
        self.loadHash()
        self.loadVisited()
        self.login()
        self.hustle()

    def loadHash(self):
        g = self.conn.execute("SELECT hash from hashes")
        for gg in g:
            self.hashtags.append(str(gg[0]))
        print(self.hashtags)

    def loadVisited(self):
        g = self.conn.execute("SELECT url from vistedlinks")
        for ccc in g:
            self.visited.append(ccc[0])
        print("##########################################")
        print(self.visited)

    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)

        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(2)

    def hustle(self):
        self.getTopPosts()
        self.execute()
        self.finalize()

    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags' + hashtag)
            time.sleep(5)

            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            #try is for when page has less than 10 post
            try:
                 for i in range(0, 9):
                    link = valid_links[i].get_attribute('href')
                
                 
                    if link not in self.links:
                        print("adding")
                        self.links.append(link)
                    else:
                        print("Already commented on Post")
                       
            except:
                pass

    def execute(self):
        for link in self.links:
            self.browser.get(link)
            
            time.sleep(1)
            

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            self.getNewHash()
            #self.comment()
            time.sleep(2)
            
            #self.like()

            self.price += 0.02
            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
        time.sleep(2)
        comment_input().click()
        comment_input().clear()

        comment = random.choice(self.comments)
        for letter in comment:
            comment_input().send_keys(letter)
            delay = random.randint(1, 7) / 30
            time.sleep(delay)

        comment_input().send_keys(Keys.RETURN)

    def like(self):
        like_button = lambda: self.browser.find_element_by_class_name('wpO6b ')
        like_button().click()
 

    def getNewHash(self):
        pattern_list = ['elkhart', 'goshen', 'granger', 'southbend', 'mishawka', 'indiana', 'saintjoe', 'michiana']
        #new_hash = self.browser.find_elements_by_tag_name('a')
        hashes = self.browser.find_elements_by_class_name('xil3i')

        condition = lambda link: '.com/explore/' in link.get_attribute('href')
        valid_hash = list(filter(condition, hashes))
        #th.append(valid_links)
        
        for i in range(len(valid_hash)-1):
            hashlink = valid_hash[i].get_attribute('href')

            for pattern in pattern_list:
                if pattern in hashlink:
                    s = hashlink
                    start = s.find('tags/') + 4
                    sss = s[start::]
                    print(sss)
                    if sss not in self.hashtags:
                        self.c.execute('INSERT INTO hashes VALUES (?,?)', [(sss),("none")])
                        self.conn.commit()
                        print("added new hashag: ", hashlink)
                    else:
                        pass
                else:
                    pass
    def finalize(self):
        self.browser.close()
        print("finished sucessfully")
        for llinks in self.links:
            self.c.execute('INSERT INTO vistedlinks VALUES (?,?)', [('2006-03-28'),(llinks)])
            self.conn.commit()
         hashtags = ['elkhart', 'elkahrtindiana', 'elkhartcounty', 'elkhartcounty4hfair', 'elkhartcountyparks', 
                    'downtownelkhart', 'elkhartartwalk', 'elkhartcountyhistory', 'elkharteats', 'elkhartphotographystudio']

        print(self.links)
        self.conn.close()
        sys.exit()


if __name__ == '__main__':
    garyVee = GaryVee()

