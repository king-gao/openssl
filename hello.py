from datetime import datetime
now=datetime.now()
print(now)

from datetime import datetime
time=datetime(2020,2,29,23)
print(time)

from datetime import datetime
t=14556294.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

from datetime import datetime
st=datetime.strptime('2011-2-5 15:20:18','%Y-%m-%d %H:%M:%S')
print(st)

from datetime import datetime
now=datetime.now()
print(now.strftime('%b,%d,%H:%M'))

from collections import defaultdict
dd=defaultdict(lambda:'N/A')
dd['hey1']='abc'
print(dd['key'])

import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
