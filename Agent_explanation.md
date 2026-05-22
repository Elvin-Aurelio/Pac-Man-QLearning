**MinimaxAgent** 

Agent ini mencari action terbaik untuk dirinya sendiri, dan dia juga berasumsi kalua lawan juga akan melakukan Langkah terbaik (seperti bot catur). 

nilai v diibaratkan sebagai "kebaikan untuk pacman". Agent pacman akan berusaha mencari action yang menghasilkan nilai v maksimum (agar pacman menang), Agentghost akan selalu mencari action yang menghasilkan nilai v minimum (agar pacman tidak menang)



**ReflexAgent**

Agent ini mengambil keputusan dengan mengevaluasi successor state. Successor state adalah kondisi yang akan terjadi setelah sebuah action dilakukan. Agent ini tidak melakukan pencarian berlapis, ia hanya melihat satu Langkah kedepan yang akan terjadi akibat masing masing action (successor state), lalu mengambil keputusan dari successor state tersebut

