import flask
from flask import request, jsonify
from ciclista.DLO.CiclistaDLO import CiclistaDLO

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Teste Rest API com Flask!</h1>"

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>Erro 404: Página não encontrada!</h1>"

@app.route('/cliente', methods=['GET'])
def crud():
    param = request.args
    nmpropertie = param.get('propertie', type=str)
    vlpropertie = []
    vlpropertie.append(param.get('value', type=str))
    action = param.get('action', type=str)
    objDlo = CiclistaDLO()
    result = None

    if action == 'delete': #/cliente?action=delete&propertie=id&value=4
        result = objDlo.deleteById(vlpropertie)
    elif action == 'update': #/cliente?action=update&propertie=id&value=Marco,marco@email.com,Tarmac,Road,4
        print(str(vlpropertie[0]).split(','))
        result = objDlo.updateById(str(vlpropertie[0]).split(','))
    elif action == 'insert': #/cliente?action=insert&propertie=all&value=4,Marco,marco@email.com,Tarmac,Road
        result = objDlo.insert(str(vlpropertie[0]).split(','))
    elif action == 'select':
        if nmpropertie == 'email': #/cliente?action=select&propertie=email&value=bernardo.2016@gmail.com
            result = objDlo.selectByEmail(nmpropertie, vlpropertie)
        elif nmpropertie == 'id': #/cliente?action=select&propertie=id&value=1
            result = objDlo.selectById(nmpropertie, vlpropertie)
    else:
        result = pageNotFound(404)
    result = [d.__dict__ for d in result]

    return jsonify(cliente=result)

app.run()
