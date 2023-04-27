function solution(players, callings) {
    var answer = [];
    const indices = {}; // 인덱스 저장할 객체
    for (let i = 0; i < players.length; i++) {
      indices[players[i]] = i;
    }
    
    for (let i = 0; i < callings.length; i++) {
      const index = indices[callings[i]];
      [players[index], players[index-1]] = [players[index-1], players[index]];
      indices[players[index]] = index;
      indices[players[index-1]] = index - 1;
    }
    answer = players;
    return answer;
  }