const express = require("express")
const { send } = require("express/lib/response")

const app = express()



app.get("/", function(req,res){
    res.send("<h1>Hello World</h1>")
})

app.get("/contact", function(req,res){
    res.send("<h1>Contact</h1>")
})

app.listen(3000,function(){
    console.log("Server started at port 3000")
})



