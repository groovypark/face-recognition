import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
  state ={
    file: null,
    faces: []
  };

  onHandleImage = (e) => {
    const file = e.target.files[0];
    this.fileUpload(file).then(({data})=>{
      if (data.faces.length === 0) {
        alert("닮은 연예인이 없습니다.");
        return;
      }
      this.setState({
        faces: data.faces
      })
    }).catch(error => {
      const message = error.response.data.message;
      message && alert(message);
    })
  };

  fileUpload = (file) => {
    const url = '/upload';
    const formData = new FormData();
    formData.append('file',file);
    const config = {
        headers: {
            'content-type': 'multipart/form-data'
        }
    };
    return axios.post(url, formData, config)
  };

  render() {
    const {
      faces
    } = this.state;

    return (
      <div className="App">
        <header className="App-header">
          {faces.map(({celebrity}, i) => (
            <div key={i}>
              <h1>
                닮은 연예인: {celebrity.value}
                신뢰도: {celebrity.confidence}
              </h1>
            </div>
          ))}
          <input type="file" name="file" onChange={this.onHandleImage}/>
        </header>
      </div>
    );
  }
}

export default App;
