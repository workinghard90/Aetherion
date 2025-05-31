import React, { useEffect, useState } from 'react';
import { FlatList, View, Text, StyleSheet } from 'react-native';
import { getScrolls } from '../services/api';

export default function ScrollsScreen() {
  const [scrolls, setScrolls] = useState([]);
  useEffect(()=>{ getScrolls().then(setScrolls); }, []);

  return (
    <FlatList
      data={scrolls}
      keyExtractor={(_,i)=>i.toString()}
      contentContainerStyle={styles.container}
      renderItem={({item})=>(
        <View style={styles.card}>
          <Text style={styles.title}>{item.archive_title || item.seed_title || item.realm_name}</Text>
          <Text style={styles.body}>{JSON.stringify(item, null, 2)}</Text>
        </View>
      )}
    />
  );
}

const styles = StyleSheet.create({
  container:{ padding:20, backgroundColor:'#000' },
  card:{ backgroundColor:'#1E1B2E', padding:16, borderRadius:8, marginBottom:12 },
  title:{ color:'#A855F7', fontSize:18, marginBottom:8 },
  body:{ color:'#C4B5FD', fontSize:12 }
});
