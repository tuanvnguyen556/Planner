import logo from './logo.svg';
import './App.css';

function App() {
  function getRequest() {
    const httprequest = new XMLHttpRequest();
    httprequest.open('GET', 'localhost:4000');
    httprequest.send();
    console.log(httprequest.responseText);
  }

  return (
    <div className="App">
      <h1>Hello world</h1>
      <button className="button" onClick={getRequest}>Submit</button>
    </div>
  );
}

export default App;
