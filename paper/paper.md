---
title: 'IndoTextKit: A Lightweight and Modular Python Library for Indonesian Text Preprocessing and Normalization'
tags:
  - Python
  - NLP
  - Indonesian
  - text processing
  - slang normalization
  - text cleaning
authors:
  - name: [Adam Dorman]
    orcid: 0000-0000-0000-0000 # (Nanti bikin akun ORCID kalau belum punya, gratis)
    affiliation: 1
affiliations:
 - name: Information Systems Department, [Pembangunan Nasional Veteran Jakarta University], Indonesia
   index: 1
date: 25 December 2025
bibliography: paper.bib
---

# Summary

The rapid growth of social media usage in Indonesia has produced a massive amount of unstructured text data. This data is often filled with colloquialisms, internet slang, abbreviations, and noise (such as URLs and emojis), making it difficult to process using standard Natural Language Processing (NLP) tools trained on formal Indonesian. **IndoTextKit** is a Python library designed to bridge this gap. It provides a lightweight, modular, and easy-to-use interface for cleaning noise and normalizing informal Indonesian text into formal language, preparing it for downstream tasks like sentiment analysis, topic modeling, or machine translation.

# Statement of Need

Researchers and data scientists working with Indonesian social media data (e.g., from Twitter/X, Instagram, Shopee reviews) face a significant bottleneck: text preprocessing. While general-purpose tools like NLTK or spaCy exist, they lack specific support for the dynamic and evolving nature of Indonesian slang (*bahasa gaul*). Existing local tools often focus heavily on stemming (e.g., Sastrawi) but do not address the slang normalization problem comprehensively.

**IndoTextKit** addresses this need by offering:
1.  **Automated Normalization:** A dictionary-based normalizer utilizing a curated dataset of over 4,000 slang words, combining the Colloquial Indonesian Lexicon [@salsabila2018] with modern internet slang.
2.  **Noise Removal:** Optimized regex-based modules to strip URLs, mentions, hashtags, and numbers.
3.  **Modular Design:** Users can use specific modules (only cleaning or only normalizing) depending on their research needs.

This library is designed for students, researchers, and developers who need a "plug-and-play" solution to clean Indonesian text data without building their own preprocessing pipelines from scratch.

# Acknowledgements

We acknowledge the work of Salsabila et al. for their public dataset on Indonesian colloquialisms, which serves as a foundation for the normalization module.

# References