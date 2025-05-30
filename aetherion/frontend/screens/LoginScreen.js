import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function LoginScreen({ navigation }) {
  const [name, setName] = useState('');

  const handleLogin = () => {
    if (name.trim()) navigation.replace('Home', { user: name });
    else alert('Enter a name.');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Aetherion</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter name..."
        placeholderTextColor="#aaa"
        onChangeText={setName}
        value={name}
      />
      <TouchableOpacity style={styles.button} onPress={handleLogin}>
        <Text style={styles.buttonText}>Invoke</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container:{ flex:1, bgColor:'#000', alignItems:'center', justifyContent:'center', padding:20 },
  title:{ fontSize:32, color:'#A855F7', marginBottom:40 },
  input:{ width:'100%', borderColor:'#555', borderWidth:1, borderRadius:8, padding:12, color:'#fff', marginBottom:20 },
  button:{ backgroundColor:'#A855F7', padding:16, borderRadius:8 },
  buttonText:{ color:'#fff', fontSize:16, textAlign:'center' }
});
