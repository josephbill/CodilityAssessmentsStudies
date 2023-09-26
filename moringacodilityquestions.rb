# 1. function takes two numbers => def compareNumbers(a,b)
# 2. when a > b -> a is greater than b 
# 3. when a < b -> a is less than b 
# 4. else a = b -> a is equal than b 

# def compareNumbers(a,b)
#     #using string interpolation
# if 'a' is equal 'b' return a string "equal to"
#     ....
# end

# <=> : spaceship conditional.

def compareNumbers(a,b)
    comparison = a <=> b
    abs_comparison = comparison.abs 
    str = "#{a} is "
    str += "greater than " * ((comparison + 1) / 2)
    str += "less than " * ((-comparison + 1) / 2)
    str += "equal to " * (1 - abs_comparison)
    str += "#{b}"
 end
 
 puts compareNumbers(2,2)
 puts compareNumbers(4,2)
 puts compareNumbers(2,4)
 
 
 # 2. 
 # BDD 
 # countCharacters('Bass')
 # [["B",1],["a",1],["s",2]]
 # 1. def countCharacters('')
 #     have an empty hash => keep count of each character in the input string -< {}
 #     have an empty array => this array will contain hashes with key ->character , count -> value 
 #     loop through each character in the string , -> each -> each_char(loop,sort)
 #     if the hash does not contain the character as a key , we create it and set its count to 0 
 #     each subsequent iteration will increment the value of the key 
 #     loop the hash , append an array of the key and value to our empty array 
 #     return a list of arrays 
 # end 
 
 def count_characters(str)
     char_count = {} 
     result = []
     str.each_char do |c|
         char_count[c] ||= 0
         char_count[c] += 1
     end
     char_count.each_pair do |key,value|
         result << [key,value]
     end
     result 
 end
 
 puts count_characters("Bass")


#  2. // Write a function that merges two strings together. It does so by merging the end of the first string with the start of the second string together when they are an exact match.

#  // "abcde" + "cdefgh" => "abcdefgh"
 
#  // "abaab" + "aabab" => "abaabab"
 
#  // "abc" + "def" => "abcdef"
 
#  // "abc" + "abc" => "abc"
 
#  // NOTE: The algorithm should always use the longest possible overlap.
 
#  // "abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"

# check explanation for pseudocode on .js file

def merge_strings(s1, s2)
    overlap = 0
    (1..[s1.length, s2.length].min).each do |i|
      if s1[-i..-1] == s2[0...i]
        overlap = i
      end
    end
    s1 + s2[overlap..-1]
  end
  

  puts merge_strings("abc", "abc")  # output: "abcdefgh"
# syntax explanation: 

# In the expression s1[-i..-1], the .. operator creates a range object that includes the last i characters of s1.
#  The -1 argument means that the end of the range is the last character of s1. The negative index is used to count the positions
#   from the end of the string, so s1[-i] would be the i-th character from the end.

# Similarly, in the expression s2[0...i], the ... operator creates a range object that includes the first i characters of s2. 
# The 0 argument means that the start of the range is the first character of s2. The ... operator is used to exclude the i-th character from the range.

# So, the expression s1[-i..-1] gets the last i characters of s1, and the expression s2[0...i] gets the first i characters of s2. 
# The if statement then checks if these two substrings are equal, which means they are a possible overlap.

# camel case question 
# Challenge 1: CamelCase Method(Toy Problem)
# Write simple .camelCase method for strings. All words must have their first letter capitalized without spaces.

# For instance:

# 'hello case'.camelcase => HelloCase

# 'camel case word'.camelcase => CamelCaseWord
# 1. first split the string into an array of words using the split method
# 2. map over each word to capitalize the first letter using capitalize
# 3. join the words back into a single string using the join method.
def camelCase(a)
  a.split.map(&:capitalize).join(' ')
end 

puts camelCase("joseph mbugua")
