import React from "react";


// function App() {

//   const [isMousedOver, setMouseOver] = React.useState(false)

//   function mouseOver() {
//     setMouseOver(true)
//   }

//   function mouseOut() {
//     setMouseOver(false)
//   }

//   return (
//     <div className="container">
//       <h1>Hello</h1>
//       <input type="text" placeholder="What's your name?" />
//       <button style={{"backgroundColor": isMousedOver ? "black" : "white"}} onMouseOver={mouseOver} onMouseOut={mouseOut}>Submit</button>
//     </div>
//   );
// }

function App() {
  const [userInput, setName] = React.useState("")

  const [headingText, setHeading] = React.useState("")

  function chnge(event){
    setName(event.target.value)
  }

  function click(event){
    setHeading(userInput)


    event.preventDefault()
  }

  return (
    <div className="container">
      <h1>Hello {headingText}</h1>
      <form onSubmit={click}>
      <input onChange={chnge} type="text" placeholder="What's your name?" />
      <button type="submit">Submit</button>
      </form>
    </div>
  );
}


export default App;
