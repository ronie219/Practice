# array = '{([])}]'
# track = {'{': '}', '(': ')', '[': ']'}
# stack = []
# for ele in array:
#     if ele in track.keys():
#         stack.append(ele)
#     else:
#         if len(stack) == 0 and track[stack.pop()] != ele:
#             print(False)
#             break
# if len(stack) == 0:
#     print(True)
# else:
#     print(False)
#
#
#
#


import uuid
import base64


def generate():
    # base64.urlsafe_b64decode(uuid.uuid1().bytes).encode("base64").rstrip()[:25]
    print()

generate()