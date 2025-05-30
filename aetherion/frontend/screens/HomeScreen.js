import React from 'react';
import { View, TouchableOpacity, Text, StyleSheet } from 'react-native';

export default function HomeScreen({ navigation, route }) {
  const user = route.params.user;
  return (
    <View style={styles.container}>
      <Text style={styles.welcome}>Welcome, {user}</Text>

      <TouchableOpacity style={styles.btn} onPress={()=> navigation.navigate('Vault')}>
        <Text style={styles.btnText}>🗝 Vault</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.btn} onPress={()=> navigation.navigate('Scrolls')}>
        <Text style={styles.btnText}>📜 Archive</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.btn} onPress={()=> navigation.navigate('Oracle')}>
        <Text style={styles.btnText}>🔮 Oracle</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container:{ flex:1, bgColor:'#000', alignItems:'center', justifyContent:'center', padding:20 },
  welcome:{ fontSize:24, color:'#C4B5FD', marginBottom:40 },
  btn:{ backgroundColor:'#1E1B2E', padding:16, marginVertical:8, borderRadius:8, width:'80%' },
  btnText:{ color:'#A855F7', fontSize:18, textAlign:'center' }
});
