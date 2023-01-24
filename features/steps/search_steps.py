import time
from behave import *
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys


#Scenario 1
@given(u'open web music youtube')
def step_impl(context):
    context.browser.get("https://music.youtube.com/")
    assert(context.browser.title) == "YouTube Music"


@when(u'Click search menu')
def step_impl(context):
    context.browser.find_element(By.ID, "placeholder").click()


@when(u'Type sugeng dalu')
def step_impl(context):
    context.browser.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input").send_keys("sugeng dalu")


@when(u'click enter')
def step_impl(context):
    context.browser.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input").send_keys(Keys.ENTER)

@then(u'Display result data sugeng dalu')
def step_impl(context):
    time.sleep(2)
    assert(context.browser.find_element(By.XPATH, "//*[@id='contents']/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a").text) == "Sugeng Ndalu"
    
    
# Scenario 2
@when(u'Type kulpsihfkshp')
def step_impl(context):
     context.browser.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input").send_keys("kulpsihfkshp")


@then(u'Display no result found in the web')
def step_impl(context):
    time.sleep(2)
    assert(context.browser.find_element(By.XPATH, "//*[@id='items']/ytmusic-message-renderer/yt-formatted-string[1]").text) == "No results found"
    
#Scenario 3
@when(u'Type empty in search')
def step_impl(context):
    context.browser.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input").send_keys("")


@then(u'Stay in search menu')
def step_impl(context):
    assert(context.browser.find_element(By.XPATH, "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input").get_attribute("placeholder")) == "Search"