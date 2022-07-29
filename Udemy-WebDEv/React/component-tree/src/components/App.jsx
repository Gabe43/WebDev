import React, { useState } from "react";
import { Heading, Listitem } from "./TodoItems";


function App() {

  const [inputText, setInputText] = useState("");
  const [items, setItems] = useState([]);

  function handleChange(event) {
    const newValue = event.target.value;
    setInputText(newValue);
  }

  function addItem() {
    setItems(prevItems => {
      return [...prevItems, inputText];
    });
    setInputText("");
  }

  function deleteItem(id) {
    setItems(prevItems => {
      return prevItems.filter((items,index)=>{
      return index !== id
      })
    })
  }

  return (
    <div className="container">
      <Heading />
      <div className="form">
        <input onChange={handleChange} type="text" value={inputText} />
        <button onClick={addItem}>
          <span>Add</span>
        </button>
      </div>
      <div>
        <ul>
          {items.map((todoItem, index) => (
            <Listitem key={index} id={index
            } text={todoItem} onChecked={deleteItem} />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
