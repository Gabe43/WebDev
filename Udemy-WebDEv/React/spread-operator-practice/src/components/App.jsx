import React from "react";

function App() {

  const [todoItem, manageItem] = React.useState({
    items: [],
    item: ""
  })

  function chnge(event) {
    const { value } = event.target

    manageItem(preValue => {
      return {
        ...preValue,
        item: value
      }
    })
  }

  function sbmit() {
    todoItem.items.push(todoItem.item)

    todoItem.item =  ""
    
    manageItem(preValue => {
      return {
        ...preValue
      }
    })
  }

  return (
    <div className="container">
      <div className="heading">
        <h1>To-Do List</h1>
      </div>
      <div className="form">
        <input onChange={chnge} type="text" value={todoItem.item} />
        <button onClick={sbmit}>
          <span>Add</span>
        </button>
      </div>
      <div>
        <ul>
          {todoItem.items.map(item => <li>{item}</li>)}
        </ul>
      </div>
    </div>
  );
}

export default App;
