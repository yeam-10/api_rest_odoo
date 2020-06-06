
import xmlrpc.client

db = "name_db" 
username ="name_user"
password = "clave"
url = "http://192.168.0.7:8069" 


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url)) #realiza el formateo a la url
uid = common.authenticate(db, username, password, {}) # declara una variable uid para luego pasar como parametro

# call methods: objeto que envia sentencias mediante los modelos de odoo

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

#Create records

id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "New Partner"

}])



print id #imprime el id insertado


###################################################################################################

#update

