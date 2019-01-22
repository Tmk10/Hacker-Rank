from collections import OrderedDict

word_dict = OrderedDict()
for _ in range(int(input())):
    temp_word = input()
    word_dict[temp_word] = word_dict.setdefault(temp_word, 0) + 1

print(len(word_dict))
print(*word_dict.values())




