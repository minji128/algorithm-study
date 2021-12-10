import java.util.ArrayList;
class Solution {
    public int[] solution(int[] answers) {
        int[] first = {1, 2, 3, 4, 5};
        int[] second = {2,1,2,3,2,4,2,5};
        int[] third = {3,3,1,1,2,2,4,4,5,5};
        int[] cnt = {0,0,0};

        for(int i=0; i<answers.length; i++) {
            if(answers[i] == first[i%first.length]) {cnt[0]++;}
            if(answers[i] == second[i%second.length]) {cnt[1]++;}
            if(answers[i] == third[i%third.length]) {cnt[2]++;}
        }

        int max = Math.max(cnt[0], Math.max(cnt[1], cnt[2]));
        ArrayList<Integer> maxList = new ArrayList<>();

        for(int i=0; i<cnt.length; i++) {
            if(cnt[i] == max) {
                maxList.add(i+1);
            }
        }

        return maxList.stream().mapToInt(i->i).toArray();
    }
}