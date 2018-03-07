# TODO

* [ ] Firmglobal.Confirmit

Most complex object-structures that can be used as parameters or return-values by web-services are grouped into Firmglobal.Comfirmit.Reporting, Firmglobal.Confirmit.SurveyData, Firmglobal.Confirmit.Authoring and so on. However, some object-structures are common to several of these and are gathered in this namespace.

* [ ] Firmglobal.Confirmit.Authoring

* [ ] Firmglobal.Confirmit.Authoring.Capi

Capi is used for integrating with external systems such as field management systems.

* [ ] Firmglobal.Confirmit.Authoring.ProjectManagement

ProjectManagement is used when reading a projectlist.

* [ ] Firmglobal.Confirmit.Authoring.QuotaWebServices

* [ ] Firmglobal.Confirmit.Authoring.Schema.PredefinedScripts

* [ ] Firmglobal.Confirmit.Authoring.Schema.Telephony

* [ ] Firmglobal.Confirmit.Authoring.Schema_17_5

Schema is used when reading, manipulating and updating the schema of a survey. The schema consists of different questions and other nodes from the routing-tree, predefined lists, quotas and encapsulating objects. When retrieving or updating schema-information the encapsulating object that keeps track of all the content is always a SurveySchema-object.

* [ ] Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport

* [ ] Firmglobal.Confirmit.Authoring.Templates

* [ ] Firmglobal.Confirmit.Emailing

This namespace contains classes that are used as parameters to decide the format of a mail that is to be sent.

* [ ] Firmglobal.Confirmit.ErrorDelegates

The classes in this namespace supports detailed errormessages returned by various webservices if case of problems updating data to the database.

* [ ] Firmglobal.Confirmit.Panel

* [ ] Firmglobal.Confirmit.Sampling.DataTransfer

* [ ] Firmglobal.Confirmit.Sampling.DataTransfer.Report

* [ ] Firmglobal.Confirmit.SurveyData.DataTransfer

DataTransfer is used to limit what loop-levels, confirmit-questions or specific database-fields to retrieve or update. There is also support for limiting what rows to retrieve.

* [ ] Firmglobal.Confirmit.SurveyData.DataTransfer.ChangedData

* [ ] Firmglobal.Confirmit.SurveyData.InterviewProgress

* [ ] Firmglobal.Confirmit.SurveyData.Querying

The Querying namespace contains objects to specify a database-independant definition of a database query. This namespace is often used by other namespaces (for instance Reporting-namespaces and the Where-clause of the DataTransfer-namespace).

* [ ] Firmglobal.Confirmit.SurveyData.TripleS

TripleS is a dataformat used by a number of actors within market research. Confirmit web-services only has limited support for this format as not all variable-types are supported. Please note that metadata reflecting precodes of Confirmit has been added. Also note that support for grouping questions according to how it is done in confirmit is NOT supported. That means that if a confirmit project is exported and imported the new survey most probably is not organized as the original survey, but it will contain the same questions. For instance GRID-questions have been transformed into a set of single-questions.

* [x] Firmglobal.Confirmit.WebServices.V180
