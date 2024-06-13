class Solution {
    public int leastInterval(char[] tasks, int n) {
        int freq[]=new int[26];

        for(char ch:tasks){
            freq[ch-65]+=1;
        }

        int min_slots=tasks.length;
        Arrays.sort(freq);

        int max_freq=freq[25]-1;
        int idle_slots=n*(max_freq);

        for(int i=24;i>=0;i--){
            idle_slots-=Math.min(max_freq,freq[i]);
            if ((idle_slots)<0){
                return min_slots;
            }
        }

        return min_slots+idle_slots;


    }
}