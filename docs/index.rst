Sphinx-Needs Demo
=================

.. req:: User login must be secure
   :id: REQ_001
   :status: open
   :tags: security, login
   :author: Ganesh

   Passwords must be hashed using bcrypt.

.. spec:: Password hashing implementation
   :id: SPEC_001
   :status: in_progress
   :links: REQ_001

   Backend will implement bcrypt with a salt of length 16.

.. test:: Verify bcrypt hashing
   :id: TEST_001
   :status: not_tested
   :links: SPEC_001

   Ensure passwords are bcrypt-hashed and salted.

Open Requirements Table
----------------------

.. needtable::
   :status: open
   :columns: id;title;status;tags
