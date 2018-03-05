import os

import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="./geckodriver")

driver.get("https://leetcode.com/")

driver.add_cookie({
    'domain': 'leetcode.com',
    'name': 'leetcode.sid',
    'value': 'sid',
    "secure" : True
})

driver.add_cookie({
    'domain': 'leetcode.com',
    'name': 'LEETCODE_SESSION',
    'value': 'token',
    "secure" : True
})

driver.get("https://leetcode.com/problemset/all/?status=Solved")
time.sleep(5)

solution_links = [elem.get_attribute("href") for elem in driver.find_elements_by_tag_name('a')]
solution_links = filter(lambda elem: elem.startswith("https://leetcode.com/problems/"), solution_links)
solution_links = list(solution_links)
del solution_links[0]

for solution_link in solution_links:
    driver.get(solution_link + "/submissions")
    time.sleep(5)
    submissions = driver.find_elements_by_link_text("Accepted")

    if submissions:
        last_submission_link = submissions[0].get_attribute("href")
        driver.get(last_submission_link)

        lines = [e.text for e in
                 driver.find_element_by_class_name("ace_text-layer").find_elements_by_class_name("ace_line_group")]
        solution_text = "\n".join(lines)
        extension = "py" if "def " in solution_text else "java"
        comment_prefix = "// " if extension == "java" else "# "
        run_time = driver.find_element_by_id("result_runtime").text

        with open("./export/" + solution_link.split("/")[-1] + "." + extension, "w") as text_file:
            print(comment_prefix + solution_link + "\n" + comment_prefix + run_time + "\n\n" + solution_text, file=text_file)
