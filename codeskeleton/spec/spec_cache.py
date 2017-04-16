from collections import OrderedDict


class SpecCache(object):
    def __init__(self, *specs):
        self.specs = OrderedDict()
        self.add_specs(*specs)

    def clear(self):
        self.specs = OrderedDict()

    def add_spec(self, spec):
        self.specs[spec.id] = spec

    def add_specs(self, *specs):
        for spec in specs:
            self.add_spec(spec)

    def get_by_id(self, id):
        return self.specs[id]
