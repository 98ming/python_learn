# 对象存在不一定是True
class Test():
    # pass
    def __len__(self):
        print('len called')
        return 8

    #
    def __bool__(self):
        print('bool called')
        return False


# 如果没有 __bool__ 方法，则会使用 __len__ 方法进行判空操作
test = Test()
print(len(test))
print(bool(test))
