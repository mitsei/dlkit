from dlkit.primordium.id.primitives import Id

from ...osid.base_records import ObjectInitRecord


class edXProviderIdMixin(ObjectInitRecord):
    def _update_object_map(self, map):
        # check if the repository has an enclosed asset with this
        # itemId. If so, insert the providerId into the object map
        super(edXProviderIdMixin, self)._update_object_map(map)
