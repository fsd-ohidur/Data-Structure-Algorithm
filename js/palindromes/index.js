// ------------ Directions
// Given a string, return true if string is palindrome or false.
// palindrome is a same word when it's reversed

// ------------ Example
// palindrome('abba')===true
// palindrome('abcdef')===false

function palindrome(word){
    // Process-1
    // let reversed=word.split('').reduce((reverse,char)=>char+reverse,'')

    // Process-2
    // let reversed=word.split('').reverse().join('')
    // return word===reversed

    // Process-3
    return word.split('').every((c,i)=>{
        return c===word[word.length-i-1]
    })


}

module.exports=palindrome