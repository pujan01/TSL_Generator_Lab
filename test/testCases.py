colName = 'age'
docName = 'document'

firestoreStorage.updateField(colName, docName, [('field', 'value')])

def testCase_1():
  firestoreStorage.updateField(colName, docName, [])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') = 'value'
  
def testCase_2():
  firestoreStorage.updateField(colName, docName, [('field', 'newVal')])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') = 'newVal'

def testCase_3():
  firestoreStorage.updateField(colName, docName, [('field', ['val1', 'val2'])])
  assert firestoreStorage.getFieldValue(colName, docName, 'field') == ['val1', 'val2']