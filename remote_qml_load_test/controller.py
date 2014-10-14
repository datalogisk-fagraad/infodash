

from time import sleep
import Pyro4

def main():
    changer = Pyro4.Proxy("PYRONAME:info.changer")
    files = ["red.qml", "green.qml"]
    for i in range(10000):
        changer.change_qml(files[i%2])
        sleep(0.5)

if __name__ == "__main__":
    main()




