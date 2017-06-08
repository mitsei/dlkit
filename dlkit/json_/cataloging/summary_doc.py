# -*- coding: utf-8 -*-
"""Cataloging Open Service Interface Definitions
cataloging version 3.0.0

The Cataloging OSID is an auxiliary service and provides a means for
organizing ``OsidObjects`` into ``OsidCatalogs``. An ``OsidObject`` is
represented by an OSID ``Id``.

``Catalogs`` can be organized into hierarchies for federation. A
``Catalog`` that is a parent of another catalog includes the ``Ids`` of
its children.

The Cataloging OSID provides the core definition for the cataloging
functions used throughout the OSIDs and aids in the adaptability of
cataloging structures.

Sub Packages

The Cataloging OSID includes a rules package for managing the behavior
of a ``Catalog`` in a federated hierarchy.

"""
