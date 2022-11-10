from re import S

from pom_proj.config.config import Bug_report, Data
from pom_proj.pages.basePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys




class main(BasePage):

    def game_results(self):
        self.click(Data.close_cookie)
        self.click(Data.tennis)
        self.a = self.find_text(Data.first_player)
        self.b = self.find_text(Data.second_player)
        
    def automating_jira(self):
    
        self.browser.get(Data.jira_url)
        self.send_keys(Data.login_field,Data.jira_username)
        self.send_keys(Data.pass_field,Data.jira_pass)
        self.click(Data.login_btn)
        self.click(Data.projects_button)
        self.click(Data.project_name)
        self.click(Data.backlog_btn)
        self.send_keys(Data.body,Keys.DOWN)
        self.click(Data.create_issue_btn)
        self.send_keys(Data.issue_name_field,Bug_report.issue_name)
        self.click(Data.open_in_dialog_btn)
        self.click(Data.description_text)
        self.send_keys(Data.description_field,Bug_report.description)
        self.send_keys(Data.browse_btn,Data.screenshot_path)
        #self.click(Data.create_btn)
        sleep(10)
        execute_script = 0 
        
  
        
    
    
        

    
    
        
            
            
        

        
  