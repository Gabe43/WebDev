import React from "react";


function Form(props) {
  return (
    <form className="form">
      <input type="text" placeholder="Username" />
      <input type="password" placeholder="Password" />
      {props.IsRegistered ? <button type="submit">Login</button> :
        <div>
          <input type="password" placeholder="Confirm Password" />
          <button type="submit">Register</button>
        </div>}
    </form>
  );
}

export default Form;
