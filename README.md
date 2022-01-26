# 🇬🇧
This project was made as a way to pass [RobôCIn](https://robocin.com.br/)'s selection process.

possession.py plots a graph containing every match result and RoboCIn's team possession percentage in them. The logic behind possession calculation is the following: for each moment of the match where the playmode is 'play_on', meaning the game isn't paused in any way, the possession of the ball is assigned to the closest player to it.

ranking.py plots a bar graph containing a score for each player of RoboCIn's team, minus the goalie. The score of a player is directly proportional to their tackle count, percentual stamina spent and effort made, and the final score is the mean of all matches scores.

# 🇧🇷
Este projeto foi realizado a fim de atingir os requisitos do processo seletivo do [RobôCIn](https://robocin.com.br/).

possession.py cria um gráfico mostrando o resultados de cada partida e a respectiva posse de bola percentual do RobôCIn. A lógica para calcular a posse de bola foi a seguinte: para cada momento da partida que tem o _playmode_ como 'play_on', ou seja, quando não estiver ocorrendo nenhum tipo de pausa no jogo, a posse da bola é atribuída ao jogador que estiver mais próximo dela.

ranking.py desenha um gráfico contendo pontuações dadas aos jogadores, exceto o goleiro. A pontuação é diretamente proporcional à quantidade de roubo de bolas, percentual de _stamina_ gasto e o esforço realizado, sendo a pontuação final a média de todas as pontuações do jogador ao longo de todas as partidas.


