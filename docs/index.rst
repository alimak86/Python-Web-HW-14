.. Contact Book documentation master file, created by
   sphinx-quickstart on Mon Aug  7 23:35:55 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Contact Book's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Contact Book main
========================================
.. automodule:: main
  :members:
  :undoc-members:
  :show-inheritance:


Contact Book database
========================================
.. autoclass:: src.database.database::Connect_db
   :members:

Contact Book model
========================================
.. automodule:: src.database.models
   :members:

Contact Book repository contacts 
========================================
.. automodule:: src.repository.contacts
  :members:
  :undoc-members:
  :show-inheritance:

Contact Book repository users 
========================================
.. automodule:: src.repository.users
  :members:
  :undoc-members:
  :show-inheritance:

Contact Book routes auth
========================================
.. autoclass:: src.routes.auth::Login
  :members:

Contact Book routes contacts
========================================
.. automodule:: src.routes.contacts
  :members:
  :undoc-members:
  :show-inheritance:

Contact Book routes users
========================================
.. automodule:: src.routes.users
  :members:

Contact Book services auth
========================================
.. automodule:: src.services.auth
  :members:

Contact Book services email
========================================
.. automodule:: src.services.email
  :members:
  :undoc-members:
  :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
