import logo from './logo.svg';
import './App.css';
import Option from './option.js'

function App() {

  function getClasses() {
    fetch('127.0.0.1:4000/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
    })
      .then(response => response.text())
      .then(text => console.log(text));

    const listOfClasses = [1, 2, 3, 4, 5, 6];
    const listOfClasses2 = [];

    for (let i = 0; i < listOfClasses.length; i++) {
      listOfClasses2.push(<option key={listOfClasses[i]}> <button onClick={() => console.log("TEST")}> {listOfClasses[i]} </button> </option>);
    }

    return listOfClasses2

  }




  // function getGpa() {
  //   fetch("127.0.0.1:4000/")
  //     .then((response) => response.json());

  //   const profList = [3, 5, 9, 3, 6, 9];
  //   const profList2 = [];
  //   for (let i = 0; i < profList.length; i++) {
  //     proflist2.push(<h6 key={profList[i]}>{profList[i]}</h6>);
  //   }
  //   return profList2
  // }


  return (
    <div className="App">
      <h1>Prof Planner</h1>
      <p>Welcome to the Professor Planner!</p>
      <label>Choose a Class:</label>

    
        {getClasses}  <select name="classes" id="dropdown">
        {getClasses()}
      </select>


      <button className="button" onClick={getClasses}>Submit</button>

      <Option></Option>
    </div>
  );

}
export default App;

