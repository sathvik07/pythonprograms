#!/usr/bin/env python3

import yaml

def parseresourceyaml():
  with open('variablelist.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
    a = data["raincoat"]
    print(" the variable a value is",a)
  f.close()
  return data


if __name__ == "__main__":
    print(" before calling my function")
    ab = parseresourceyaml()
    print("printing after calling the function",ab)