
Comparing QAE and CAE:

In terms of Precision, Accuracy, Recall, F1-Score, Matrix Report, Classification Report, AUROC

Time includes loading and inference time.

Left shots empty, tried with shots=1024, but end up anomaly looks like normal

CAE large trained on 761,875 datapoints
CAE small trained on 1,000 datapoints
QAE trained on 1,000 datapoints (SWAP Test)
**On Testing dataset (high anomalous) - Macro scores**

Classical:
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{8F Classical AE (Large)} & 0.82 & 0.95 & 0.97 & 0.87 & 0.963 & TP=161312, FP=107, FN=10147, TN=17401 & 0.0756 \\
\hline
\text{8F Classical AE (Small)} & 0.76 & 0.91 & 0.94 & 0.81 & 0.969 & TP=155531, FP=444, FN=15928, TN=17064  & 0.0741 \\
\hline
\text{10F Classical AE (Large)} & 0.79 & 0.93 & 0.82 & 0.80 & 0.955 & TP=163657, FP=5547, FN=7802, TN=11961 & 0.0700 \\
\hline
\text{16F Classical AE (Large)} & 0.80 & 0.94 & 0.91 & 0.84 & 0.962 & TP=161467, FP=1958, FN=9992, TN=15550 & 0.0867 \\
\hline
\end{array}
$$

Amplitude Encoding:
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{8F Amplitude+ RA1 QAE (3+3qbit)} & 0.71 & 0.88 & 0.91 & 0.76 & 0.914 & TP=149607, FP=1020, FN=21852, TN=16488 & 657.9677 \\
\hline
\text{8F Amplitude+ RA3 QAE (3+3qbit)} & 0.57 & 0.83 & 0.59 & 0.58 & 0.413 & TP=151805, FP=12262, FN=19654, TN=5246 & 1900.4211s \\
\hline
\text{8F Amplitude+ Pauli1 QAE (3+3qbit)} & 0.69 & 0.88 & 0.76 & 0.71 & 0.859 & TP=156423, FP=6830, FN=15036, TN=10678 & 638.4235s \\
\hline
\text{8F Amplitude+ Pauli3 QAE (3+3qbit)} & 0.71 & 0.88 & 0.90 & 0.76 & 0.110 & TP=150620, FP=1431, FN=20839, TN=16077 & 738.8952s \\
\hline
\text{16F Amplitude + RA1 QAE (4+3qbit)} & 0.66 & 0.83 & 0.85 & 0.70 & 0.851 & TP=142548, FP=2291, FN=28911, TN=15217 & 586.2585 \\
\hline
\text{16F Amplitude + RA3 QAE (4+3qbit)} & 0.68 & 0.87 & 0.79 & 0.71 & 0.788 & TP=151829, FP=5264, FN=19630, TN=12244 & 833.7029s \\
\hline
\text{32F Amplitude + RA1 QAE (5+3qbit)} & 0.66 & 0.84 & 0.82 & 0.69 & 0.132 & TP=144014, FP=3574, FN=27445, TN=13934 & 639.9032s \\
\hline
\text{32F Amplitude + RA3 QAE (5+3qbit)} & 0.72 & 0.91 & 0.66 & 0.68 & 0.540 & TP=165251, FP=11203, FN=6208, TN=6305 & 848.7447s \\
\hline
\end{array}
$$

Angle Encoding:
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{8F Angle+ RA1 QAE (8+3qbit)} & 0.69 & 0.90 & 0.68 & 0.69 & 0.537 & TP=161687, FP=10056, FN=9772, TN=7452 & 695.3718s \\
\hline
\text{8F Angle + RA3 QAE (8+3qbit)} & 0.68 & 0.89 & 0.71 & 0.69 & 0.583 & 159840, FP=9086, FN=11619, TN=8422 & 1049.0635s \\
\hline
\text{8F Angle + Pauli1 QAE (8+3qbit)} & 0.64 & 0.90 & 0.53 & 0.53 & 0.552 & TP=169347, FP=16272, FN=2112, TN=1236 & 1427.5716s \\
\hline
\text{8F Angle + Pauli3 QAE (8+3qbit)} & 0.68 & 0.88 & 0.74 & 0.71 & 0.120 & TP=157129, FP=7506, FN=14330, TN=10002 & 1170.6053s \\
\hline
\text{10F Angle + RA3 QAE (10+3qbit)} & & & & & & & \\
\hline
\end{array}
$$

