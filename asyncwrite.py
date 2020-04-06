import threading
import time
class acyncwrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out,"a")
        f.write(self.text+'\n')
        f.close();
        time.sleep(10)
        print("finish background "+self.out)

def Main():
    message = input("enter String: ")
    backgroud = acyncwrite(message, "out.txt")
    backgroud.start()
    print("beress")
    backgroud.join()
    print("wait")

if __name__ == '__main__':
    Main()