import React from 'react';
import { StyleSheet, Text, View, TextInput, Button, Alert } from 'react-native'; 


function Home() {
    return (
        <View style={styles.input}>
            
            <TextInput
        style={{height: 40}}
        placeholder="Enter Song Title"
        
      />
      <Button 
      title="Search Song"
      
      onPress={() => Alert.alert('Button Pressed')}
      ></Button>
        </View>
    )

}

const styles = StyleSheet.create({
    input:{
        padding:'15%',
        

    }
    
})
export default Home
