import logo from './logo.svg';
import './App.css';
import Option from './option.js'

function App() {

  function getClasses() {
    let data;
    // fetch('127.0.0.1:4000/')
    //   .then(response => {
    //     let data = response.json()
    //     console.log(data)
    //   })
    const url = '127.0.0.1:4000/';
    fetch(url)
      .then(response => response.json())
      .then(json => {
        console.log(json.JSON.jsonify);
      })

    const listOfClasses2 = [];

    // for (let i = 0; i < data.keys(dictionary).length; i++) {
    //   listOfClasses2.push(<option key={data[i]}></option>);
    // }

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
      {/* <img class = "blackadam" src={require('./blackadambald.jpeg')} alt='Black adam'></img> */}
      <h1 class="theTitle">Prof Planner</h1>
      <p>Welcome to the Professor Planner!</p>
      <label>Choose a Class:</label>


      <select name="classes" id="dropdown">
        {getClasses()}
      </select>


      <button className="button" onClick={getClasses}>Submit</button>

      <Option></Option>
    </div>
  );

}
export default App;

