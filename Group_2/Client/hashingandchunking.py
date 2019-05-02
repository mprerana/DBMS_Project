import hashlib
import os

def hashing(filePath):
  with open(filePath, 'rb') as fh:
    m = hashlib.md5()
    size = os.path.getsize(filePath)
    while True:
      data = fh.read(8192)
      if not data:
        break
      m.update(data)
    data = (m.hexdigest(),size)
    return data

def split_equal(file_path, output_dir, no_of_chunks = 10):
  d = dict()
  offset = 0
  filePath = os.path.split(file_path)
  print(filePath)
  file_name = filePath[1]
  print(file_name)
  with open(file_name, 'rb') as mfile:
      content = bytearray(os.path.getsize(file_name))
      chunk_size = int(os.path.getsize(file_name)/(no_of_chunks))+1
      mfile.readinto(content)
      for c, i in enumerate(range(0, len(content), chunk_size)):
        with open(output_dir+file_name[c], 'wb') as f:
          f.write(content[i: i + chunk_size])
          f.close()
          hash_name = hashing(output_dir+file_name[c])[0]
          offset += 1
          d[hash_name] = offset
          if os.path.exists(output_dir+hash_name):
                      os.remove(output_dir+hash_name)
          os.rename(output_dir+file_name[c],output_dir+hash_name)
  return d
