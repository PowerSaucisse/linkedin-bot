import selenium, time, os, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.linkedin.com/login/")
time.sleep(1)
driver.find_element_by_xpath("//button[@action-type='ACCEPT']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='username']").send_keys(os.environ.get("JOBBER_EMAIL"))
driver.find_element_by_xpath("//input[@id='password']").send_keys(os.environ.get("JOBBER_CREDENTIAL"))
time.sleep(0.5)
driver.find_element_by_xpath("//button[@data-litms-control-urn='login-submit']").click()
time.sleep(0.5)
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(1)

i = 1
while True:
    try:
        driver.find_element_by_xpath("//li[@class='mn-connection-card artdeco-list'][{0}]//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']".format(str(i))).click()
    except Exception as e:
        # //button[@class='artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button']
        driver.find_element_by_xpath("//button[@class='artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--full artdeco-button--secondary ember-view scaffold-finite-scroll__load-button']").click()
        time.sleep(3)
        continue
    
    time.sleep(random.randint(1, 7))
    message_zone = driver.find_element_by_xpath("//div[@aria-label='Write a message…']/p")
    locked_div = driver.find_element_by_xpath("//div[@data-placeholder='Write a message…']")
    print(message_zone)
    print(locked_div)
    driver.execute_script("arguments[0].setAttribute('class','t-14 t-black--light t-normal')", locked_div)
    driver.execute_script("arguments[0].innerHTML = 'Bonjour Monsieur'", message_zone)
    time.sleep(random.randint(1, 7))
    submit_message = driver.find_element_by_xpath("//button[@class='msg-form__send-button artdeco-button artdeco-button--1']")
    driver.execute_script("arguments[0].removeAttribute('disabled')", submit_message)
    time.sleep(random.randint(1, 7))
    driver.find_element_by_xpath("//button[@data-control-name='overlay.close_conversation_window']").click()
    time.sleep(random.randint(100, 200))
    i = i + 1
