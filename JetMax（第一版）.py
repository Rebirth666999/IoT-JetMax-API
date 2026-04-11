from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/suck',methods=['GET'])
def suck():

    #此处添加机械臂打开吸盘的程序

    return jsonify(name='is_ok',type='bool',desp='success')

@app.route('/put',methods=['GET'])
def put():

    #此处添加机械臂关闭吸盘的程序

    return jsonify(name='is_ok',type='bool',desp='success')

@app.route('/move_head',methods=['POST'])
def move_head():

    my_json=request.get_json()
    name=my_json.get('name')
    type=my_json.get('type')
    require=my_json.get('require')
    desp=my_json.get('desp')

    if name=='pos' and type=='double[]' and require==1:

        x=desp[0]
        y=desp[1]
        z=desp[2]

        print(x,y,z)
        # 此处添加机械臂根据坐标移动的程序

        return jsonify(name='is_ok',type='bool',desp='success')

    else:

        return jsonify(msg='"name"或者"type"或者"require"输入不正确')

@app.route('/base_turn',methods=['POST'])
def base_turn():

    my_json=request.get_json()
    name=my_json.get('name')
    type=my_json.get('type')
    require=my_json.get('require')
    desp=my_json.get('desp')

    if name=='angle' and type=='double' and require==1:

        t=desp#角度制

        print(t)
        # 此处添加控制机械臂基座舵机的旋转角度的程序

        return jsonify(name='is_ok',type='bool',desp='success')

    else:

        return jsonify(msg='"name"或者"type"或者"require"输入不正确')

@app.route('/single_turn',methods=['POST'])
def single_turn():
    #怎么同时接收两组数据？
    return jsonify(name='is_ok',type='bool',desp='success')

@app.route('/multiple_turn',methods=['POST'])
def multiple_turn():
    # 怎么同时接收两组数据？
    return jsonify(name='is_ok',type='bool',desp='success')

if __name__ == '__main__':
    app.run(host='0.0.0.0')