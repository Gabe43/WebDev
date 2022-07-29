import React from "react";

function App() {

  const [Time, currentTime] = React.useState("TIME")

  function showTime() {
    setInterval(function () {
      let time = new Date().toLocaleTimeString().slice(0,7)
      currentTime(time)
    }, 1000)
  }


  return (
    <div className="container">
      <h1>{Time}</h1>
      <button onClick={showTime}>Get Time</button>
    </div>
  );
}

export default App;
