import React, { Component } from 'react'

import axios from 'axios'
import {View} from 'react-native'





export default class API extends Component {
  state = {
    songs: []
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/app/')
      .then(res => {
        const songs = res.data;
        this.setState({ songs });
      })
      .catch (err =>{})
  }

  render() 
  {
    return (<View>{this.state.songs.map(songs=><p>{songs.title}</p>)}</View>)
  }
}



  
  