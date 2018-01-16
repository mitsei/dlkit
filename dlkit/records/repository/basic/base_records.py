from dlkit.json_.utilities import JSONClientValidated
from dlkit.json_.repository.objects import Asset, AssetList

from dlkit.primordium.id.primitives import Id
from dlkit.abstract_osid.osid.errors import IllegalState

from bson.objectid import ObjectId

from ...osid.base_records import ProvenanceRecord


class ProvenanceAssetRecord(ProvenanceRecord):
    def get_provenance_parent(self):
        if self.has_provenance():
            collection = JSONClientValidated('repository',
                                             collection='Asset',
                                             runtime=self.my_osid_object._runtime)
            result = collection.find_one({'_id': ObjectId(Id(self.get_provenance_id()).get_identifier())})
            return Asset(osid_object_map=result,
                         runtime=self.my_osid_object._runtime,
                         proxy=self.my_osid_object._proxy)
        raise IllegalState("Asset has no provenance parent.")

    def has_provenance_children(self):
        collection = JSONClientValidated('repository',
                                         collection='Asset',
                                         runtime=self.my_osid_object._runtime)
        if collection.find({'provenanceId': self.my_osid_object.object_map['id']}).count() > 0:
            return True
        else:
            return False

    def get_provenance_children(self):
        if self.has_provenance_children():
            collection = JSONClientValidated('repository',
                                             collection='Asset',
                                             runtime=self.my_osid_object._runtime)
            result = collection.find({'provenanceId': self.my_osid_object.object_map['id']})
            return AssetList(result,
                             runtime=self.my_osid_object._runtime,
                             proxy=self.my_osid_object._proxy)
        raise IllegalState('No provenance children.')

    provenance_children = property(fget=get_provenance_children)
    provenance_parent = property(fget=get_provenance_parent)


class ProvenanceCompositionRecord(ProvenanceRecord):
    def get_provenance_parent(self):
        if self.has_provenance():
            collection = JSONClientValidated('repository',
                                             collection='Composition',
                                             runtime=self.my_osid_object._runtime)
            result = collection.find_one({'_id': ObjectId(Id(self.get_provenance_id()).get_identifier())})
            return Asset(osid_object_map=result,
                         runtime=self.my_osid_object._runtime,
                         proxy=self.my_osid_object._proxy)
        raise IllegalState("Composition has no provenance parent.")

    def has_provenance_children(self):
        collection = JSONClientValidated('repository',
                                         collection='Composition',
                                         runtime=self.my_osid_object._runtime)
        if collection.find({'provenanceId': self.my_osid_object.object_map['id']}).count() > 0:
            return True
        else:
            return False

    def get_provenance_children(self):
        if self.has_provenance_children():
            collection = JSONClientValidated('repository',
                                             collection='Composition',
                                             runtime=self.my_osid_object._runtime)
            result = collection.find({'provenanceId': self.my_osid_object.object_map['id']})
            return AssetList(result,
                             runtime=self.my_osid_object._runtime,
                             proxy=self.my_osid_object._proxy)
        raise IllegalState('No provenance children.')

    provenance_children = property(fget=get_provenance_children)
    provenance_parent = property(fget=get_provenance_parent)
