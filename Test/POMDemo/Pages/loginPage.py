from Test.POMDemo.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver #now we need to create locators. In login page, we have 3 locators, username,password & login.
        #format(generally) used in naming is, name_type_locator_type_we_have_used. It is an intuitive format which can be used/remembered even after a long time.
        # self.username_textbox_id = "txtUsername"
        self.username_textbox_id = Locators.username_textbox_id #after importing locators, instead of hard coding values we can use this

        # self.password_textbox_id = "txtPassword"
        self.password_textbox_id = Locators.password_textbox_id #after importing locators, instead of hard coding values we can use this

        # self.login_button_id = "btnLogin"
        self.login_button_id = Locators.login_button_id #after importing locators, instead of hard coding values we can use this
        #We can add for welcome & logout too. But because POM says separate class for separate Page, it will be defined in another Page

        #Functions or action methods

    def enter_username(self, username): #username is an argument we are passing
        self.driver.find_element_by_id(self.username_textbox_id).clear() #Good practice to clear the box before passing any values
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)


    def enter_password(self, password):  # password is an argument we are passing
        self.driver.find_element_by_id(self.password_textbox_id).clear()  # Good practice to clear the box before passing any values
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self): #no argument as we are just clicking on the button
        self.driver.find_element_by_id(self.login_button_id).click()

