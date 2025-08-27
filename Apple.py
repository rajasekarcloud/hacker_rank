import time
def call_with_retry(fn):
    retry =1
    time.sleep(1)
    print(f'sleep 1sec, count {retry}, {fn()}')
    retry += 1
    for i in range(2,12,2):
        if retry <=5:
            time.sleep(i)
            print(f'sleep {i}sec, count {retry}, {fn()}')
            retry +=1
        else:
            break
def fn():
    try:
        return 'welcome'
    except:
        return 'Failed to welcome'

call_with_retry(fn)