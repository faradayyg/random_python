from abc import ABCMeta


class BaseFactoryMeta(type):
    _builders = {}

    def __new__(mcs, class_name, bases, attrs):
        init_class = super().__new__(mcs, class_name, bases, attrs)
        builder_key = getattr(init_class, "n", None)
        if builder_key:
            mcs._builders[builder_key] = init_class
        print(mcs._builders)
        return init_class

    @classmethod
    def create(mcs, key, **kwargs):
        builder = mcs._builders.get(key)
        if not builder:
            raise ValueError(f"{key} does not exist.")
        return builder(**kwargs)


class FactoryProvider(metaclass=BaseFactoryMeta):
    key = None

    def get_id(mcs):
        return mcs.key

    @classmethod
    def get(mcs, i):
        return mcs.create(i)


class ChildFactory1(FactoryProvider):
    n = "childOne"
    desc = "First Child Factory"


class ChildFactory2(FactoryProvider):
    n = "childTwo"
    desc = "Second Child Factory"


gs = (
    "childOne",
    "childTwo",
)

for i in gs:
    m = FactoryProvider()
    n = m.get(i)
    print(n.desc)


class Parent:
    def a(self):
        print(self.b())

    @staticmethod
    def b():
        return "Gold"


class Child(Parent):
    def a(self):
        super().a()

    @staticmethod
    def b():
        super(Child, Child).b()
        return "yaat"

