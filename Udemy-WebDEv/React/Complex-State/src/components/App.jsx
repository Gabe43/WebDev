import React from "react";

function App() {

  const [fullName, setFullName] = React.useState({
    fName: "",
    lName: ""
  })


  function handelChange(event) {
    const { value, name } = event.target

    name === "fName" ? setFullName({ fName: value, lName: fullName.lName }) : setFullName({ fName: fullName.fName, lName: value })
  }


  return (
    <div className="container">
      <h1>Hello {fullName.fName} {fullName.lName}</h1>
      <form>
        <input onChange={handelChange} name="fName" placeholder="First Name" value={fullName.fName} />
        <input onChange={handelChange} name="lName" placeholder="Last Name" value={fullName.lName} />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
