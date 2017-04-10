# Introduction

This documentation for the Digital Learning Toolkit (DLKit), like the toolkit itself, is still under development. It currently covers only a small handful of the 180 service packages and over 10,000 educational service APIs that have been defined by MIT’s Office of Digital Learning and its collaborators to date.

The DLKit codebase is generated from the Open Service Interface Definitions (OSIDs), an extensive and growing suite of interface contract specifications that describe the integration points among the core services and components that make up modern educational systems.

Note that this documentation is intended for API consumers. However, at the heart of DLKit is an integration stack that is even more closely aligned with the OSID specifications. This has been designed to allow third parties to extend the library with alternative or additional implementations of any of the defined services for the purposes of service integration, technology migration, service adaptation, etc. Documentation written for service implementers and system integrators, including implementation notes and compliance information, will be provided elsewhere.

The complete OSID specification can be found at [https://osid.org/specifications](https://osid.org/specifications).

Currently, DLKit works with Python 2.6 and 2.7.

If you are interested in learning more about the DLKit Python libraries documented here, please contact dlkit-info@mit.edu

# Running DLKit

## Tutorial

This Jupyter notebook is useful for learning about how to use `dlkit`.

https://github.com/mitsei/dlkit-tutorial

## Runtime Config

To use `dlkit`, you need to include a runtime config in an `app_configs`
directory.

```
app_configs
  |-configs.py
  |-registry.py
your_app
  |-app.py
```

Example `app_config` files are included in this repo and used for testing.

# Building This Library
Note that this library is mostly generated by the `dlkit_builders` repo,
which can be found [here](https://github.com/mitsei/dlkit_builders).

Hand-written modules are:

  - primordium
  - aws_adapter
  - filesystem_adapter
  - handcar

