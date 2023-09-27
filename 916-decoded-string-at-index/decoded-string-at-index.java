class Solution {
    public String decodeAtIndex(String s, int k) {
       long size = 0;
       int n = s.length();

       for (int i = 0; i < n; ++i) {
           char c = s.charAt(i);
           if (Character.isDigit(c)) {
               size *= c - '0';
           } else {
               size++;
           }
       }

       for (int i = n - 1; i > -1; --i) {
           
           char c = s.charAt(i);
           
           if (Character.isDigit(c)) {
               size /= c - '0';
               k %= size;
           } else {
               if (k % size == 0) {
                   return Character.toString(c);
               }
               size--;
           }
       }
        return ""; 
    }
}