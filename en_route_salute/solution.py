def answer(s):
              right = 0
              result = 0
              for word in s:
                    if word == '>':
                       right = right + 1
                    elif word == '<':
                       result = result + (right*2)
              return result

print answer('<>>----<<<')
