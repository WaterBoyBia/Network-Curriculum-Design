import os
from catch_html import get_html
from dispose import html_to_csv
from dispose import add_title
from delete_html import remove

# user_id = "ruo1996"
#
# add_title()
# get_html(user_id)
# html_to_csv()
# remove()

for user_id in range(43761473, 43761483):
    get_html(user_id)
    if os.path.exists('1.html'):
        html_to_csv()
        remove()

