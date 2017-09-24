/*
 * Given two strings s1, s2, write a function that returns true if s2 is a special substring s1. A special substring s2 is such that the s1 contains s2 where each character in s2 appears in sequence in s1, but there can be any characters in s1 in between the sequence.
 * Example:
 * isSpecialSubstring('abcdefg', 'abc') => true
 * isSpecialSubstring('abcdefg', 'acg') => true
 * The first two are abc and acg appears in 'abcdefg' in that order, although there might be multiple chars between the next character in s2.
 * The last one is false, because in 'acb' the character 'b' appears before the character 'c' in 'abcdefg'
 * Credit : https://www.careercup.com/question?id=5670677955739648
 *
 */

const isSpecialSubstring = (s1, s2) => {
  // Check if s2 > s1 return false
  // loop s1 and s2 in parallel and set index for both
  // if iS1 > EOW return false

  if(s1.length < s2.lenght ) return false;

  let position = 0;
  let hitCounter = 0;
  let iS1 = 0;
  for( let iS2 = 0; iS2 < s2.length; iS2++ ) {
    for(iS1 = position; iS1 < s1.length ; iS1++) {
      if(s1[iS1] === s2[iS2]){
        console.log("found "+s2[iS2])
        break;
      }
    }
    if (iS1 >= s1.length)
      return false;
    hitCounter++;
    position = iS1 + 1;
    console.log(`hit counter ${hitCounter} position ${position}`)
  }
  return hitCounter < s2.length ? false : true;
}

console.log("String manipulation")
console.log(isSpecialSubstring('abcdefg','aeg'))
console.log(isSpecialSubstring('abcdefg', 'acg'));
console.log(isSpecialSubstring('abcdefg', 'aeb'));

/*
 * Best Solution from Internet is as below
 * bool IsSubsequence(string const &s, string const &sub_s)
{
	int i = 0;
	for (int j = 0; j < s.size() && i < sub_s.size(); ++j) {
		if (s[j] == sub_s[i]) {
			++i;
		}
	}
	return i == sub_s.size();
}
*/
