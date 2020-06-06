from xmlrpc import client as xmlrpclib
url = 'http://127.0.0.1:12000'
db = 'your_database'
username = 'admin'
password = 'admin'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

uid = common.login(db, username, password)
result = models.execute(db, uid, password, 'res.partner', 'search_read', [['id', '=', 1]])
number_of_customers = models.execute(db, uid, password, 'res.partner', 'search_count', [])
numberc = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner"
}])

print('Number of customers: ' + str(number_of_customers))
print('result: ' + str(result[0].get('name')))

print ('numberc :' + str(numberc))



