=================================================

PAC-MAN AI USING Q-LEARNING \& ADVERSARIAL SEARCH

=================================================



Version     : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Language    : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Category    : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Framework   : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



=================================================

PROJECT OVERVIEW

=================================================



Project ini mengimplementasikan berbagai algoritma

Artificial Intelligence pada permainan Pac-Man untuk

mempelajari pengambilan keputusan otomatis dalam

lingkungan yang dinamis.



Algoritma yang tersedia:



1\. Reflex Agent

&#x20;  - Mengambil keputusan berdasarkan kondisi saat ini.

&#x20;  - Tidak mempertimbangkan langkah masa depan.



2\. Minimax Agent

&#x20;  - Menggunakan pencarian adversarial.

&#x20;  - Mengasumsikan ghost bermain optimal.



3\. Alpha-Beta Agent

&#x20;  - Optimasi Minimax menggunakan pruning.



4\. Expectimax Agent

&#x20;  - Menganggap ghost bergerak secara probabilistik.



5\. Q-Learning Agent

&#x20;  - Reinforcement Learning berbasis reward.

&#x20;  - Belajar dari pengalaman bermain.



=================================================

GAME OBJECTIVE

=================================================



Tujuan Pac-Man adalah:



\- Mengumpulkan seluruh food pellet.

\- Menghindari ghost.

\- Memanfaatkan power capsule.

\- Memaksimalkan score.

\- Menyelesaikan level dengan jumlah langkah minimum.



=================================================

PROJECT ARCHITECTURE

=================================================



+-----------------------+

|      pacman.py        |

+-----------+-----------+

&#x20;           |

&#x20;           v

+-----------------------+

|       game.py         |

+-----------+-----------+

&#x20;           |

&#x20;           v

+-----------------------+

|   Agent Controller    |

+-----------+-----------+

&#x20;           |

&#x20;   +-------+-------+

&#x20;   |               |

&#x20;   v               v

Pacman Agent    Ghost Agent

&#x20;   |               |

&#x20;   +-------+-------+

&#x20;           |

&#x20;           v

&#x20;    Game Environment



=================================================

DIRECTORY STRUCTURE

=================================================



\##Example##



Pac-Man-QLearning

│

├── assets

├── docs

├──src/

&#x09;│

&#x09;├── agents/

&#x09;│   ├── ghostAgents.py

&#x09;│   ├── keyboardAgents.py

&#x09;│   ├── multiAgents.py

&#x09;│   └── pacmanAgents.py

&#x09;│

&#x09;├── core/

&#x09;│   ├── game.py

&#x09;│   ├── layout.py

&#x09;│   └── util.py

&#x09;│

&#x09;├── display/

&#x09;│   ├── graphicsDisplay.py

&#x09;│   ├── graphicsUtils.py

&#x09;│   └── textDisplay.py

&#x09;│

&#x09;└── layouts/

│

├── tests

│

├── README.md

├── requirements.txt

└── LICENSE



=================================================

QUICK START

=================================================



Menjalankan game:



python pacman.py



Menjalankan layout tertentu:



python pacman.py -l mediumClassic



Menjalankan tanpa GUI:



python pacman.py -q



Menjalankan dengan keyboard:



python pacman.py -p KeyboardAgent



=================================================

AI AGENT EXECUTION

=================================================



Reflex Agent:



python pacman.py -p ReflexAgent



Minimax Agent:



python pacman.py -p MinimaxAgent



Minimax depth 3:



python pacman.py -p MinimaxAgent -a depth=3



Alpha-Beta Agent:



python pacman.py -p AlphaBetaAgent



Expectimax Agent:



python pacman.py -p ExpectimaxAgent



=================================================

PERFORMANCE EVALUATION

=================================================



Untuk mengevaluasi agent gunakan:



python pacman.py -p ReflexAgent -n 10 -q



Keterangan:



\-n 10

&#x20;   Menjalankan 10 game.



\-q

&#x20;   Menonaktifkan GUI.



Metrik evaluasi:



\- Average Score

\- Win Rate

\- Survival Time

\- Number of Steps

\- Food Collected

\- Ghost Encounters



=================================================

DEBUGGING

=================================================



Menampilkan informasi lebih detail:



python pacman.py --help



Menguji layout sederhana:



python pacman.py -l testClassic



Menguji layout minimax:



python pacman.py -l minimaxClassic



=================================================

AUTOGRADER

=================================================



Project mendukung autograder UC Berkeley.



Menjalankan seluruh test:



python autograder.py



Menjalankan test tertentu:



python autograder.py -q q1



=================================================

REINFORCEMENT LEARNING CONCEPT

=================================================



Q-Learning menggunakan persamaan:



:contentReference\[oaicite:0]{index=0}



Dimana:



Q(s,a)  = nilai aksi

α       = learning rate

γ       = discount factor

r       = reward

s       = state



=================================================

FUTURE IMPROVEMENTS

=================================================



Beberapa pengembangan yang direkomendasikan:



\[AI]

\- \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\[GAMEPLAY]

\- \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\[ANALYTICS]

\- \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\[ENGINEERING]

\- \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

=================================================

SYSTEM REQUIREMENTS

=================================================



Minimum:



CPU      : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

RAM      : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Python   : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



Recommended:



CPU      : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

RAM      : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Python   : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



=================================================

REFERENCES

=================================================



\*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



=================================================

LICENSE

=================================================



\*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



=================================================

AUTHOR

=================================================



Project : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Purpose : \*\*\*\*\*\*\*\*\*ISI SENDIRI \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



=================================================

