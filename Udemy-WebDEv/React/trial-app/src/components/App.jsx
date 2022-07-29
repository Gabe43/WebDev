import React from "react";
import Card from "./Card";
import contacts from "../contacts";


function createCard(contacts) {
  return <Card key={contacts.id} name={contacts.name} image={contacts.imgURL} number={contacts.phone} mail={contacts.email} />
}

function App() {
  return <div>
    <h1 className="heading">My Contacts</h1>
    {contacts.map(createCard)}
  </div>
}



export default App;
