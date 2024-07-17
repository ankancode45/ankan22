from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/sort')
def sort():
    a=[2,10,85,77,99]
    a.sort()
    return jsonify(sorted_numbers=a)   
if __name__=='__main__':
    app.run(debug=True)