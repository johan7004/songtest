import React, { Component } from 'react'
import API from './components/api'
import {View, Text} from 'react-native'

export default class App extends Component {
  render() {
    return (
      <View>
      
        <Text>
          <API></API>

        </Text>
      
      </View>
    )
  }
}
