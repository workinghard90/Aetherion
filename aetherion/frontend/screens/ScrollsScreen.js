import React, { useEffect, useState } from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';
import { getScrolls } from '../services/api';

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);
  useEffect(()=>{ getScrolls().then(setScrolls); }, []);
  return (
    <FlatList
      contentContainerStyle={styles.container}
      data={scrolls}
      keyExtractor={(_,i)=>i.toString()}
      renderItem={({ item })=>(
        <View style={styles.card}>
          <Text style={styles.title}>{item.title}</Text>
          <Text style={styles.body}>{item.body}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  container:{ padding:20, bgColor:'#000' },
  card:{ bgColor:'#1E1B2E', padding:16, borderRadius:8, marginBottom:12 },
  title:{ color:'#A855F7', fontSize:18, marginBottom:8 },
  body:{ color:'#C4B5FD' }
});
