# chew_and_cheer | Django Project CRUD using AJAX, DJANGO FORMS, GRAPHQL and DJANGO REST/GRAPHQL APIs

This is a simple django CRUD project

## Project Features

1. **Account Functionality:** Complete account management.
2. **PostgreSql Integration:** Utilized as a database.
3. **AWS S3/MinIO Integration:** For file storage.
4. **Redis Integration:** Utilized for caching and message pub/sub.
5. **MailJet Integration:** Used for email services.
6. **Dockerized Project:** Fully containerized for easy deployment.
7. **Kubernetes-native** Kubernetes support also available.
8. **CI/CD Pipeline:** Continuous integration and deployment included using Jenkins.
9. **Sentry Integrated:** Logging and Debugging Made Easy.

## CURD Functionalities

CRUD Operations

### Django Forms

	-	Create Operation: Users can create new entries using Django forms. The form data is validated on the server side, and upon successful validation, the data is saved to the PostgreSQL database.
	-	Read Operation: The project displays existing entries using Django views and templates. Users can view a list of entries or details of a specific entry.
	-	Update Operation: Users can update existing entries through forms. The current data is pre-populated in the form, allowing users to make changes and save them.
	-	Delete Operation: Users can delete entries. Upon confirmation, the entry is removed from the database.

### AJAX Integration

	-	Asynchronous Form Submission: Forms are submitted using AJAX to provide a seamless user experience. The page does not need to reload, and users receive immediate feedback.
	-	Dynamic Content Loading: Data is fetched asynchronously to update parts of the web page without a full reload, enhancing responsiveness.

### GraphQL Integration

	-	Querying Data: Users can query entries using GraphQL queries. This allows fetching specific data fields, reducing the amount of data transferred.
	-	Mutations: Users can create, update, and delete entries using GraphQL mutations, providing a flexible and efficient way to manage data.

## Django REST Framework (DRF) API

The project includes an API app that demonstrates different views available in Django REST Framework:

	-  Function-Based Views (FBVs)
	-	FBV with @api_view Decorator
	-	Basic Class-Based Views (CBVs)
	-	Class-Based Views using APIView
	-	Generic API Views with Mixins
	-	ViewSets
	-	ViewSets with Authentication and Permissions
	-	ListAPIView with Filters and Pagination
	-	Nested Serializers and Hyperlinked Serializers
   -  Have Open Schema View
   -  Have Docs View 