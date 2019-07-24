=====================
CrateDB Cloud Console
=====================

The *Cloud Console* is a hosted web administration interface for interacting
with `CrateDB Cloud`_.

.. NOTE::

    For now, CrateDB Cloud is by invitation only.

    `Request a free account`_.

.. rubric:: Table of contents

.. contents::
   :local:

.. _overview-screen:

Overview screen
===============

Here's what the CrateDB Cloud dashboard looks like when it first loads:

.. image:: ../_assets/img/overview.png

You can view the following information about your cluster:

- Overview

  - The name of your `cloud provider`_

  - The `version`_ of CrateDB your cluster is running

  - The number of `CrateDB nodes`_

- Hardware specifications

  - `CPU cores`_

  - `Heap size`_

  - Per-node disk size

  - `HDD`_ type

- Database

  - Default `username`_

- :ref:`Metrics <metrics-screen>` preview (last hour)

- Cluster `logs`_ (last 24 hours)

  - Error count

  - Exception count

Navigation
----------

The navigation is split into two parts:

- The `account menu`_ (along the top)

- The `cluster menu`_ (down the left-hand side)

The account menu and cluster menu are visible on every page.

.. _account-menu:

Account menu
............

Along the top of the screen, from left to right, the account menu has:

+-------------------------+---------------------------------------------------+
| Item                    | Description                                       |
+=========================+===================================================+
| Project select menu     | Displays a list of your current projects and      |
|                         | allows you to switch between them.                |
|                         |                                                   |
|                         | Each project may contain multiple CrateDB         |
|                         | clusters.                                         |
+-------------------------+---------------------------------------------------+
| Cluster overview button | Takes you to the cluster `overview screen`_.      |
+-------------------------+---------------------------------------------------+
| Connect button          | Connect to a rabbitMQ stream.                     |
|                         |                                                   |
|                         | This feature is temporarily non-functional for    |
|                         | most users.                                       |
+-------------------------+---------------------------------------------------+
| Support button          | Displays a list of support options.               |
+-------------------------+---------------------------------------------------+
| Region select menu      | Displays a list of geographic regions and allows  |
|                         | you to switch between them.                       |
|                         |                                                   |
|                         | You can run CrateDB clusters in three regions:    |
|                         |                                                   |
|                         | - `Azure East-US`_                                |
|                         | - `Azure West-Europe`_                            |
|                         | - Bregenz                                         |
|                         |                                                   |
|                         | The *Bregenz* region is managed by Crate.io and   |
|                         | is located in Austria, Europe.                    |
+-------------------------+---------------------------------------------------+

.. _cluster-menu:

Cluster menu
............

Running down the left-hand side, from top to bottom, the cluster menu lets you
view:

- :ref:`Overview <overview-screen>`

- :ref:`Metrics <metrics-screen>`

- :ref:`Logs <logs-screen>`

- :ref:`Snapshots <snapshots-screen>`

- `Admin UI`_ (opens in a new window)

.. _metrics-screen:

Metrics screen
==============

Average response time [s]
-------------------------

.. image:: ../_assets/img/metrics-time.png

This graph displays the average response time for each type of query being
executed on your cluster for the last thirty minutes.

Average CrateDB queries
-----------------------

.. image:: ../_assets/img/metrics-queries.png

This graph displays the average number of each type of query per unit time
being executed on your cluster for the last thirty minutes.

.. _logs-screen:

Logs screen
===========

.. image:: ../_assets/img/logs.png

On this screen, you can view and interact with a paginated table of aggregated
cluster `logs`_. You can filter logs on text, dates, and log level.

.. _snapshots-screen:

Snapshots screen
================

.. image:: ../_assets/img/snapshots.png

On this screen, you can view and interact with a paginated table of cluster
`snapshots`_. You can revert back to a previous cluster state by *restoring* a
snapshot.

.. NOTE::

    For the time being, you must email support if you wish to restore
    a snapshot.

.. _Admin UI: https://crate.io/docs/clients/admin-ui/en/latest/
.. _Azure East-US: https://azure.microsoft.com/en-us/global-infrastructure/regions/
.. _Azure West-Europe: https://azure.microsoft.com/en-us/global-infrastructure/regions/
.. _cloud provider: https://en.wikipedia.org/wiki/Infrastructure_as_a_service
.. _CPU cores: https://en.wikipedia.org/wiki/Multi-core_processor
.. _CrateDB Cloud: https://crate.io/products/cratedb-cloud/
.. _CrateDB nodes: https://crate.io/docs/crate/guide/en/latest/architecture/shared-nothing.html#multi-node-setup-clusters
.. _HDD: https://en.wikipedia.org/wiki/Hard_disk_drive
.. _Heap size: https://crate.io/docs/crate/guide/en/latest/performance/memory.html
.. _logs: https://crate.io/docs/crate/reference/en/latest/config/logging.html
.. _Request a free account: https://crate.io/products/cratedb-cloud/#sign-up
.. _snapshots: https://crate.io/docs/crate/reference/en/latest/admin/snapshots.html
.. _username: https://crate.io/docs/crate/reference/en/latest/admin/user-management.html
.. _version: https://crate.io/docs/crate/reference/en/latest/appendices/release-notes/index.html
