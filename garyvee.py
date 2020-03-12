from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import time
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


class GaryVee:
    username = 'garyveedollareighty'
    password = 'dollareighty'
    people = []
    likes = []
    comments = []
    current_followers = []
    hashtags = [
        'elkhart', 'elkahrtindiana', 'elkhartcounty', 'elkhartcounty4hfair', 'elkhartcountyparks', 
        'downtownelkhart', 'elkhartartwalk', 'elkhartcountyhistory', 'elkharteats', 'elkhartphotographystudio',
    ]

    comments = [
        'Your posts are amazing', 'Amazing work. Keep going!', 'Your photos are magnificent',
        'Your work fascinates me!', 'I like how you put your posts together', 'Great job',
        'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing',
    ]

    links = []

    price = 0.0

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.login()
        self.hustle()

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
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
            time.sleep(2)

            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range(0, 9):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    def execute(self):
        for link in self.links:
            self.browser.get(link)
            time.sleep(1)

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            self.comment()
            time.sleep(2)
            
            self.like()

            self.price += 0.02
            sleeptime = random.randint(18, 28)
            time.sleep(sleeptime)

    def comment(self):
        comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
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

    def finalize(self):
        self.browser.close()
        print("finished sucessfully")
        sys.exit()

if __name__ == '__main__':
    app.run()
    garyVee = GaryVee()


