from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import json
import queue
import threading

import schedule
import time
from selenium.webdriver.common.by import By

def read_user_data():
    '''return a dict of user'''
    with open('user.json', 'r') as file:
        user_data = json.load(file)
    return user_data

def read_course_data_list():

    with open('slots.json', 'r') as file:
        course_data_list = json.load(file)
    return course_data_list


def process_item(course_data_queue,user_data):
    while True:
        course_data = course_data_queue.get()
        course_booking(course_data,user_data)
        print(f"Processing item: {course_data}")
        time.sleep(2)
        print(f"Finished processing item: {course_data}")

        # Mark the task as done in the queue
        course_data_queue.task_done()

def course_booking(course_data,user_data):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Open the website
    # driver.get('https://buchung.hsz.rwth-aachen.de/angebote/Wintersemester/_Flag-Football_Level_1.html')
    driver.get(course_data['url'])

    # find the buchen button
    # target_tr = driver.find_element(By.CSS_SELECTOR, 'tr#bs_trFB8302A782C2')
    target_tr = driver.find_element(By.CSS_SELECTOR, f'tr#{course_data["tr_id"]}')


    # Check if the target <tr> element is found
    if target_tr:
        # Find the "buchen" button within the target <tr> element
        buchen_button = target_tr.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="buchen"]')

        # Check if the "buchen" button is found
        if buchen_button:
            # Click the "buchen" button
            buchen_button.click()
            print("Button 'buchen' clicked.")
        else:
            print("Button 'buchen' not found in the target element.")
    else:
        print("Target element not found.")


    # knowing the kursid before hand
    # redirect_button = driver.find_element_by_name('BS_Kursid_198729')

    buchen_button.click()
    # new_page_url = driver.current_url

    # print('Redirected Page URL:', new_page_url)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    new_page_title = driver.title
    print("Title of the new page:", new_page_title)


    # fill user info
    user_sex = user_data["sex"]
    sex_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(('xpath', f'//input[@type="radio" and @name="sex" and @value="{user_sex}"]'))
    )
    print("sex found")
    sex_button.click()
    print("sex clicked")

    vorname = driver.find_element_by_name('vorname')
    vorname.send_keys(user_data["vorname"])

    name = driver.find_element_by_name('name')
    name.send_keys(user_data["name"])

    strasse = driver.find_element_by_name('strasse')
    strasse.send_keys(user_data["strasse"])

    ort = driver.find_element_by_name('ort')
    ort.send_keys(user_data["ort"])

    status_select_element = Select(driver.find_element_by_id('BS_F1600'))
    # Select an option by value
    status_select_element.select_by_value(user_data["status"])

    matnr = driver.find_element_by_name('matnr')
    matnr.send_keys(user_data["matnr"])

    email = driver.find_element_by_name('email')
    email.send_keys(user_data["email"])

    telefon = driver.find_element_by_name('telefon')
    telefon.send_keys(user_data["telefon"])

    iban = driver.find_element_by_name('iban')
    if iban:
        iban.send_keys(user_data["iban"])

    checkbox = driver.find_element_by_name('tnbed')
    if not checkbox.is_selected():
        checkbox.click()

    weiter_buchung_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(('id', 'bs_submit'))
    )
    # weiter_buchung = driver.find_element_by_id('bs_submit')

    weiter_buchung_button.click()
    time.sleep(10)

    new_page_url = driver.current_url
    print("URL of the new page:", new_page_url)
    driver.get(new_page_url)
    time.sleep(20)

def big_one():
    user_data = read_user_data()
    course_data_list = read_course_data_list()

    course_data_queue = queue.Queue()
    for course_data in course_data_list:
        print(course_data)

        course_data_queue.put(course_data)

    num_threads = 3
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=process_item, args=(course_data_queue, user_data))
        thread.start()
        threads.append(thread)
    course_data_queue.join()
    for thread in threads:
        thread.join()

    print("all items are processed")

if __name__ == '__main__':
    # big_one()
    schedule.every().day.at("16:30").do(big_one)
    while True:
        schedule.run_pending()
        time.sleep(1)