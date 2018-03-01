import sys, os
sys.path.append(os.path.abspath('../../'))

from core.ConfirmitCore import ConfirmitCore
from .LogOn import LogOn

class DatabaseDesigner(ConfirmitCore):
  """
  The Database Designer web service is used . It enables an interface to
    Get, delete and update content for a table
    Synchronize content from design mode to runtime mode.
  """

  def __init__(self):
    self.logon = LogOn()
    self.key = self.logon.LogOnUser(ConfirmitCore.USERNAME, ConfirmitCore.PASSWORD)
    self.wsdl = ConfirmitCore.WSDL['databasedesigner']
  
  def CreateDbRelation(self, schemaId=None, tableId=None, newRelation=None):
    """Method for adding a db relation to a specified table
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema to which the table we will add a relation to belongs
      tableId
        Type: System.Int32
        The id of the table we want to add a relation to
      newRelation
        Type: Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport.WSDbRelation
        The data carrier object holding the definition of the relation we want to create
    Return Value
      Type: Int32
      The id of the new relation
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')
    if tableId is None:
      raise Exception('Please specify tableId')
    if newRelation is None:
      raise Exception('Please specify newRelation')

    return self.GetClient().CreateDbRelation(self.key, schemaId, tableId, newRelation)

  def CreateHierarchy(self, schemaId=None, newHierarchy=None):
    """Method for creating a new hierarchy
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema in which the hierarchy should be created
      newHierarchy
        Type: Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport.WSHierarchy
        The data carrier object holding the definition of the hierarchy to be created
    Return Value
      Type: Int32
      The id of the new hierarchy
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')
    if newHierarchy is None:
      raise Exception('Please specify newHierarchy')

    return self.GetClient().CreateHierarchy(self.key, schemaId, newHierarchy)

  def CreateSchema(self, schemaName=None):
    """Method for creating a new schema in the database designer
    Parameters
      key
        Type: System.String
        Key to validate the user.
      schemaName
        Type: System.String
        The name that the new schema should have
    Return Value
      Type: Int32
      The id of the new schema
    """
    if schemaName is None:
      raise Exception('Please specify schemaName')

    return self.GetClient().CreateSchema(self.key, schemaName)

  def CreateTable(self, schemaId=None, newTable=None):
    """Method for creating a new table in a schema in the database designer
    Parameters
      key
        Type: System.String
        Key to validate the user.
      schemaId
        Type: System.Int32
        The id of the schema to which the new table should be added
      newTable
        Type: Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport.WsDbTable
        The definition of the table you want to create
    Return Value
      Type: Int32
      The id of the new table
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')
    if newTable is None:
      raise Exception('Please specify newTable')

    return self.GetClient().CreateTable(self.key, schemaId, newTable)

  def CreateUserdefinedColumn(self, tableId=None, columnName=None, columnWidth=None, languageIndependent=None):
    """Method for creating a userdefined column
    Parameters
      key
        Type: System.String
        Key to validate the user
      tableId
        Type: System.Int32
        The id of the table we want to add a column to
      columnName
        Type: System.String
        The name of the new column
      columnWidth
        Type: System.Int32
        the dababase fieldwidth of the column
      languageIndependent
        Type: System.Boolean
        If the column is language transparent
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if columnName is None:
      raise Exception('Please specify columnName')
    if columnWidth is None:
      raise Exception('Please specify columnWidth')
    if languageIndependent is None:
      raise Exception('Please specify languageIndependent')

    return self.GetClient().CreateUserdefinedColumn(self.key, tableId, columnName, columnWidth, languageIndependent)

  def DeleteAllContent(self, tableId=None):
    """Delete all content for a table in design mode.
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id to delete all content.
    Return Value
      Type:String[]
      Row ids that where not deleted due to a contraint. If all rows where deleted successfully, an empty array is returned.
    """
    if tableId is None:
      raise Exception('Please specify tableId')

    return self.GetClient().DeleteAllContent(self.key, tableId)

  def DeleteContent(self, tableId=None, idsToDelete=None):
    """Deletes content for a table in design mode.
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id to delete content.
      idsToDelete
        Type:System.String[]
        The ids of the rows to delete.
    Return Value
      Type:String[]
      Row ids that where not deleted due to a contraint. If all rows where deleted successfully, an empty array is returned.
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if idsToDelete is None:
      raise Exception('Please specify idsToDelete')

    return self.GetClient().DeleteContent(self.key, tableId, idsToDelete)

  def DeleteUserDefinedColumn(self, tableId=None, columnName=None):
    """Method for deleting a userdefined column
    Parameters
      key
        Type: System.String
        Key to validate the user
      tableId
        Type: System.Int32
        The id of the table we want to delete a column from
      columnName
        Type: System.String
        The name of the column we want to delete
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if columnName is None:
      raise Exception('Please specify columnName')

    return self.GetClient().DeleteUserDefinedColumn(self.key, tableId, columnName)

  def GenerateTable(self, schemaId=None, tableId=None):
    """Method for generating a table
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema to which the table belongs
      tableId
        Type: System.Int32
        The id of the table we want to generate
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')
    if tableId is None:
      raise Exception('Please specify tableId')

    return self.GetClient().GenerateTable(self.key, schemaId, tableId)

  def GetContent(self, tableId=None, pageSize=None, lastPageId=None, direction=None, getRunTimeContent=None, ids=None):
    """Returns a DatabaseContent containing the database designer content data.
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id for the database designer table.
      pageSize
        Type: System.Int32
        The number of rows requested.
      lastPageId
        Type: System.String
        Use Null to start from the beginning. For paging, use the last id from the previous query.
      direction
        Type: BrowseListDirection
        The direction to retrieve the next page.
      getRunTimeContent
        Type: System.Boolean
        True to get run time content, False to get design time content.
      ids
        Type:System.String[]
        Filter with the specified ids. Use null to disable filtering.
    Return Value
      Type: DatabaseContent
      The datbase content for requested table
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if pageSize is None:
      raise Exception('Please specify pageSize')
    if lastPageId is None:
      raise Exception('Please specify lastPageId')
    if direction is None:
      raise Exception('Please specify direction')
    if getRunTimeContent is None:
      raise Exception('Please specify getRunTimeContent')
    if ids is None:
      raise Exception('Please specify ids')

    return self.GetClient().GetContent(self.key, tableId, pageSize, lastPageId, direction, getRunTimeContent, ids)

  def GetHierarchies(self, schemaId=None):
    """Method for obtaining the definition of all hierarchies in a given schema
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema we want all hierarchies for
    Return Value
      Type:WSHierarchy[]
      A collection of data carrier classes each holding the definition of one hierarchy
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetHierarchies(self.key, schemaId)

  def GetHierarchyGuid(self, schemaId=None, hierarchyId=None):
    """Method to obtain the Hierarchy Guid
    Parameters
      key
        Type: System.String
        Key to validate the user.
      schemaId
        Type: System.Int32
      hierarchyId
        Type: System.Int32
    Return Value
      Type: Guid
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')
    if hierarchyId is None:
      raise Exception('Please specify hierarchyId')

    return self.GetClient().GetHierarchyGuid(self.key, schemaId, hierarchyId)

  def GetSchemaGuid(self, schemaId=None):
    """Method to obtain the Schema Guid
    Parameters
      key
        Type: System.String
      schemaId
        Type: System.Int32
    Return Value
      Type: Guid
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetSchemaGuid(self.key, schemaId)

  def GetSchemaName(self, schemaId=None):
    """Method for obtaining the name of a given table schema
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema
    Return Value
      Type: String
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetSchemaName(self.key, schemaId)

  def GetTableIds(self, schemaId=None):
    """Gets the id's of all non-deleted tables belonging to a specified schema in design mode
    Parameters
      key
        Type: System.String
        Key to validate user.
      schemaId
        Type: System.Int32
        THe id of the schema we want all tables for
    Return Value
      Type:Int32[]
      The ids of all tables belonging to the specified schema
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetTableIds(self.key, schemaId)

  def GetTableSchemaInfoFromSchemaGuid(self, schemaId=None):
    """Gets basic information (ids and name) of a specific table schema
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Guid
        The id of the schema we want the info for
    Return Value
      Type: WsTableSchema
      A datacarrier holding the basic scheam information
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetTableSchemaInfoFromSchemaGuid(self.key, schemaId)

  def GetTableSchemaInfoFromSchemaId(self, schemaId=None):
    """Gets basic information (ids and name) of a specific table schema
    Parameters
      key
        Type: System.String
        Key to validate the user
      schemaId
        Type: System.Int32
        The id of the schema we want the info for
    Return Value
      Type: WsTableSchema
      A datacarrier holding the basic scheam information
    """
    if schemaId is None:
      raise Exception('Please specify schemaId')

    return self.GetClient().GetTableSchemaInfoFromSchemaId(self.key, schemaId)

  def SynchronizeContent(self, tableId=None):
    """Synchronize content from design to runtim for a table.
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id to synchronize content for.
    """
    if tableId is None:
      raise Exception('Please specify tableId')

    return self.GetClient().SynchronizeContent(self.key, tableId)

  def UpdateContent(self, tableId=None, dbContent=None):
    """Update content for a table in design mode.
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id to update content.
      dbContent
        Type: Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport.DatabaseContent
        The content to be updated.
    Return Value
      Type:Boolean[]
      A boolean array whether the rows existed or not.
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if dbContent is None:
      raise Exception('Please specify dbContent')

    return self.GetClient().UpdateContent(self.key, tableId, dbContent)

  def UpdateContentInDesignAndRuntime(self, tableId=None, dbContent=None):
    """Update content for a table in design mode and runtime mode
    Parameters
      key
        Type: System.String
        Key to validate user.
      tableId
        Type: System.Int32
        The table id to update content.
      dbContent
        Type: Firmglobal.Confirmit.Authoring.TableSchemas.WebServiceSupport.DatabaseContent
        The content to be updated.
    Return Value
      Type:Boolean[]
      A boolean array whether the rows existed or not in the runtime table
    """
    if tableId is None:
      raise Exception('Please specify tableId')
    if dbContent is None:
      raise Exception('Please specify dbContent')

    return self.GetClient().UpdateContentInDesignAndRuntime(self.key, tableId, dbContent)
