import React from 'react'
import axios, { post } from 'axios';

class FileUpload extends React.Component {



  render() {
    return (
      <form onSubmit={this.onFormSubmit}>
        <h1>File Upload</h1>
        <input type="file" onChange={this.onChange} />
        <button type="submit">Upload</button>
      </form>
   )
  }
}



export default FileUpload