Dense Angle Encoding:
- 8F2 means 3 latent 1 trash
- 8F means 2 latent 2 trash
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{8F Dense + RA1 QAE (4+3qbit)} & 0.69 & 0.87 & 0.87 & 0.73 & 0.895 & TP=148210, FP=3962, FN=23249, TN=13546 & 539.0609 \\
\hline
\text{8F Dense + RA3 QAE (4+3qbit)} & 0.31 & 0.14 & 0.14 & 0.12 & 0.086 & TP=148349, FP=2209, FN=23110, TN=15299 & 937.6973s \\
\hline
\text{8F Dense + Pauli1 QAE (4+3qbit)} & 0.81 & 0.94 & 0.93 & 0.86 & 0.918 & TP=161990, FP=1550, FN=9469, TN=15958 & 473.7450s \\
\hline
\text{8F Dense + Pauli3 QAE (4+3qbit)} & 0.67 & 0.86 & 0.82 & 0.71 & 0.131 & TP=148893, FP=4021, FN=22566, TN=13487 & 648.7574s \\
\hline
\text{8F Dense + Pauli5 QAE (4+3qbit)} & 0.65 & 0.79 & 0.86 & 0.66 & 0.893 & TP=132921, FP=1030, FN=38538, TN=16478 & 763.6089s \\
\hline
\text{16F Dense + RA1 QAE (8+3qbit)} & 0.44 & 0.39 & 0.33 & 0.31 & 0.253 & TP=69375, FP=13170, FN=102084, TN=4338 & 803.1847s \\
\hline
\text{16F Dense + RA3 QAE (8+3qbit)} & 0.17 & 0.08 & 0.40 & 0.08 & 0.286 & TP=1247, FP=3486, FN=170212, TN=14022 & 1054.5358s \\
\hline
\text{16F Dense + Pauli1 QAE (8+3qbit)} & 0.85 & 0.92 & 0.61 & 0.65 & 0.094 & TP=170285, FP=13586, FN=1174, TN=3922 & 792.5153s \\
\hline
\text{16F Dense + Pauli3 QAE (8+3qbit)} & 0.63 & 0.91 & 0.51 & 0.49 & 0.395 & TP=170873, FP=17197, FN=586, TN=311 & 1909.7379s \\
\end{array}
$$

Efficient SU2 Encoding (default reps=1):
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & & \textbf{AUROC} \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{16F Efficient SU2 + RA1 QAE (4+3qbit)} & 0.54 & 0.79 & 0.57 & 0.54 & 0.429 & TP=143108, FP=12110, FN=28351, TN=5398 & 1115.8412 \\
\hline
\text{16F Efficient SU2 + RA3 QAE (4+3qbit)} & 0.26 & 0.09 & 0.17 & 0.09 & 0.049 & TP=12192, FP=12695, FN=159267, TN=4813 & 1263.9179 \\
\hline
\text{24F Efficient SU2 + RA1 QAE (6+3qbit)} & 0.55 & 0.89 & 0.52 & 0.51 & 0.597 & TP=167128, FP=16512, FN=4331, TN=996 & 1556.3941 \\
\hline
\text{24F Efficient SU2 R3 + RA1 QAE (6+3qbit)} & 0.62 & 0.86 & 0.65 & 0.63 & 0.814 & TP=155604, FP=10483, FN=15855, TN=7025 & 2142.1510s \\
\hline
\text{24F Efficient SU2 R3 + Pauli1 QAE (6+3qbit)} & 0.67 & 0.89 & 0.65 & 0.66 & 0.453 & TP=162275, FP=11434, FN=9184, TN=6074 & 1822.2099s \\
\hline
\end{array}
$$


We can also try with the PauliTwoAnsatz 
or different Entanglements for RA
	- Current is on "reverse_linear"
	- For Angle: Full, linear is poor havent tried the rest
	- https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.n_local

