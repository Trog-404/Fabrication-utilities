from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

# from nomad.config import config
# from nomad.datamodel.metainfo.workflow import Workflow
# from nomad.parsing.parser import MatchingParser

# configuration = config.get_plugin_entry_point(
#    'fabrication_facilities.parsers:parser_entry_point'
# )


# class NewParser(MatchingParser):
#    def parse(
#        self,
#        mainfile: str,
#        archive: 'EntryArchive',
#        logger: 'BoundLogger',
#        child_archives: dict[str, 'EntryArchive'] = None,
#    ) -> None:
#        logger.info('NewParser.parse', parameter=configuration.parameter)

#        archive.workflow2 = Workflow(name='test')
