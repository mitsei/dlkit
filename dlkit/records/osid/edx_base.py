from .base_records import QueryInitRecord
from dlkit.abstract_osid.osid.errors import NotFound


class edXQueryMethods(QueryInitRecord):
    def _get_descendant_ids(self, composition_id, repository_id, mgr=None):
        if mgr is None:
            mgr = self._my_osid_query._get_provider_manager('REPOSITORY')
        cls = mgr.get_composition_lookup_session_for_repository(repository_id)
        cls.use_unsequestered_composition_view()
        descendent_ids = []

        try:
            composition = cls.get_composition(composition_id)
            for child_id in composition.get_child_ids():
                descendent_ids += [child_id]
                descendent_ids += self._get_descendant_ids(child_id, repository_id, mgr)
        except NotFound:
            pass

        return descendent_ids

    def match_edxml(self, edxml):
        """stub"""
        self._my_osid_query._add_match('texts.edxml', str(edxml), True)
