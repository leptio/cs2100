#adding custom objects to a set/dict requires __hash__()
#__hash__() must always return the same value for the same object
#return the same valuable for equal objects (__eq__)

#desirably, different objects compute different values
#and the hash is fast to compute (O(1))

#lists check all items -> O(n) worst case
#Sets use hash tables -> O(1) average case
#binary search -> O(log n) complexity
#hashed search  (constant) -> O(1) complexity
#linear search -> O(n) complexity

#HASH USED FOR IMMUTABLES: CONSTANT TIME (sets, keys)

#hash -> map value to integer
#hash table -> a list that stores elements via hashing
#hash set -> a set of elements stored using the same hash function
#hash function -> algorithm mapping values to indexes
#hash function could be %(modulo), len (for strings)

#collision: hash is already occupied and new data has hte same hash value

#COLLISION SOLUTIONS:
#probing: if next hash is empty, assign
#(move to next available slot)
#chaining: add/search/remove must traverse list, but the lists are short
#(store list at each index)