**Flipped?**
- 32F Amplitude + RA1 
- 8F Amplitude + Pauli3
- 8F Dense + RA3 
- 16F Dense + RA1/3
- 16F Dense + Pauli

Select the best QAE then get metrics for (CAE too)
5k samples
10k samples
20k samples
plot graph

**SHORTLISTED**
8F Classical AE
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{1,000 Samples} & 0.76 & 0.91 & 0.94 & 0.81 & 0.969 & TP=155531, FP=444, FN=15928, TN=17064  & 0.0741 \\
\hline
\text{5,000 Samples} & & & & & & & \\
\hline
\text{10,000 Samples} & & & & & & & \\
\hline
\text{20,0000 Samples} & & & & & & & \\
\hline
\text{Full} & 0.82 & 0.95 & 0.97 & 0.87 & 0.963 & TP=161312, FP=107, FN=10147, TN=17401 & 0.0756 \\
\hline
\end{array}
$$

8F Dense + Pauli QAE (4+3qbit)
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{1,000 Samples (1 rep)} & 0.69 & 0.88 & 0.78 & 0.72 & 0.692 & TP=15490, FP=5941, FN=16519, TN=11567 & 760.3842s \\
\hline
\text{3,000 Samples (1 rep)} & & & & & & & \\
\hline
\text{3,000 Samples (2 reps)} & 0.71 & 0.88 & 0.90 & 0.76 & 0.926 & TP=150062, FP=1340, FN=21397,TN=16168 & 685.1486s \\
\hline
\text{3,000 Samples (3 reps)} & 0.66 & 0.89 & 0.63 & 0.65 & 0.297 & TP=162835, FP=11940, FN=8624, TN=5568 & 712.9864s \\
\hline
\text{5,000 Samples (3 reps)} & 0.71 & 0.90 & 0.71 & 0.71 & 0.611 & TP=161922, FP=9062, FN=9537, TN=8446 & 752.3155s \\
\hline
\text{5,000 Samples (4 reps)} & 0.69 & 0.89 & 0.69 & 0.69 & 0.488 & TP=161372, FP=9876, FN=10087, TN=7632 & 708.4284s \\
\hline
\text{5,000 Samples (5 reps)} & 0.68 & 0.89 & 0.67 & 0.67 & 0.231 & TP=161458, FP=10429, FN=10001, TN=7079 & 868.5664s \\
\hline
\end{array}
$$

Also try 5 sets of 1k samples and see differences (eh wait I realised my sample selection was always random)

____________
In terms of Performance with Smaller and Larger Datasets
- Does Smaller datasets in QAE perform better? etc.




Tried Adam + Estimator
- Still Overlap, 3 hours to train for 1 Epoch of Batch 64 on 10k Samples


Lol ok redo without feature reduction with CAE, 

Select 8 Features, on First 1000 Samples for 60 COBYLA Iterations
Except Efficient SU2 is 24 features

