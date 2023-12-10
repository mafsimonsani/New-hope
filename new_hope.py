# WC '15 Contest 2 J1 - A New Hope

repeat = int(input())

# Given N, produce the correct sentence.

sentence = 'A long time ago in a galaxy ' + ('far, ' * (repeat-1)) + 'far away...'

print(sentence)