/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */
class Solution {
    // Picking a random number between a and b (where a and b are inclusive).
    public static int pickRandom(int a, int b) {
        Random rand = new Random();
        int randomNum = rand.nextInt((b - a) + 1) + a;
        return randomNum;
    }
    // Returns an array list containing indices of words when match(word, compare) is equal to matchCount
    public static ArrayList<Integer> populateChoices(String[] words, ArrayList<Integer> previousChoices, String compare, int matchCount){
        ArrayList<Integer> choices = new ArrayList<>();
        for(int idx : previousChoices){
            if(matching(words[idx], compare) == matchCount) choices.add(idx);
        }
        return choices;
    }
    // Returns an integer representing the number of exact matches (value and position) of word1 to word2.
    public static int matching(String word1, String word2){
        int count = 0;
        for(int i = 0; i < word1.length(); i++){
            if(word1.charAt(i) == word2.charAt(i)) count++;
        }
        return count;
    }

    public void findSecretWord(String[] words, Master master) {
        ArrayList<Integer> choices = new ArrayList<>();
        // Initially all the words are available
        for(int i = 0; i < words.length; i++){
            choices.add(i);
        }
        int index, targetIndex,matchCount;
        String randomWord;
        while(true){
            index = pickRandom(0, choices.size() - 1); // We pick the random index from the choices list, which contains indices of words (which are the available choices).
            targetIndex = choices.get(index); // We get the word's index from choices list based on random index choosed earlier.
            randomWord = words[targetIndex]; // We get the word based on targetIndex.
            matchCount = master.guess(randomWord); // We guess whether the selected word is the secret.
            if(matchCount == 6) return; // if it's secret we return
            choices = populateChoices(words, choices, randomWord, matchCount); // Else, now we have narrowed down our choices.
        }
    }
}