**First-N**
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude + RA1 (3+3qbit)} & 0.80 & 0.92 & 0.68 & 0.72 & 0.872 & TP=168185, FP=10986, FN=3274, TN=6522 & 784.6801s \\
\hline
\text{Amplitude + RA3 (3+3qbit)} & 0.79 & 0.93 & 0.73 & 0.75 & 0.899 & TP=166641, FP=9125, FN=4818, TN=8383 & 857.0893s \\
\hline
\text{Amplitude + Pauli1 (3+3qbit)} & 0.69 & 0.88 & 0.77 & 0.72 & 0.790 & TP=156068, FP=6450, FN=15391, TN=11058 & 538.5516s \\
\hline
\text{Amplitude + Pauli3 (3+3qbit)} & 0.79 & 0.92 & 0.60 & 0.64 & 0.424 & TP=169472, FP=13734, FN=1987, TN=3774 & 660.2520s \\
\hline
\text{Dense + RA1 (4+3qbit)} & 0.81 & 0.94 & 0.95 & 0.86 & 0.960 & TP=161620, FP=835, FN=9839, TN=16673 & 672.3176s \\
\hline
\text{Dense + RA3 (4+3qbit)} & 0.81 & 0.94 & 0.94 & 0.86 & 0.955 & TP=161313, FP=1010, FN=10146, TN=16498 & 819.0662s \\
\hline
\text{Dense + Pauli1 (4+3qbit)} & 0.69 & 0.88 & 0.80 & 0.72 & 0.918 & TP=153759, FP=5186, FN=17700, TN=12322 & 704.9696s \\
\hline
\text{Dense + Pauli3 (4+3qbit)} & 0.68 & 0.88 & 0.79 & 0.72 & 0.096 & TP=153322, FP=5373, FN=18137, TN=12135 & 658.3439s \\
\hline
\text{Angle + RA1 (8+3qbit)} & 0.69 & 0.86 & 0.88 & 0.74 & 0.864 & TP=147217, FP=1552, FN=24242, TN=15956 & 779.1593s \\
\hline
\text{Angle + RA3 (8+3qbit)} & 0.80 & 0.94 & 0.92 & 0.85 & 0.896 & TP=161769, FP=1788, FN=9690, TN=15720 & 1025.4575s \\
\hline
\text{Angle + Pauli1 (8+3qbit)} & 0.69 & 0.88 & 0.80 & 0.73 & 0.900 & TP=154356, FP=5273, FN=17103, TN=12235 & 904.6889s \\
\hline
\text{Angle + Pauli3 (8+3qbit)} & 0.69 & 0.88 & 0.80 & 0.73 & 0.835 & TP=154546, FP=5377, FN=16913, TN=12131 & 941.1387s \\
\hline
\text{Efficient SU2 R3 + RA1 (6+3qbit)} & 0.62 & 0.86 & 0.65 & 0.63 & 0.814 & TP=155604, FP=10483, FN=15855, TN=7025 & 2142.1510s \\
\hline
\text{Efficient SU2 R3 + RA3 (6+3qbit)} & 0.67 & 0.88 & 0.74 & 0.70 & 0.103 & TP=155281, FP=7336, FN=16178, TN=10172 & 2488.6089s \\
\hline
\text{Efficient SU2 R3 + Pauli1 (6+3qbit)} & 0.67 & 0.89 & 0.65 & 0.66 & 0.453 & TP=162275, FP=11434, FN=9184, TN=6074 & 1822.2099s \\
\hline
\text{Efficient SU2 R3 + Pauli3 (6+3qbit)} & 0.73 & 0.91 & 0.69 & 0.71 & 0.683 & TP=164258, FP=9992, FN=7201, TN=7516 & 2412.7191s \\
\hline
\end{array}
$$


**Shortlisted Models** based off first-N
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude + RA1 (3+3qbit)} & 0.80 & 0.92 & 0.68 & 0.72 & 0.872 & TP=168185, FP=10986, FN=3274, TN=6522 & 784.6801s \\
\hline
\text{Amplitude + RA3 (3+3qbit)} & 0.79 & 0.93 & 0.73 & 0.75 & 0.899 & TP=166641, FP=9125, FN=4818, TN=8383 & 857.0893s \\
\hline
\text{Dense + RA1 (4+3qbit)} & 0.81 & 0.94 & 0.95 & 0.86 & 0.960 & TP=161620, FP=835, FN=9839, TN=16673 & 672.3176s \\
\hline
\text{Dense + RA3 (4+3qbit)} & 0.81 & 0.94 & 0.94 & 0.86 & 0.955 & TP=161313, FP=1010, FN=10146, TN=16498 & 819.0662s \\
\hline
\end{array}
$$

Try different feature selection methods

1. Autoencoder - Dimensionality Reduction (DONE)
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude+ RA1 (3+3qbit)} & 0.71 & 0.88 & 0.91 & 0.76 & 0.914 & TP=149607, FP=1020, FN=21852, TN=16488 & 657.9677 \\
\hline
\text{Amplitude+ RA3 (3+3qbit)} & 0.57 & 0.83 & 0.59 & 0.58 & 0.413 & TP=151805, FP=12262, FN=19654, TN=5246 & 1900.4211s \\
\hline
\text{Dense + RA1 (4+3qbit)} & 0.69 & 0.87 & 0.87 & 0.73 & 0.895 & TP=148210, FP=3962, FN=23249, TN=13546 & 539.0609 \\
\hline
\text{Dense + RA3 (4+3qbit)} & 0.73 & 0.91 & 0.69 & 0.71 & 0.085 & TP=164453, FP=10051, FN=7006, TN=745 & 937.6973s \\
\hline
\end{array}
$$
 
