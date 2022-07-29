const express = require("express")
const https = require("https")
const { url } = require("inspector")
const bodyParser = require("body-parser")


const app = express()
app.use(bodyParser.urlencoded({ extended: true }))



app.get("/", function (req, res) {
    res.sendFile(__dirname + "/index.html")
})

app.post("/", function (req, res) {
    let city = req.body.cityName
    const url = `https://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=5b47e1b09698da5948780b7e4758386e`

    https.get(url, function (response) {

        response.on("data", function (data) {
            const dat = JSON.parse(data)
            const lat = dat[0].lat
            const lng = dat[0].lon

            const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lng}&appid=5b47e1b09698da5948780b7e4758386e&exclude=current,minutely,hourly`

            https.get(url, function (response) {
                // console.log(response.statusCode)

                response.on("data", function (data) {

                    const weatherData = JSON.parse(data)
                    const temp = weatherData.daily[0].temp.max
                    const weatherDesc = weatherData.daily[0].feels_like.eve
                    const icon = weatherData.daily[0].weather[0].icon

                    res.write(`<h1>The temperature in ${city} is ${temp} Fahrenheit</h1>`)
                    res.write(`<p>It feels like ${weatherDesc} Fahrenheit for sure..</p>`)
                    res.write(`<img src="https://openweathermap.org/img/wn/${icon}@2x.png">`)

                    res.send()//It doesnt accept numbers....Numbers needs to be converted to string
                })
            })
        })
    })
})




app.listen(3000, function () {
    console.log("The server is running on port 3000")
})


// const lat = 22.572645
//     const lon = 88.363892
//     const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&appid=5b47e1b09698da5948780b7e4758386e&exclude=current,minutely,hourly`

//     https.get(url, function (response) {
//         // console.log(response.statusCode)

//         response.on("data", function (data) {

//             const weatherData = JSON.parse(data)
//             const temp = weatherData.daily[0].temp.max
//             const weatherDesc = weatherData.daily[0].feels_like.eve
//             const icon = weatherData.daily[0].weather[0].icon

//             res.write(`<h1>The temperature in Kolkata is ${temp} Fahrenheit</h1>`)
//             res.write(`<p>It feels like ${weatherDesc} Fahrenheit for sure..</p>`)
//             res.write(`<img src="https://openweathermap.org/img/wn/${icon}@2x.png">`)

//             res.send()//It doesnt accept numbers....Numbers needs to be converted to string

//             // const object = {
//             //     name: "Angela",
//             //     favouriteFood: "Ramen"
//             // }
//             // console.log(JSON.stringify(object))
//         })
//     })