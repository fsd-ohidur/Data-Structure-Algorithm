const reverse=require('./reverse_string/index')
const palindrome = require('./palindromes/index')
const reverseInt = require('./reverse_int/index')

const word = 'abba'
const numbers=-312
// let result = reverse(word)
// let result = palindrome(word)
let result=reverseInt(numbers)


console.log(result)