2. PCA - Dimensionality Reduction
Dense F1: 0.49, 0.48
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude + RA1 (3+3qbit)} & 0.72 & 0.89 & 0.91 & 0.77 & 0.905 & TP=150832, FP=1097, FN=20627, TN=16411 & 557.8209s \\
\hline
\text{Amplitude + RA3 (3+3qbit)} & 0.72 & 0.89 & 0.91 & 0.77 & 0.921 & TP=150976, FP=1060, FN=20483, TN=16448 & 911.5760s \\
\hline
\end{array}
$$

3. PCA - Feature Extraction / Filter
Selected: *6  0 21 17 11 16  4  5*
Amplitude F1: 0.64
Others are pretty bad
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Dense + RA1 (4+3qbit)} & 0.69 & 0.88 & 0.81 & 0.73 & 0.918 & TP=152812, FP=4635, FN=18647, TN=12873 & 491.4111s \\
\hline
\end{array}
$$

5. Mutual Information - Supervised Statistical Filter Method (try again but just normal to feature selection)
*Selected: 20 10 15  0  1 11 13  9*
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude + RA1 (3+3qbit)} & 0.79 & 0.91 & 0.57 & 0.60 & 0.325 & TP=170003, FP=14777, FN=1456, TN=2731 & 703.1709s \\
\hline
\text{Amplitude + RA3 (3+3qbit)} & 0.71 & 0.91 & 0.69 & 0.70 & 0.655 & TP=163712, FP=10186, FN=7747, TN=7322 & 735.3668s \\
\hline
\text{Dense + RA1 (4+3qbit)} & 0.77 & 0.92 & 0.75 & 0.76 & 0.613 & TP=165097, FP=8243, FN=6362, TN=9265 & 646.9557s \\
\hline
\text{Dense + RA3 (4+3qbit)} & 0.78 & 0.92 & 0.75 & 0.76 & 0.924 & TP=165234, FP=8236, FN=6225, TN=9272 & 731.5439s \\
\hline
\end{array}
$$

6. ANOVA- Supervised Statistical Filter Method
Selected: 22  2 17 16 19 21 18  1
Amplitude F1: 0.79
Dense F1: 0.09
Distribution is poor, no/barely any difference between anomaly/normal.


7. Kendall's - Supervised Statistical Filter Method
Selected: *2 21 22  1 17 16 19 18*
Amplitude F1:  0.63, 0.66
Dense F1: 0.09
Distribution is poor, no/barely any difference between anomaly/normal.
Though an interesting result for the Amplitude case is threshold between 0.1 and 0.4
![[Pasted image 20250812140211.png]]

9. Last N & Middle N
Looks bad

10. Least Correlated
Selected: 4, 5, 3, 1, 0, 16, 23, 18
Amplitude F1: 0.68
Dense F1: 0.08
Distribution is poor, no/barely any difference between anomaly/normal.
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{Amplitude + RA1 (3+3qbit)} & & & & & & & \\
\hline
\text{Amplitude + RA3 (3+3qbit)} & & & & & & & \\
\hline
\text{Dense + RA1 (4+3qbit)} & & & & & & & \\
\hline
\text{Dense + RA3 (4+3qbit)} & & & & & & & \\
\hline
\end{array}
$$



**BEST MODEL**
Up samples (and reps of selected)

