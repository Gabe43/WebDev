const mongoose = require("mongoose")


mongoose.connect('mongodb://localhost:27017/fruitsDB')


const fruitSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    rating: {
        type: Number,
        min: 1,
        max: 10
    },
    review: String
})


const peopleSchema = new mongoose.Schema({
    name: String,
    age: Number,
    favouriteFruit: fruitSchema
})


const Fruit = mongoose.model("Fruit", fruitSchema)
const People = mongoose.model("People", peopleSchema)



const mango = new Fruit({
    name: "Mango",
    rating: 9,
    review: "Pretty awesome as a fruit"
})

const banana = new Fruit({
    name: "Banana",
    rating: 6,
    review: "Not a good texture as a fruit"
})

const orange = new Fruit({
    name: "Orange",
    rating: 5,
    review: "Pretty sour as a fruit"
})

// const john = new People({
//     name: "John",
//     age: 37
// })

// john.save()



// Fruit.insertMany([mango, banana, orange], function(err){
//     if (err){
//         console.log(err)
//     }
//     else{
//         console.log("All the data was saved")
//     }
// })


// Fruit.find(function (err, fruits) {
//     if (err) {
//         console.log(err)
//     }
//     else {
//         mongoose.connection.close()


//         fruits.forEach(element => {
//             console.log(element.name)
//         });
//     }
// })

const grape = new Fruit({
    name: "Grape",
    rating: 6,
    review: "Pretty sour as a fruit"
})

grape.save()



People.updateOne({name: "John"}, {favouriteFruit: grape }, function(err){
    if (err){
        console.log(err)
    }else{
        mongoose.connection.close()
        console.log("Successfully Updated")
    }
})





// fruit.save()





























// Mongo db driver code


// const MongoClient = require('mongodb').MongoClient;
// const assert = require('assert');

// // Connection URL
// const url = 'mongodb://localhost:27017';

// // Database Name
// const dbName = 'fruitsDB';

// // Create a new MongoClient
// const client = new MongoClient(url);

// // Use connect method to connect to the Server
// client.connect(function (err) {
//     assert.equal(null, err);
//     console.log("Connected successfully to server");

//     const db = client.db(dbName);
//     insertDocuments(db, function () {
//         client.close();
//     });
// });

// const insertDocuments = function (db, callback) {
//     // Get the documents collection
//     const collection = db.collection('fruits');
//     // Insert some documents
//     collection.insertMany([
//         {
//             name: "Apple",
//             score: 8,
//             review: "Great Fruit"
//         },
//         {
//             name: "Orange",
//             score: 6,
//             review: "Kinda Sour"
//         },
//         {
//             name: "Banana",
//             score: 9,
//             review: "Great Stuff"
//         }
//     ], function (err, result) {
//         assert.equal(err, null);
//         assert.equal(3, result.result.n);
//         assert.equal(3, result.ops.length);
//         console.log("Inserted 3 documents into the collection");
//         callback(result);
//     });
// }