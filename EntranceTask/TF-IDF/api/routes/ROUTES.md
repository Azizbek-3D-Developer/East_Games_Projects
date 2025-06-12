# This file contains all available routes for the project
In addition all available routes are groupped by the logic and where they are used

## Routes lists
### Can be used without Login
- **/status** - endpoint for health checks.
- **/version** - endpoint to return current version info.
- **/** - endpoint to landing page
- **/register** - endpoint to registration page
- **/?register_status=success** - endpoint to landing page with success result of registration
- **/login** - endpoint to login page
- **/test-500** - error 500 page Internal Server Error
- **/whatever** - error 404 page Not Found

### Can be used only after being Logged In
- **/metrics** - endpoint to track performance and processing stats.
- **/dashboard** - endpoint for user dashboard
- **/dashboard/documents** - endpoint to list of documents
- **/dashboard/documents/create** - endpoint for creating new document
- **/dashboard/documents/{{document_id}}/edit** - endpoint for editing document
- **/dashboard/documents/{{document_id}}** - endpoint for document details
- **/dashboard/documents/{{document_id}}/huffman** - endpoint for viewing huffman encoding
- **/dsahboard/documents/{{document_id}}/delete** - endpoint for deleting document
- **/documents/details/{{document_id}}/create** - endpoint for creating document-collection connection from documents page
- **/collections/details/{{collection_id}}/{{document_id}}/delete** - endpoint for removing document-collection connection
- **/dashboard/collections** - enpoint to list of collections
- **/dashboard/collections/create** - endpoint to create new collection
- **/dashboard/collections/{{collection_id}}** - endpoint to details of the collection
- **/dashboard/collections/{{collection_id}}/edit** - endpoint to update the collection
- **/dashboard/collections/{{collection_id}}/delete** - endpoint for deleting collection
- **/collections/details/{{collection_id}}/create** -endpoint for creating document-collection connection from collections page
- **/dashboard/collections/{{collection_id}}/statistics** - endpoint to see the statistics of the collection containing documents
- **/setting** - endpoint to user settings page
- **//{{user_id}}** - endpoint for updating user info
- **/setting/{{user_id}}/delete** - deleting user
