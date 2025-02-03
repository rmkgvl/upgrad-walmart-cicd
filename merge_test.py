merge_message = "this file is created to test out merge with main"

def print_message():
    print(merge_message)

print_message()

merge_message_2 = "this message is from main branch, this is to test out merge conflict resolving"
print(merge_message_2)

merge_message_2 = "this message is in the feature2 branch, we will test out how merge conflit resolves"
print(merge_message_2)