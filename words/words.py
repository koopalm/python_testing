def reverse_words(string):
    x_list = list(string.split(" "))
    final_list = []
    for word in x_list:
        if len(word)>=5:
            word = word[::-1]
        if len(word)==2:
            word = word.upper()
            final_list.append(word)
        else:
            final_list.append(word)
    final_word = " ".join(final_list)
    return final_word

if __name__ == "__main__":
    string = "Pluto is a dog"
    print(reverse_words(string))



# def reverse_words(string):
#     x_list = list(string.split(" "))
#     final_list = []
#     for word in x_list:
#         if len(word)>=5:
#             word = word[::-1]
#             final_list.append(word)
#         else:
#             final_list.append(word)
#     last_list = []
#     for word in final_list:
#         if len(word)==2:
#             word = word.upper()
#             last_list.append(word)
#         else:
#             last_list.append(word)
#     final_word = " ".join(last_list)
#     return final_word

# if __name__ == "__main__":
#     string = "Pluto is a dog"
#     print(reverse_words(string))