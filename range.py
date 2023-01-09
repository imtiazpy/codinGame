# not working 

def get_range(s):
  parts = s.split(" ")
  op = parts[1]
  num = int(parts[2])
  if op == ">":
    return f"{num+1} <= x"
  elif op == "<":
    return f"x <= {num-1}"
  else:
    return f"{num} <= x <= {num}"


def extract_range(lines):
  ranges = []
  for line in lines:
    ranges.append(get_range(line))
  return " and ".join(ranges)

def main():
  n = int(input())
  lines = []
  for _ in range(n):
    line = input()
    lines.append(line)
  print(extract_range(lines))

main()
