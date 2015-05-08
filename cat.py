from .base import ElasticsearchCommand

DEFAULT_PARAMS = dict(v=1)


class CatClientCommand(ElasticsearchCommand):
    show_result_on_window = True
    syntax = 'Packages/Text/Plain text.tmLanguage'
    result_window_title = ""


class CatAliasesCommand(CatClientCommand):
    result_window_title = "Cat Aliases"

    def run(self):
        self.get_alias(self.on_done)

    def on_done(self, name):
        self.request(self.client.cat.aliases, name=name, params=DEFAULT_PARAMS)


class CatAllocationCommand(CatClientCommand):
    result_window_title = "Cat Allocation"

    def run(self):
        self.get_node_id(self.on_done)

    def on_done(self, node_id):
        self.request(self.esclient.cat.allocation,
                     node_id=node_id, params=dict(v=1))


class CatCountCommand(CatClientCommand):
    result_window_title = "Cat Count"

    def run(self):
        self.get_index(self.on_done)

    def on_done(self, index):
        self.request(self.esclient.cat.count,
                     index=index, params=DEFAULT_PARAMS)


class CatHealthCommand(CatClientCommand):
    result_window_title = "Cat Health"

    def run(self):
        self.request(self.esclient.cat.health, params=DEFAULT_PARAMS)


class CatHelpCommand(CatClientCommand):
    result_window_title = "Cat Help"

    def run(self):
        self.request(self.esclient.cat.help)


class CatIndicesCommand(CatClientCommand):
    result_window_title = "Cat Indices"

    def run(self):
        self.get_index(self.on_done)

    def on_done(self, index):
        self.request(self.esclient.cat.indices,
                     index=index, params=DEFAULT_PARAMS)


class CatMasterCommand(CatClientCommand):
    result_window_title = "Cat Master"

    def run(self):
        self.request(self.esclient.cat.master, params=DEFAULT_PARAMS)


class CatNodesCommand(CatClientCommand):
    result_window_title = "Cat Nodes"

    def run(self):
        self.request(self.esclient.cat.nodes, params=DEFAULT_PARAMS)


class CatRecoveryCommand(CatClientCommand):
    result_window_title = "Cat Recovery"

    def run(self):
        self.get_index(self.on_done)

    def on_done(self, index):
        self.request(self.esclient.cat.recovery,
                     index=index, params=DEFAULT_PARAMS)


class CatShardsCommand(CatClientCommand):
    result_window_title = "Cat Shards"

    def run(self):
        self.get_index(self.on_done)

    def on_done(self, index):
        self.request(self.esclient.cat.shards,
                     index=index, params=DEFAULT_PARAMS)


class CatSegmentsCommand(CatClientCommand):
    result_window_title = "Cat Segments"

    def run(self):
        self.get_index(self.on_done)

    def on_done(self, index):
        self.request(self.esclient.cat.segments,
                     index=index, params=DEFAULT_PARAMS)


class CatPendingTasksCommand(CatClientCommand):
    result_window_title = "Cat Pending Tasks"

    def run(self):
        self.request(self.esclient.cat.pending_tasks, params=DEFAULT_PARAMS)


class CatThreadPoolCommand(CatClientCommand):
    result_window_title = "Cat Thread Pool"

    def run(self):
        self.request(self.esclient.cat.thread_pool, params=DEFAULT_PARAMS)


class CatFielddataCommand(CatClientCommand):
    result_window_title = "Cat Fielddata"

    def run(self):
        self.get_fields(self.on_done)

    def on_done(self, fields):
        self.request(self.esclient.cat.fielddata,
                     fields=fields, params=DEFAULT_PARAMS)


class CatPluginsCommand(CatClientCommand):
    result_window_title = "Cat Plugins"

    def run(self):
        self.request(self.esclient.cat.plugins, params=DEFAULT_PARAMS)