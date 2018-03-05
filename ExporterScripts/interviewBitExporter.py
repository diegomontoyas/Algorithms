import time
from selenium import webdriver

USER_PATH = "user"

driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get("https://www.interviewbit.com/")

driver.add_cookie({
    'domain': 'www.interviewbit.com',
    'name': 'XSRF-TOKEN',
    'value': 'token',
})

driver.add_cookie({
    'domain': 'interviewbit.com',
    'name': 'remember_user_token',
    'value': 'token',
})

solution_links = []

num_pages = 18
for page in range(num_pages):
    page_link = "https://www.interviewbit.com/profile/"+USER_PATH+"/solved-problems/?page=" + str(page+1)
    driver.get(page_link)
    time.sleep(2)

    page_solution_links = [elem.get_attribute("href") for elem in driver.find_elements_by_tag_name('a')]
    page_solution_links = filter(lambda elem: elem is not None, page_solution_links)
    page_solution_links = filter(lambda elem: elem.startswith("https://www.interviewbit.com/courses/programming/"),
                                 page_solution_links)

    solution_links += list(page_solution_links)

for solution_link in solution_links:
    driver.get(solution_link)
    time.sleep(2)

    text_containers = driver.find_elements_by_class_name("ace_text-layer")
    if len(text_containers) == 0:
        continue

    text_container = text_containers[1]

    line_elements = text_container.find_elements_by_class_name("ace_line")
    lines = [el.text for el in line_elements]
    solution_text = "\n".join(lines)

    extension = "py" if "def " in solution_text else "java"
    comment_prefix = "// " if extension == "java" else "# "

    with open("./export/" + solution_link.split("/")[-2] + "." + extension, "w") as text_file:
        print(comment_prefix + solution_link + "\n" + comment_prefix + "\n\n" + solution_text, file=text_file)
