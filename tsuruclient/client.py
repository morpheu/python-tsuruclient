from tsuruclient import apps, nodes, templates, pools, machines


class Client(object):
    def __init__(self, target, token):
        self.apps = apps.Manager(target, token)
        self.nodes = nodes.Manager(target, token)
        self.templates = templates.Manager(target, token)
        self.pools = pools.Manager(target, token)
        self.machines = machines.Manager(target, token)