8F Classical AE
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{1,000 Samples} & 0.76 & 0.91 & 0.94 & 0.81 & 0.969 & TP=155531, FP=444, FN=15928, TN=17064  & 0.0741s \\
\hline
\text{5,000 Samples} & 0.73 & 0.90 & 0.92 & 0.78 & 0.961 & TP=152844, FP=999, FN=18615, TN=16509 & 0.0963s \\
\hline
\text{10,000 Samples} & 0.77 & 0.92 & 0.88 & 0.81 & 0.892 & TP=159817, FP=2999, FN=11642, TN=14509 & 0.1234s \\
\hline
\text{20,0000 Samples} & 0.81 & 0.94 & 0.94 & 0.86 & 0.898 & TP=161605, FP=1264, FN=9854, TN=16244 & 0.0965s \\
\hline
\text{Full} & 0.82 & 0.95 & 0.97 & 0.87 & 0.963 & TP=161312, FP=107, FN=10147, TN=17401 & 0.0756s \\
\hline
\end{array}
$$

First-N + 8F Dense +  RA QAE (4+3qbit)
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{1,000 Samples (1 rep)} & 0.81 & 0.94 & 0.95 & 0.86 & 0.960 & TP=161620, FP=835, FN=9839, TN=16673 & 672.3176s \\
\hline
\text{5,000 Samples (1 reps)} & 0.70 & 0.87 & 0.90 & 0.74 & 0.902 & TP=147168, FP=1046, FN=24291, TN=16462 & 436.5684s \\
\hline
\text{5,000 Samples (2 reps)} & 0.82 & 0.95 & 0.97 & 0.87 & 0.965 & TP=161313, FP=57, FN=10146, TN=17451 & 580.4456s \\
\hline
\text{5,000 Samples (3 reps)} & 0.79 & 0.94 & 0.91 & 0.84 & 0.930 & TP=161313, FP=2127, FN=10146, TN=15381 & 602.6237s \\
\hline
\text{10,000 Samples (2 reps)} & 0.80 & 0.94 & 0.91 & 0.84 & 0.952 & TP=161774, FP=2091, FN=9685, TN=15417 & 605.7277s \\
\hline
\text{10,000 Samples (3 reps)} & 0.79 & 0.94 & 0.91 & 0.84 & 0.912 & TP=161313, FP=2127, FN=10146, TN=15381 & 671.7445s \\
\hline
\text{10,000 Samples (4 reps)} & 0.79 & 0.93 & 0.89 & 0.83 & 0.867 & TP=161748, FP=2870, FN=9711, TN=14638 &  700.3153s \\
\hline
\text{10,000 Samples (5 reps)} & 0.81 & 0.94 & 0.94 & 0.86 & 0.951 & TP=161640, FP=1062, FN=9819, TN=16446 & 837.1920s \\
\hline
\text{20,000 Samples (5 reps)} & 0.73 & 0.90 & 0.92 & 0.79 & 0.949 & TP=153175, FP=957, FN=18284, TN=16551 & 827.3391s\\
\hline
\text{20,000 Samples (6 reps)} & 0.80 & 0.94 & 0.92 & 0.85 & 0.961 & TP=161550, FP=1899, FN=9909, TN=15609 & 788.4926s \\
\hline
\text{20,000 Samples (7 reps)} & 0.79 & 0.93 & 0.90 & 0.84 & 0.911 & TP=161639, FP=2557, FN=9820, TN=14951 & 853.6726s\\
\hline
\end{array}
$$


Full 8F CAE + Isolation Forest / NCE
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{CAE + IF w/Contamination = 0.1} & 0.63 & 0.88 & 0.63 & 0.63 & 0.650 & TP=159862, FP=11740, FN=11597, TN=5768  & N.A. \\
\hline
\text{CAE + NCE} & 0.68 & 0.90 & 0.62 & 0.64 & 0.943 & TP=165320, FP=12673, FN=6139, TN=4835 & N.A. \\
\hline
\text{CAE + NCE \& IF w/Contamination = 0.1} & 0.63 & 0.89 & 0.57 & 0.59 & 0.518 & TP=165942, FP=14543, FN=5517, TN=2965 & N.A. \\
\hline
\end{array}
$$


5k, 8F Dense RA2 QAE + Isolation Forest / NCE
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{QAE + IF w/Contamination = 0.1} & 0.45 & 0.13 & 0.47 & 0.13 & 0.510 & TP=8412, FP=1827, FN=163047, TN=15681 & N.A. \\
\hline
\text{QAE + NCE} & 0.81 & 0.91 & 0.57 & 0.59 & 0.971 & TP=170459, FP=15090, FN=1000, TN=2418 & N.A. \\
\hline
\end{array}
$$

