import sys, inspect, os
from DataStream import DataStream
def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)


def find_subs():
    app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
    print(os.listdir("packages"))
    for i in os.listdir("packages"):
        print(os.path.join(app_dir,'packages', i))
        with os.system(os.path.join(app_dir, 'packages', i)):
            for name, obj in inspect.getmembers(sys.modules[__name__]):
                if inspect.isclass(obj):
                    print(obj)

def test():
    clsmembers = inspect.getmembers(sys.modules['packages'], inspect.isclass)
    for name, cls in clsmembers:
        print(cls)

    print({cls().id: cls for name, cls in inspect.getmembers(sys.modules['packages'], inspect.isclass)})


#find_subs()
#print(globals())
#test()

class A:
    def api(self):
        print("A")

class B(A):
    def api(self):
        print('B')

class C(B):
    def api(self):
        print("C")
    def testA(self):
        super(A, self).api()
    def testB(self):
        super(B, self).api()

    def testC(self):
        super(C,self).api()

#c = C()
#c.testA()
#c.testB()
#c.testC()


def testingDataStream():
    stream = DataStream()
    stream.write_uint16(1)
    stream.write_string_unicode(b"admin")
    stream.write_string_unicode(b"123")
    resp = stream.send()

    newData = DataStream(resp)
    print(newData.read_uint16())
    print(newData.read_string_unicode())
    print(newData.read_string_unicode())

testingDataStream()
import struct
import ctypes

def scr_test():
    res = b'admin'
    value = struct.pack('>5s', res)
    print(value)