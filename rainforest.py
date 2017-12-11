nums = [1,2,3,5,8,13,99, 1,6]


def rain():
  num = 0
  for index, n in enumerate(nums):
    if n != 99:
      num += n
      print(num / (index + 1))
    else:
      return "its over"
rain()