_______________
24F CAE Random 5000
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{CAE Random 5k 1} & 0.75 & 0.92 & 0.84 & 0.79 & 0.872 & TP=159793, FP=4388, FN=11666, TN=13120 & 0.1581s \\
\hline
\text{CAE Random 5k 2} & 0.74 & 0.91 & 0.85 & 0.78 & 0.877 & TP=158463, FP=4089, FN=12996, TN=13419 & 0.0995s \\
\hline
\text{CAE Random 5k 3} & 0.70 & 0.90 & 0.75 & 0.72 & 0.755 & TP=159465, FP=7521, FN=11994, TN=9987 & 0.0851s \\
\hline
\text{CAE Random 5k 4} & 0.72 & 0.90 & 0.84 & 0.76 & 0.846 & TP=155981, FP=4018, FN=15478, TN=13490 & 0.1045s \\
\hline
\text{CAE First 5k} & 0.73 & 0.90 & 0.92 & 0.78 & 0.961 & TP=152844, FP=999, FN=18615, TN=16509 & 0.0963s \\
\hline
\text{CAE Average} & 0.73 & 0.90 & 0.84 & 0.77 & 0.862 & TP=157309, FP=4203, FN=14150, TN=13305 & 0.1087s \\
\hline
\end{array}
$$

8f CAE Random 5000
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{CAE Random 5k 1} & 0.73 & 0.90 & 0.87 & 0.78 & 0.914 & TP=155948, FP=3031, FN=15511, TN=14477 & 0.0716s \\
\hline
\text{CAE Random 5k 2} & 0.74 & 0.91 & 0.84 & 0.77 & 0.939 & TP=158196, FP=4302, FN=13263, TN=13206 & 0.0690s \\
\hline
\text{CAE Random 5k 3} & 0.72 & 0.89 & 0.84 & 0.76 & 0.816 & TP=155466, FP=4105, FN=15993, TN=13403 & 0.0652s \\
\hline
\text{CAE Random 5k 4} & 0.70 & 0.89 & 0.83 & 0.74 & 0.925 & TP=154240, FP=4234, FN=17219, TN=13274 & 0.0677s \\
\hline
\text{CAE First 5k} & 0.72 & 0.92 & 0.85 & 0.79 & 0.913 & TP=159567, FP=4018, FN=11892, TN=13490 & 0.0631s \\
\hline
\text{CAE Average} & 0.72 & 0.90 & 0.85 & 0.77 & 0.901 & TP=156883, FP=3938, FN=14776, TN=13570 & 0.0673s \\
\hline
\end{array}
$$

8F QAE Random 5000
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{QAE Random 5k 1} & 0.70 & 0.88 & 0.86 & 0.75 & 0.875 & TP=151986, FP=3033, FN=19473, TN=14475 & 559.8888s \\
\hline
\text{QAE Random 5k 2} & 0.79 & 0.93 & 0.88 & 0.83 & 0.878 & TP=161774, FP=3058, FN=9685, TN=14450 & 746.1335s \\
\hline
\text{QAE Random 5k 3} & 0.79 & 0.93 & 0.89 & 0.83 & 0.906 & TP=161677, FP=3024, FN=9782, TN=14484 & 736.3817s \\
\hline
\text{QAE Random 5k 4} & 0.80 & 0.94 & 0.91 & 0.84 & 0.923 & TP=161749, FP=2115, FN=9710, TN=15393 & 616.5363s \\
\hline
\text{QAE First 5k} & 0.82 & 0.95 & 0.97 & 0.87 & 0.965 & TP=161313, FP=57, FN=10146, TN=17451 & 580.4456s \\
\hline
\text{QAE Average} & 0.78 & 0.93 & 0.90 & 0.82 & 0.909 & TP=159700, FP=2257, FN=11759, TN=15251 & 647.88s \\
\hline
\end{array}
$$

_____
Hardware attempt 1 - I think it was still simulating
![[Pasted image 20250818094545.png]]

Attempt 2 - 

