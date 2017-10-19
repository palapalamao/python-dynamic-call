import config


class LazyImport(object):
    """
    动态导入模块
    """

    def __init__(self, module_name, class_name, func_name):
        """
        :param module_name:
        :param class_name:
        :param func_name:
        :return:   form module_name call func
        """
        self.module_name = module_name
        self.module_class = class_name
        self.module = None

        self.module = __import__(self.module_name, fromlist=[self.module_class])
        c = getattr(self.module, self.module_class)
        obj = c()
        mtd = getattr(obj, func_name)
        mtd()


def main():
    """main"""
    LazyImport(config.current_branch, "testclass", "report1")
    LazyImport(config.current_branch, "testclass", "report2")
    print("hi")
if __name__ == "__main__":
    main()

