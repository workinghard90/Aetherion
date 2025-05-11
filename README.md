  useEffect(() => {
    getUniverse()
      .then(setEntities)
      .catch((err) => {
        console.error('API failed:', err);
      });
  }, []);

  const renderItem = ({ item }) => (
    <TouchableOpacity onPress={() => navigation.navigate('Entity', { entity: item })}>
      <View>
        <Text>{item.name} ({item.type})</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={{ padding: 20 }}>
      <Button title="Create Entity" onPress={() => navigation.navigate('CreateEntity')} />
      <FlatList
        data={entities}
        keyExtractor={(item) => item.id.toString()}
        renderItem={renderItem}
      />
    </View>
  );
}
