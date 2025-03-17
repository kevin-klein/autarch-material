import os

for f in os.listdir('.'):
  if not f.endswith('.jpg'):
    continue

  file_without_extension = os.path.splitext(f)[0]
  if not os.path.exists(f"{file_without_extension}.xml"):
    os.remove(f)