______________
Why First N best?
- First N has good variance coverage (some lows, some low-mid, some highs)
- Good separation based on tSNE
![[Pasted image 20250815163723.png]]

- Compared to other methods used, for example Mutual Information:
![[Pasted image 20250815163838.png]]

- To test we define a balance variance feature selection method, noting good tSNE separability as well.
![[Pasted image 20250815163945.png]]
- We then trained the same 8 Feature Dense Real Amplitude 2 Reps model on the first 5k samples and while we did not achieve a *better* model we managed to achieve a similar distribution to First-N where there is generally good separation. However there is still significantly high FN and FPs.

![[Pasted image 20250815164151.png]]
![[Pasted image 20250831190711.png]]

__________

Next Steps
- Plot Expressibility of Amplitude, Angle, Dense-Angle and EfficientSU2 Embeddings
	- Can refer to https://arxiv.org/pdf/2003.01695
- Run on Quantum Hardware
	- This can't be right? Ok it is!![[Pasted image 20250820144336.png]]
	![[Pasted image 20250820152451.png]]

_________________
Literature Notes
- A key advantage of quantum autoencoders lies in their parameter efficiency and data requirements. Research demonstrates that quantum autoencoders, when augmented with quantum gradient descent for training, are much less dependent on the number of training samples and reach optimal reconstruction performance with minuscule training datasets ([Ngairangbam et al., 2021](https://www.semanticscholar.org/p/245006312)). This efficiency extends to model complexity, where quantum autoencoders with approximately 10 parameters can outperform classical autoencoders with around 1000 parameters in anomaly detection capabilities ([Ngairangbam et al., 2021](https://www.semanticscholar.org/p/245006312)).

- There is still limited understanding of how different ansatz designs and **data embedding strategies impact the performance of quantum autoencoders**, indicating opportunities for further optimization and specialization ([Araz et al., 2024](https://www.semanticscholar.org/p/272524491)). This suggests that the development of specialized quantum autoencoder variants is still in its early stages, with substantial potential for domain-specific optimizations and novel architectural approaches.

____

On other datasets

QAE
$$
\begin{array}{|l|c|c|c|c|c|c|c|c|}
\hline
\textbf{Model} & \textbf{Precision} & \textbf{Accuracy} & \textbf{Recall} & \textbf{F1} & \textbf{AUROC} & \textbf{Matrix} & \textbf{Time (s)} \\
\hline
\text{QAE Goldstein Cancer 8FA Dense RA1} & 0.75 & 0.92 & 0.78 & 0.76 & 0.935 & TP=6, FP=5, FN=4, TN=103 & 5.7667s \\
\hline
\text{QAE Goldstein Letter 8FA Dense RA1} & 0.65 & 0.73 & 0.73 & 0.66 & 0.806 & TP=24, FP=40, FN=9, TN=110 & 12.3663s \\
\hline
\text{QAE Goldstein Letter 8FC Dense RA1} & 0.68 & 0.76 & 0.77 & 0.69 & 0.829 & TP=26, FP=37, FN=7, TN=113 & 13.9951s \\
\hline
\text{QAE Goldstein Pen Global 8FA Dense RA1} & 0.56 & 0.51 & 0.57 & 0.51 & 0.670 & TP=63, FP=123, FN=27, TN=93 & 16.8289s \\
\hline
\text{QAE Goldstein Pen Global 8FC Dense RA1} & 0.58 & 0.53 & 0.59 & 0.52 & 0.715 & TP=67, FP=122, FN=23, TN=94 & 15.6192s \\
\hline
\text{CAE Goldstein Cancer 8FA} & 0.88 & 0.96 & 0.84 & 0.86 & 0.972 & TP=7, FP=2, FN=3, TN=106 & 0.0087 \\
\hline
\text{CAE Goldstein Letter 8FA} & 0.72 & 0.84 & 0.66 & 0.68 & 0.867 & TP=13, FP=10, FN=20, TN=140 & 0.0083\\
\hline
\text{CAE Goldstein Pen Global 8FA} & 0.85 & 0.86 & 0.81 & 0.83 & 0.948 & TP=61, FP=13, FN=29, TN=203 & 0.0256 \\
\hline
\end{array}
$$
