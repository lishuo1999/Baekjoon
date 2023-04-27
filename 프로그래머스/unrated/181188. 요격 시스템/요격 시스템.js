function solution(targets) {
    var answer = 0;
    targets.sort((a, b) => a[1] - b[1])
    var tmp = targets[0][1];
    answer++;
    for (let i=0; i<targets.length; i++) {
        if (targets[i][0] >= tmp){
            answer++;
            tmp = targets[i][1];
        }
    }
    return answer;
}