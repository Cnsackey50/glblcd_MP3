from functools import reduce

def join_strings(words):
  """Joins a list of words into a single string using '+'.

  Args:
    words: A list of strings.

  Returns:
    A single string containing all the words joined together with '+'.
  """

  return reduce(lambda item, running_total: item + running_total, words)
words = ["hello ", "world"]
helloworld = join_strings(words) # "hello world"
# total = reduce(lambda item, running_total: item + running_total, words)
print(helloworld)

