from pylon.core.tools import log, module

from tools import theme


class Module(module.ModuleModel):
    def __init__(self, context, descriptor):
        self.context = context
        self.descriptor = descriptor

    def init(self):
        log.info('Initializing Mock')

        self.descriptor.init_api()


    def deinit(self):  # pylint: disable=R0201
        """ De-init module """
        log.info('De-initializing')
