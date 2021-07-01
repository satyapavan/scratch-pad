import urllib.request
import sys
import time

counter = 1

print(f"Arguments count: {len(sys.argv)}")

if len(sys.argv) > 1:
    counter = int(sys.argv[1])

while counter > 0:
    print(f"Processing {counter}")
    with urllib.request.urlopen('http://source.unsplash.com/random/1600x900') as response:
        out_file = open('%04d'%(counter) + '.jpg', 'wb')
        out_file.write(response.read())
        out_file.close()
        counter = counter - 1
        print("Sleeping....")
        time.sleep(10)

