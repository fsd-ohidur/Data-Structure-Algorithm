// -----------------------Directions
// Given a string, return a new string with the reversed order of characters

// -----------------------Example
// reverse('apple') === 'elppa'
// reverse('hello') === 'olleh'

function reverse(word)
{
// ----------------------- Soution 1
// const arr=word.split('')
// arr.reverse()
// return arr.join('')

// Single Line
// return word.split('').reverse().join('');

// ----------------------- Solution 2
// let reversed=''
// for(i=word.length-1;i>=0; i--){
//     reversed=reversed+word[i];
// }

// for (let character of word){
//         reversed=character+reversed;
// }
// return reversed

// ----------------------- Solution 3
// one way
    // return word.split('').reduce(
    //     (reversed, character)=>{
    //         return character+reversed
    //     },
    // '')
    
// another way
    return word.split('').reduce((reversed, character)=>character+reversed,'')
}

module.exports=reverse