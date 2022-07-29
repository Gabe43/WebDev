import React, { useState } from "react";

function App() {
  const [contact, setContact] = useState({
    fName: "",
    lName: "",
    email: ""
  });

  function changeState(event) {
    const { name, value } = event.target

    //One method
    name === "fName" ? setContact({ fName: value, lName: contact.lName, email: contact.email }) : name === "lName" ? setContact({ fName: contact.fName, lName: value, email: contact.email }) : setContact({ fName: contact.fName, lName: contact.lName, email: value })

    //Another Method
    // setContact((preValue) => {
    //   if (name === "fName") {
    //     return ({
    //       fName: value,
    //       lName: preValue.lName,
    //       email: preValue.email
    //     })
    //   } else if (name === "lName") {
    //     return ({
    //       fName: preValue.fName,
    //       lName: value,
    //       email: preValue.email
    //     })
    //   } else {
    //     return ({
    //       fName: preValue.fName,
    //       lName: preValue.lName,
    //       email: value
    //     })
    //   }
    // })



  }

  return (
    <div className="container">
      <h1>
        Hello {contact.fName} {contact.lName}
      </h1>
      <p>{contact.email}</p>
      <form>
        <input onChange={changeState} name="fName" placeholder="First Name" />
        <input onChange={changeState} name="lName" placeholder="Last Name" />
        <input onChange={changeState} name="email" placeholder="Email" />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
