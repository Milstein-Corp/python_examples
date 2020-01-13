import json


fb_page_info = {
        "page_name": "Python Bootcamp Cambodia",
        "username": "python.bootcamp",
        "social": {
            "likes": 12345,
            "followers": 15000
        }
}

print(fb_page_info)
# {'page_name': 'Python Bootcamp Cambodia', 'username': 'python.bootcamp', 'social': {'likes': 12345, 'followers': 15000}}

print(json.dumps(fb_page_info, indent=4))
# {
#     "page_name": "Python Bootcamp Cambodia",
#     "username": "python.bootcamp",
#     "social": {
#         "likes": 12345,
#         "followers": 15000
#     }
# }

print(json.dumps(fb_page_info, indent=4, sort_keys=True))
# # will print:
# {
#     "page_name": "Python Bootcamp Cambodia",
#     "social": {
#         "followers": 15000,
#         "likes": 12345
#     },
#     "username": "python.bootcamp"
# }
