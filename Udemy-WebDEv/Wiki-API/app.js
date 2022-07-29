const express = require("express")
const mongoose = require("mongoose")
const bodyParser = require("body-parser")
const ejs = require("ejs")

const app = express()

app.set("view engine", "ejs")

app.use(express.static("public"))

app.use(bodyParser.urlencoded({ extended: true }))


mongoose.connect("mongodb://localhost:27017/wikiDB")


const articleSchema = new mongoose.Schema({
    title: String,
    content: String
})


const Article = mongoose.model("Article", articleSchema)

app.route("/articles")/* if we use app.route("/the route") we dont need to write the route many times and we can write the code like this */

    .get(function (req, res) {
        Article.find(function (err, list) {
            if (err) {
                console.log(err)
            }
            else {
                res.send(list)
            }
        })
    })
    .post(function (req, res) {
        const nwArticle = new Article({
            title: req.body.title,
            content: req.body.content
        })
        nwArticle.save(function (err) {
            if (err) {
                console.log(err)
            }
            else {
                res.send("Successfully Added a new Article")
            }
        })
    })
    .delete(function (req, res) {
        Article.deleteMany(function (err) {
            if (err) {
                console.log(err)
            }
            else {
                res.send("Successfully Deleted All Articles")
            }
        })
    })

app.route("/articles/:input")
    .get(function (req, res) {
        Article.find({ title: req.params.input }, function (err, list) {
            if (err) {
                console.log(err)
            }
            else {
                res.send(list)
            }
        })
    })

    .put(function (req, res) {
        Article.replaceOne({ title: req.params.input }, { title: req.body.title, content: req.body.content }, { overwrite: true }, function (err) {
            if (err) {
                console.log(err)
            } else {
                res.send("Successfully Updated")
            }
        })
    })

    .patch(function (req, res) {
        Article.updateOne({ title: req.params.input }, { title: req.body.title, content: req.body.content }, function (err) {
            if (err) {
                console.log(err)
            } else {
                res.send("Successfully Updated")
            }
        })
    })

    .delete(function (req, res) {
        Article.deleteOne({ title: req.params.input }, function (err) {
            if (err) {
                console.log(err)
            } else {
                res.send("Successfully Deleted Article")
            }
        })
    })




app.listen(3000, function () {
    console.log("Server running on port 3000")
})