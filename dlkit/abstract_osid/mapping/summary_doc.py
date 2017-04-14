# -*- coding: utf-8 -*-
"""Mapping Open Service Interface Definitions
mapping version 3.0.0

The Mapping OSID provides a means for managing inventories of places and
performing a variety of mapping operations.

Locations

One aspect of the Mapping OSID provides references to location places
used in other OSIDs. A ``Location`` may include a spatial coordinate or
defined boundary described in a ``SpatialUnit``. Additional sessions
provide a means to easily look up locations by ``Coordinate`` or
arbitrary ``SpatialUnit`` as well as to traverse locations through
lookups of adjacent ``Locations``.

``Locations`` may be structured in hierarchies to convey hierarchical
relationships. A room may be located inside a building, within a city
within a state.

Primitives

The data interfaces for ``Coordinates`` and ``SpatialUnits`` are defined
through their respective ``Types`` to allow for any kind of coordinate
or spatial system. A definition for distance resolution is also provided
to capture an extremely wide array of unit values. ``Distance,``
``Coordinate,``  ``Heading,`` and ``SpatialUnit`` appear to the OSID as
complex primitive interfaces which are constructed by the consumer in
order to fulfill the interface contracts. It is required that the
consumer and provider agree on the coordinate domain and spatial unit
types through testing of the ``Type`` support.

Resource Tracking

``Resources`` may be tracked spatially. Sessions are available to query
and place ``Resources`` at specific ``Locations`` and ``Coordinates,``
and receive notifications to changes in their locations.

Map Cataloging

``Locations`` may be organuzed in hierarchical ``Maps`` that offer a
means of federation or layering of map data.

Sub Packages

The Mapping OSID includes a Mapping Route OSID for creating and
navigating Routes, a Mapping Path OSID for querying and designing
physical ``Paths`` and a Mapping Batch OSID for managing locations in
bulk.

"""
