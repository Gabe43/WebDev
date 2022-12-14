// CHALLENGE: uncomment the code below and see the car stats rendered
import React from "react";
import ReactDOM from "react-dom";
import cars from "./practice"

//Destructuring Arrays and Objects

const [honda, tesla] = cars

//Tesla Components
const {coloursByPopularity: [teslaTopColour] , speedStats: {topSpeed : teslaTopSpeed }} = tesla


//Honda Components
const {coloursByPopularity: [hondaTopColour], speedStats: {topSpeed : hondaTopSpeed}} = honda





ReactDOM.render(
  <table>
    <tr>
      <th>Brand</th>
      <th>Top Speed</th>
      <th>Top Color</th> 
    </tr>
    <tr>
      <td>{tesla.model}</td>
      <td>{teslaTopSpeed}</td>
      <td>{teslaTopColour}</td>
    </tr>
    <tr>
      <td>{honda.model}</td>
      <td>{hondaTopSpeed}</td>
      <td>{hondaTopColour}</td>
    </tr>
  </table>,
  document.getElementById("root")
);
