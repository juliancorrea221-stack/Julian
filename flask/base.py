from flask import Flask, request, jsonify, session

app=Flask(__name__)
app.secret_key="secret1112345"
USER={
    "username:admin",
    "password:1234",

}
@app.route("/api/login",methods=["POST"])
def login(e):
    data= request.json

