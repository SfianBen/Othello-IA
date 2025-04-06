# 🧠 Othello IA – Projet FDT

Ce projet est un jeu **Othello/Reversi** développé en Python avec une interface graphique via **Tkinter**, pour le module **Fondements de l’Intelligence Artificielle (FDT_IA)**.  
Il inclut plusieurs intelligences artificielles capables de s’affronter automatiquement.

---

## 🎮 Fonctionnalités principales

- ✅ Interface graphique avec Tkinter
- ✅ Mode **Joueur vs IA** ou **IA vs IA**
- ✅ 3 algorithmes d’IA implémentés :
  - MinMax
  - Alpha-Bêta
  - NegaMax
- ✅ 4 fonctions d’évaluation :
  - Score
  - Position
  - Mobilité
  - Mixte (score + position + mobilité)
- ✅ Menu interactif pour lancer une partie
- ✅ Timer + Compteur de tours
- ✅ Fin automatique de la partie
- ✅ Génération de fichiers `.txt` avec les scores d’évaluation IA


---

## 🚀 Lancement

```bash
python main.py
```

> Nécessite Python 3.8+ et la bibliothèque Tkinter (intégrée par défaut)

---

## 📁 Arborescence du projet

```
othello/
├── main.py
├── menu.py
├── game.py
├── logic.py
├── board.py
├── evaluation.py
├── dummy.py
├── ai_minmax.py
├── ai_alphabeta.py
├── ai_negamax.py
```

---

## 📝 Test IA

Tu peux comparer les IA entre elles à travers exemple :
- `alphabeta_score.txt`
- `negamax_mixte.txt`
- `comparaison.txt` : résumé des performances
- `comparaison_scores.png` : courbe des scores IA par tour

---
