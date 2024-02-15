class Solution {
    public String makeGood(String s) {
        int n = s.length();

       Stack<Character> st=new Stack<>();
        int i=0;
        while(i<n){
           if(st.size()>0){
                // "abBAcC"
                while(st.size()>0 && i<n && Math.abs(st.peek()-s.charAt(i))==32){
                    st.pop();
                    i+=1;
                }
                if(i<n)
                {
                    st.add(s.charAt(i));
                }
           }
           else{
               st.add(s.charAt(i));
              
           }
           i+=1;
            
        }
        
        String ans="";
        while(st.size()>0){
            ans=st.pop()+ans;
        }
        return ans;
    }
}