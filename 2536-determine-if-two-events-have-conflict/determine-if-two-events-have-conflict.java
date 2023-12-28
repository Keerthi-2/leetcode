class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        
        int event1Start = Integer.parseInt(event1[0].substring(0, 2)) * 60 + Integer.parseInt(event1[0].substring(3));

int event1End = Integer.parseInt(event1[1].substring(0, 2)) * 60 + Integer.parseInt(event1[1].substring(3));

int event2Start = Integer.parseInt(event2[0].substring(0, 2)) * 60 + Integer.parseInt(event2[0].substring(3));

int event2End = Integer.parseInt(event2[1].substring(0, 2)) * 60 + Integer.parseInt(event2[1].substring(3));

//System.out.println(event1Start + " " + event1End + " " + event2Start + " " + event2End);

if (event1End >= event2Start && event1Start <= event2Start) {

return true;

} else if (event1Start <= event2End && event1Start >= event2Start) {

return true;
   //( (2,4) (1,3)
}

return false;
    }
}